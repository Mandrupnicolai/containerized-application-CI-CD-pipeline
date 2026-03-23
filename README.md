# Containerized App with CI/CD

Small FastAPI app, packaged as a Docker image, with GitHub Actions:
- **CI**: lint + tests + Docker build
- **CD**: build + push image to GitHub Container Registry (GHCR), with an optional SSH deploy job

## Local run (Python)

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt -r requirements-dev.txt
.\.venv\Scripts\python -m uvicorn app.main:app --reload
```

Open `http://localhost:8000/healthz`.

## Local run (Docker)

```powershell
docker compose up --build
```

Open `http://localhost:8000/healthz`.

## CI (GitHub Actions)

Workflow: `.github/workflows/ci.yml`
- Runs `ruff` + `pytest`
- Builds the Docker image (no push)

## CD (GitHub Actions)

Workflow: `.github/workflows/cd.yml`
- Pushes image to GHCR on:
  - `main` (tags include `latest` + `sha-...`)
  - tags like `v1.2.3` (tags include `v1.2.3`)

### Optional deploy job (SSH)

If you add these repository secrets, a `deploy` job runs on pushes to `main`:
- `DEPLOY_HOST` (e.g. `example.com`)
- `DEPLOY_USER` (e.g. `ubuntu`)
- `DEPLOY_SSH_KEY` (private key, e.g. ed25519)
- `GHCR_READ_TOKEN` (a PAT with **read:packages** for pulling from GHCR on the server)
- Optional: `DEPLOY_PORT` (defaults to `22`)

The deploy job restarts a container named `containerized-app` on the target host.

## Repo layout note

GitHub only runs workflows from the repository root. If this folder is not your repo root, move `.github/workflows/*` to your repo root and update the workflow `working-directory` / `docker build` paths accordingly.

