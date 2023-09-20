import asyncio
import httpx

from dploy.database.session import SessionLocal
from dploy.schemas.daemons import DaemonSchema

polling_interval = 5 # seconds

async def check_daemon_heartbeat():
    try:
        async with httpx.AsyncClient() as client:
            try:
                # creating sepearte instance of db session to prevent
                # asyncio sleep from blocking other sessions
                database = SessionLocal()
                daemons = database.query(
                DaemonSchema.uuid, DaemonSchema.url, DaemonSchema.name).all()

                for daemon in daemons:
                    response = await client.get(daemon.url)
                    if response.status_code == 200:
                        # Log heartbeat = 1 to influxdb
                        print("Request successful")
                    else:
                        # Log heartbeat = 0 to influxdb
                        print(f"Request failed with status code: {response.status_code}")
            finally:
                database.close()
    except Exception as e:
        print(f"An error occurred: {e}")


async def schedule_health_check():
    while True:
        await check_daemon_heartbeat()
        await asyncio.sleep(polling_interval)