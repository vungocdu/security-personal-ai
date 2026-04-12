# Security Personal AI

Query-first RAG MVP for securities research document intelligence.

## Current Scope

- Architecture baseline: [AD-SPAI-2026-001](./doc/02-Architecture/AD/AD-SPAI-2026-001-Architecture_Design.md)
- API source of truth: [openapi.yaml](./doc/02-Architecture/API/openapi.yaml)
- Backend MVP skeleton: [`backend/`](./backend)

## Run FastAPI locally

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

OpenAPI JSON:

```bash
curl http://127.0.0.1:8000/openapi.json
```

## Vercel deployment target

This repo is configured so Vercel can deploy the backend from [`backend/`](./backend).

```bash
cd backend
vercel
```

Recommended Vercel project settings:

- Framework preset: `Other`
- Root directory: `backend`
- Runtime entrypoint: `backend/api/index.py`
- Production health check: `/health`

## GitHub Actions baseline

CI workflow lives at [`.github/workflows/ci.yml`](./.github/workflows/ci.yml).

It validates two things only:

- FastAPI backend installs and imports cleanly
- `openapi.yaml` parses successfully

## GitHub SSH setup

This repo is intended to use the local key:

```bash
~/.ssh/id_ed25519_github_timesheet
```

After the GitHub repository exists, add the SSH remote:

```bash
git remote add origin git@github.com:<owner>/<repo>.git
git push -u origin main
```
