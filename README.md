# Pharmacy Inventory Management System

A modular Flask web application implementing the core of the supplied Pharmacy Inventory Management PRD. It is designed as an educational project so the architecture remains understandable and maintainable.

## Features implemented

- Secure password hashing and login/logout
- Role field on users
- Medicine and category management
- Supplier management
- Batch-level stock, expiry and pricing
- Purchase recording
- Sales recording with stock validation
- Stock movement ledger
- Low-stock and expiry alerts
- Dashboard KPIs
- Inventory CSV report
- English, Hindi and Bengali navigation translations
- Provider-independent AI manager with a local rules/analytics provider
- SQLite for development and PostgreSQL configuration for production
- Pytest foundation and Docker support

## Run on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

Open `http://127.0.0.1:5000`. Demo login: `admin` / `admin123`.

Health check: `http://127.0.0.1:5000/health`.

## Docker

```bash
docker compose up --build
```

## Production

Use PostgreSQL, real secrets, HTTPS, backups, monitoring, a production WSGI server, and domain/security/compliance review before real pharmacy use.

## Important

This is an educational/demo implementation and is not a certified pharmacy management product.
