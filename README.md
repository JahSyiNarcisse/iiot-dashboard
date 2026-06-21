# IIOT Dashboard - FastAPI scaffold

Minimal FastAPI app with basic system endpoints.

Endpoints:

- `GET /health` — health status
- `GET /cpu` — CPU usage percent
- `GET /memory` — memory totals and usage
- `GET /disk` — disk totals and usage
- `GET /system` — platform and boot time
- `GET /network` — network I/O counters

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Built-in docs are available at `/docs` and `/redoc` when the app is running.
