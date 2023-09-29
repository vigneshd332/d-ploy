<h1 align="center">D-Ploy</h1>
<h3 align="center">An utility for automating server operations and deployment pipelines</h3>
<p align="center">
  <a href="https://github.com/delta/d-ploy/actions/workflows/lint.yml">
      <img src="https://github.com/delta/d-ploy/actions/workflows/lint.yml/badge.svg?branch=main"/>
  </a>
  <a href="https://github.com/delta/d-ploy/actions/workflows/ci.yml">
      <img src="https://github.com/delta/d-ploy/actions/workflows/ci.yml/badge.svg"/>
  </a>
  <a href="https://github.com/delta/d-ploy/actions/workflows/docs.yml">
      <img src="https://github.com/delta/d-ploy/actions/workflows/docs.yml/badge.svg"/>
  </a>
  <a href="https://codecov.io/gh/delta/d-ploy">
      <img src="https://codecov.io/gh/delta/d-ploy/branch/main/graph/badge.svg?token=DQuDX4BSjE"/>
  </a>
</p>

## Local development

#### With docker

1. Clone the repo
2. Run `cp .env.example .env`
3. Run `docker-compose up --build`

#### With virtual environment

1. Clone the repo
2. Run `cp .env.example .env`
3. Run `virtualenv --clear venv`
4. Run `source ./venv/bin/activate`
5. Run `pip install -r requirements-dev.txt`
6. Run `pre-commit install` to install the git hooks for linting and testing
7. Run `uvicorn dploy.main:app --reload` to start the server

## License

MIT License

Copyright (c) 2021 Delta Force
