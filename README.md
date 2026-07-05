# Flask DevOps Portfolio Project

## Overview

This project is a production-style Flask REST API built as part of my DevOps portfolio.

It demonstrates modern DevOps practices including:

- Python
- Flask
- Docker
- Docker Compose
- Git
- GitHub
- Pytest
- CI/CD (coming next)
- AWS Deployment (coming next)

---

## Project Structure

```text
portfolio-project-1/
│
├── app/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .github/
```

---

## Features

- REST API
- Health Check Endpoint
- Dockerized Application
- Automated Tests
- Git Version Control

---

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Welcome endpoint |
| `/health` | Health check |

---

## Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
python app/app.py
```

---

## Run with Docker

```bash
docker compose up -d
```

---

## Testing

```bash
pytest
```

---

## Technologies

- Python 3.12
- Flask
- Docker
- Docker Compose
- Git
- GitHub
- Pytest

---

## Author

**Tholiwe Mchunu**