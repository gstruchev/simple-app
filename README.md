# Simple App

Small demo application to showcase my DevOps skills (Docker, CI/CD, remote deployment).

## Stack

- Python + FastAPI
- Docker, Docker Compose
- GitHub Actions (CI/CD)
- Remote server (VPS / EC2)

## Endpoints

- `GET /` – basic info
- `GET /health` – healthcheck
- `GET /version` – returns app version

## Run locally

```bash
pip install -r app/requirements.txt
pip install pytest
pytest app/tests
uvicorn app.main:app --reload
```

## Run with Docker

```bash
docker build -t devops-portfolio-app -f docker/Dockerfile .
docker run -p 8000:8000 devops-portfolio-app
```

## Production (server)

`infra/docker-compose.prod.yml` defines the app service

GitHub Actions workflow `.github/workflows/ci-cd.yml`:

- runs tests
- builds & pushes Docker image to Docker Hub
- deploys to remote server via SSH