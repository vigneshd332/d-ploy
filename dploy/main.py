"""
Entrypoint for the API.
"""

import json
import sys
from typing import Any, Generator

import uvicorn
from fastapi import Depends, FastAPI

from dploy.config import Settings
from dploy.database.base import Base
from dploy.database.session import SessionLocal, engine
from dploy.dependencies import check_authentication
from dploy.routers import audit_logs, daemons, keyring, projects, aws, firewall, docker

Base.metadata.create_all(bind=engine)


settings = Settings()
app: FastAPI = FastAPI(dependencies=[Depends(check_authentication)])


def get_db() -> Generator[Any, None, None]:
    """Dependency to get the database"""
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


app.include_router(daemons.router)
app.include_router(projects.router)
app.include_router(keyring.router)
app.include_router(audit_logs.router)
app.include_router(aws.router)
app.include_router(firewall.router)
app.include_router(docker.router)


@app.get("/")
async def root() -> dict[str, str]:
    """Basic route for testing"""
    return {"message": "Working!"}


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "docs":
        print(json.dumps(app.openapi(), indent=4))
    else:
        uvicorn.run(app, host="0.0.0.0", port=8000)
