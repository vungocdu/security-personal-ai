# Security Personal AI

Query-first RAG MVP for securities research document intelligence.

## Current Scope

- Architecture baseline: [AD-SPAI-2026-001](./doc/02-Architecture/AD/AD-SPAI-2026-001-Architecture_Design.md)
- API source of truth: [openapi.yaml](./doc/02-Architecture/API/openapi.yaml)
- Backend MVP skeleton: [`backend/`](./backend)
- Frontend MVP analyst workspace: [`frontend/`](./frontend)

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

Run backend tests:

```bash
cd backend
source .venv/bin/activate
pytest -q
```

## Qdrant connectivity check

Configure backend environment:

```bash
cd backend
cp .env.example .env.local
```

Set `QDRANT_URL` and `QDRANT_API_KEY` in `backend/.env.local`, then run:

```bash
cd backend
source .venv/bin/activate
python scripts/check_qdrant_connection.py
```

Expected output:

```text
collection_count=<number>
collections=[...]
```

Run an end-to-end seed + search smoke test:

```bash
cd backend
source .venv/bin/activate
python scripts/seed_and_test_qdrant.py
```

Optional env for smoke script:

- `QDRANT_TEST_COLLECTION` to force a collection name (default auto timestamp)
- `QDRANT_TEST_KEEP_COLLECTION=true` to keep the seeded collection after test

## Run Next.js frontend locally

```bash
cd frontend
npm install --cache .npm-cache
npm run dev
```

The frontend defaults to fixture mode. To connect to the FastAPI backend:

```bash
export NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

Frontend quality gates:

```bash
cd frontend
npm run lint
npm test
npm run build
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

- FastAPI backend installs, imports, and passes unit tests
- `openapi.yaml` parses successfully
- Next.js frontend lint, test, and build all pass

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
