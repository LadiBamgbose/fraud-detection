# Real-Time Fraud Detection (FastAPI + Postgres + Redis)

Production-oriented, real-time fraud detection service built from scratch:
- **FastAPI** inference service
- **PostgreSQL** request/prediction logging (audit + replay later)
- **Redis** for low-latency online features (velocity/rolling counts later)
- **Docker Compose** for local deployment

> Current milestone: **v0.1** — containerized API + Postgres + Redis + `/health` endpoint running locally.

---

## Quickstart (local)

### Prereqs
- Docker Desktop (macOS)

### Run
```bash
docker compose up --build
