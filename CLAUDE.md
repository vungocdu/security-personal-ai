# CLAUDE.md

## Deployment

- Deploy target: Vercel
- Deployable service in this repository: `backend`
- Vercel root directory: `backend`
- Runtime entrypoint: `backend/api/index.py`
- Health endpoint: `/health`
- OpenAPI endpoint: `/openapi.json`

## Local Commands

Run backend locally:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Verify backend:

```bash
curl http://127.0.0.1:8000/health
```

## CI

- GitHub Actions workflow: `.github/workflows/ci.yml`
- Backend smoke check: `python -c "from app.main import app; print(app.title)"`
- OpenAPI validation: parse `doc/02-Architecture/API/openapi.yaml`
