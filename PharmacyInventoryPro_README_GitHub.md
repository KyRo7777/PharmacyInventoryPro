# Pharmacy Inventory Pro — Industry Edition

> A modular Flask-based pharmacy inventory management system with transactional inventory operations, batch-level stock tracking, analytics, multilingual support, a provider-independent AI assistant, Docker deployment, and automated tests.

## Overview

**Pharmacy Inventory Pro** is a full-stack web application designed around the operational workflow of a pharmacy:

- Manage medicines and categories
- Manage suppliers
- Track medicine batches
- Track expiry dates and stock quantities
- Record purchases and sales
- Maintain a stock-movement ledger
- Detect low-stock and expiry conditions
- Generate inventory reports
- Provide demand forecasting and reorder signals
- Support FEFO (First Expiry, First Out) dispatch prioritization
- Run a lightweight, explainable transaction anomaly detector
- Provide a what-if inventory simulator
- Generate a SHA-256 ledger fingerprint as an integrity signal
- Quarantine batches operationally
- Provide English, Hindi, and Bengali UI localization
- Provide a local, provider-independent AI assistant
- Run with SQLite for development or PostgreSQL for deployment
- Run locally or through Docker

The project is intentionally modular so that the transactional core can operate independently of the AI/intelligence layer.

---

## Key Highlights

### Core pharmacy operations

- Authentication with password hashing
- Medicine catalogue management
- Medicine categories
- Supplier management
- Batch-level inventory
- Purchase recording
- Sales recording
- Stock validation
- Expiry handling
- Stock movement history
- Inventory CSV export
- Dashboard KPIs

### Pharmacy Intelligence V2

The V2 intelligence layer adds read-only analytics and an operational batch action without requiring new database columns.

Implemented capabilities include:

1. **FEFO queue** — prioritizes eligible batches with the earliest expiry date.
2. **30-day demand forecast** — estimates demand from recorded sales history.
3. **Explainable reorder signal** — combines forecast demand, safety stock and current stock.
4. **What-if simulator** — tests demand changes and supplier lead-time assumptions.
5. **Transaction anomaly detection** — flags unusually large sales compared with the typical transaction quantity for the same medicine.
6. **Ledger fingerprint** — chains SHA-256 hashes of stock movements to provide an integrity signal.
7. **Batch quarantine** — deactivates a batch and records the quarantine action in the stock movement ledger.
8. **Multilingual AI assistant** — provides operational answers using the local analytics provider.
9. **Human-in-the-loop design** — analytics recommends; authorized staff perform operational actions.

> The ledger fingerprint is an integrity indicator. It is **not** a blockchain implementation and does not constitute regulatory certification.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ORM | Flask-SQLAlchemy / SQLAlchemy |
| Authentication | Flask-Login |
| Database | SQLite / PostgreSQL |
| Database migration support | Flask-Migrate |
| Frontend | HTML, CSS, Jinja2 |
| UI styling | Bootstrap-based templates + custom CSS |
| Client-side scripting | JavaScript |
| Analytics | Python-based rule/statistical calculations |
| AI layer | Provider-independent manager + local rules/analytics provider |
| Localization | JSON translation files |
| Testing | Pytest, pytest-flask |
| Production server | Gunicorn |
| Containerization | Docker, Docker Compose |
| Configuration | Environment variables + python-dotenv |

---

## Architecture

```text
                        ┌──────────────────────────┐
                        │       Web Browser        │
                        └────────────┬─────────────┘
                                     │
                                     ▼
                        ┌──────────────────────────┐
                        │     Flask Application     │
                        │     Application Factory   │
                        └────────────┬─────────────┘
                                     │
                 ┌───────────────────┼───────────────────┐
                 ▼                   ▼                   ▼
          ┌─────────────┐     ┌─────────────┐     ┌──────────────┐
          │   Routes /  │     │  Templates  │     │ Localization │
          │  Blueprints │     │   / Jinja   │     │ EN / HI / BN │
          └──────┬──────┘     └─────────────┘     └──────────────┘
                 │
                 ▼
          ┌─────────────────────────────┐
          │        Service Layer        │
          │                             │
          │ InventoryService            │
          │ PharmacyAnalytics            │
          │ AIManager / LocalProvider   │
          └────────────┬────────────────┘
                       │
                       ▼
          ┌─────────────────────────────┐
          │      SQLAlchemy Models      │
          │                             │
          │ Users / Medicines / Batches │
          │ Suppliers / Sales / Purch.  │
          │ Stock Movements              │
          └────────────┬────────────────┘
                       │
              ┌────────┴─────────┐
              ▼                  ▼
        ┌──────────┐       ┌────────────┐
        │  SQLite  │       │ PostgreSQL │
        └──────────┘       └────────────┘
```

### AI architecture

```text
Application
     │
     ▼
 AIManager
     │
     ▼
 Provider interface / adapter boundary
     │
     ├──────── LocalProvider
     │          └── Rules + Analytics
     │
     └──────── Future external provider
                └── API-based implementation
```

The current implementation uses the local provider. The configuration already exposes provider/model/API settings so the AI layer can be extended without coupling the core pharmacy operations directly to a specific AI vendor.

---

## Project Structure

```text
PharmacyInventoryPro/
│
├── app/
│   ├── __init__.py
│   ├── bootstrap.py
│   ├── extensions.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── catalog.py
│   │   └── transaction.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── medicines.py
│   │   ├── categories.py
│   │   ├── suppliers.py
│   │   ├── batches.py
│   │   ├── purchases.py
│   │   ├── sales.py
│   │   ├── reports.py
│   │   ├── ai.py
│   │   ├── intelligence.py
│   │   └── health.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── inventory.py
│   │   ├── analytics.py
│   │   ├── ai.py
│   │   └── localization.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── medicines.html
│   │   ├── medicine_form.html
│   │   ├── categories.html
│   │   ├── suppliers.html
│   │   ├── supplier_form.html
│   │   ├── batches.html
│   │   ├── batch_form.html
│   │   ├── purchases.html
│   │   ├── purchase_form.html
│   │   ├── sales.html
│   │   ├── sale_form.html
│   │   ├── reports.html
│   │   ├── intelligence.html
│   │   ├── ai.html
│   │   └── simple_form.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── app.css
│   │   └── js/
│   │       └── app.js
│   │
│   └── translations/
│       ├── en.json
│       ├── hi.json
│       └── bn.json
│
├── docs/
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── V2_FEATURES.md
│   ├── V2_README.md
│   ├── AI_HANDOFF.md
│   └── LEARNING_GUIDE.md
│
├── tests/
│   ├── conftest.py
│   └── test_basic.py
│
├── config.py
├── run.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── pharmacy.db
```

---

## Important Files

### `run.py`

Application entry point.

It creates the Flask application using the application factory and starts the development server when executed directly.

### `config.py`

Central configuration layer.

Controls:

- Flask secret key
- Database URL
- Expiry warning period
- Default locale
- AI enable/disable state
- AI provider
- AI model
- AI API key placeholder
- AI base URL
- AI request timeout

### `app/__init__.py`

Implements the Flask **application factory**.

It:

1. Creates the Flask application.
2. Loads configuration.
3. Initializes SQLAlchemy.
4. Initializes Flask-Migrate.
5. Initializes Flask-Login.
6. Imports models.
7. Registers application blueprints.
8. Registers translation context helpers.
9. Runs bootstrap initialization.

### `app/extensions.py`

Creates shared Flask extensions:

- SQLAlchemy
- Flask-Migrate
- Flask-Login

---

# Data Model

## User

Stores:

- username
- password hash
- role
- active status
- preferred locale

Passwords are hashed through Werkzeug rather than stored in plaintext.

## Category

Stores medicine categories and active status.

## Medicine

Stores:

- medicine name
- generic name
- manufacturer
- unit
- minimum stock threshold
- description
- category
- active status

`current_stock` is calculated from active batches.

## Supplier

Stores:

- supplier name
- contact person
- phone
- email
- address
- tax/business identifier
- status
- notes

## MedicineBatch

Stores:

- batch number
- expiry date
- purchase price
- selling price
- available quantity
- medicine relationship
- supplier relationship
- active/quarantine status

A unique constraint prevents duplicate batch numbers for the same medicine.

## Purchase / PurchaseItem

Purchases record incoming stock and supplier information.

A purchase item links a purchase to a specific batch and quantity.

## Sale / SaleItem

Sales record outgoing stock.

Before stock is removed:

- quantity must be positive
- the batch cannot be expired
- sufficient stock must exist

## StockMovement

The stock ledger records quantity changes and references the source transaction.

Movement records include:

- batch
- movement type
- quantity delta
- reference type
- reference ID
- note
- creating user

---

# Inventory Logic

The central inventory logic is implemented in `InventoryService`.

### Adding stock

```text
Purchase / Opening Stock
        │
        ▼
InventoryService.add()
        │
        ├── Increase batch quantity
        └── Create stock movement
```

### Removing stock

```text
Sale
 │
 ▼
InventoryService.remove()
 │
 ├── Validate positive quantity
 ├── Reject expired batch
 ├── Validate sufficient stock
 ├── Decrease batch quantity
 └── Create stock movement
```

This keeps inventory mutations in one service rather than duplicating the rules across multiple routes.

---

# Pharmacy Intelligence

## 1. Demand Forecasting

The analytics layer calculates a transparent 30-day demand estimate from recorded sales history.

The implementation:

1. Retrieves sales grouped by sale date.
2. Looks at recent sales history.
3. Calculates average daily demand.
4. Projects demand over 30 days.
5. Calculates safety stock.
6. Compares projected demand with current stock.
7. Produces a reorder quantity.
8. Assigns a stock-risk category based on stock coverage.

The calculation is intentionally transparent rather than a black-box ML prediction.

## 2. FEFO

FEFO means:

> **First Expiry, First Out**

The system identifies the active, non-expired batch with available stock and the earliest expiry date for each medicine.

This creates a dispatch-priority queue.

## 3. Anomaly Detection

The project includes a lightweight statistical rule rather than a black-box anomaly model.

For a medicine:

- transaction quantities are grouped
- the median quantity is calculated
- unusually large transactions are flagged when they are sufficiently above the typical quantity

The result includes the date, medicine, quantity, typical quantity and explanation.

## 4. What-If Simulator

The intelligence interface allows the user to vary:

- expected demand change percentage
- supplier lead time in days

The system then recalculates:

- projected monthly demand
- lead-time demand
- safety stock
- reorder quantity
- days of stock cover

This allows users to explore operational scenarios without changing the actual database.

## 5. Ledger Fingerprint

Every stock movement is serialized into a canonical representation and incorporated into a SHA-256 chain.

```text
GENESIS
   │
   ▼
Hash(Movement 1)
   │
   ▼
Hash(previous hash + Movement 2)
   │
   ▼
Hash(previous hash + Movement 3)
   │
   ▼
...
```

The application exposes a shortened fingerprint and movement count as an integrity signal.

---

# AI Assistant

The AI layer is intentionally separated from core pharmacy operations.

### Current provider

The included `LocalProvider` uses deterministic rules and analytics.

It can answer operational questions around:

- low stock
- expiry
- FEFO priority
- demand forecasting
- reorder suggestions
- general inventory summary

The assistant supports English, Hindi and Bengali responses.

### Provider independence

The core application interacts with `AIManager` rather than directly coupling business logic to an external AI SDK.

This makes it possible to implement an external provider later while keeping the transactional system independent.

### Important boundary

The current release does **not** ship with an external LLM integration. `AI_API_KEY`, `AI_BASE_URL`, `AI_PROVIDER`, `AI_MODEL` and timeout settings are configuration points for future provider integrations.

---

# Localization

Supported locales:

- English — `en`
- Hindi — `hi`
- Bengali — `bn`

Translation files are stored in:

```text
app/translations/
├── en.json
├── hi.json
└── bn.json
```

The localization system deliberately keeps domain data such as:

- medicine names
- batch numbers
- supplier names
- numeric values

unchanged.

Only UI labels and supported assistant responses are localized.

---

# Routes

| Route | Purpose |
|---|---|
| `/` | Dashboard |
| `/auth/login` | Login |
| `/auth/logout` | Logout |
| `/medicines/` | Medicine catalogue |
| `/categories/` | Categories |
| `/suppliers/` | Suppliers |
| `/batches/` | Batch inventory |
| `/purchases/` | Purchase management |
| `/sales/` | Sales management |
| `/reports/` | Reports |
| `/reports/inventory.csv` | CSV inventory export |
| `/intelligence/` | Pharmacy Intelligence V2 |
| `/ai/` | AI assistant |
| `/lang/<code>` | Change UI language |
| `/health` | Health check |

All major operational views require authentication.

---

# Running Locally

## 1. Clone

```bash
git clone <your-repository-url>
cd PharmacyInventoryPro
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment

Copy:

```text
.env.example
```

to:

```text
.env
```

Then update secrets/configuration as required.

## 5. Run

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

### Demo account

The bootstrap process creates:

```text
Username: admin
Password: admin123
```

Change/remove demo credentials before any real deployment.

### Health check

```text
http://127.0.0.1:5000/health
```

Expected response:

```json
{
  "status": "healthy",
  "service": "pharmacy-inventory-management-system"
}
```

---

# Docker

The repository includes both `Dockerfile` and `docker-compose.yml`.

Run:

```bash
docker compose up --build
```

The Compose configuration starts:

- Flask/Gunicorn web service
- PostgreSQL 16 database

The database is persisted through the `pharmacy_pgdata` Docker volume.

---

# Testing

The project includes a Pytest foundation.

Run:

```bash
pytest
```

The current tests verify:

- application creation
- health endpoint availability

The testing configuration uses an in-memory SQLite database.

---

# Environment Variables

Example:

```env
SECRET_KEY=change-me
DATABASE_URL=sqlite:///pharmacy.db
DEFAULT_LOCALE=en
EXPIRY_WARNING_DAYS=30

AI_ENABLED=true
AI_PROVIDER=local
AI_MODEL=rules-and-analytics
AI_API_KEY=
AI_BASE_URL=
AI_TIMEOUT=20
```

For production, use a strong secret and a production PostgreSQL database.

---

# Security and Production Notes

This repository is an **educational/demo implementation**, not a certified pharmacy product.

Before real-world deployment, additional work is required, including:

- CSRF protection
- stronger role-based authorization enforcement
- production secret management
- secure credential rotation
- database backups
- monitoring and logging
- HTTPS
- production WSGI configuration
- audit/compliance review
- data retention/privacy review
- invoice and return workflows
- notification integrations
- production AI provider integration
- broader automated test coverage

The current implementation should therefore be treated as a learning/demo system rather than software approved for real pharmacy operations.

---

# Learning Path

Recommended order for understanding the project:

```text
Flask fundamentals
        ↓
Application Factory
        ↓
Blueprints
        ↓
Jinja2 Templates
        ↓
SQLAlchemy ORM
        ↓
Database Relationships
        ↓
Authentication
        ↓
Service Layer
        ↓
Transactions
        ↓
Testing
        ↓
PostgreSQL
        ↓
AI Adapter / Provider Architecture
        ↓
Docker Deployment
```

---

# Project Documentation

Additional documentation is available under `docs/`:

| File | Purpose |
|---|---|
| `docs/ARCHITECTURE.md` | High-level architecture |
| `docs/API.md` | Routes/API surface |
| `docs/V2_FEATURES.md` | Intelligence V2 features |
| `docs/V2_README.md` | V2 usage notes |
| `docs/AI_HANDOFF.md` | Current implementation and production gaps |
| `docs/LEARNING_GUIDE.md` | Suggested learning sequence |

A separate file, `PROJECT_DOCUMENTATION.md`, provides a more detailed file-by-file technical explanation.

---

# Current Scope

### Implemented

- Authentication
- Medicine management
- Categories
- Suppliers
- Batch inventory
- Purchases
- Sales
- Stock movement ledger
- Low-stock detection
- Expiry alerts
- Dashboard
- CSV inventory report
- English/Hindi/Bengali localization
- FEFO
- Demand forecasting
- Reorder signals
- What-if analysis
- Explainable transaction anomaly detection
- SHA-256 ledger fingerprint
- Batch quarantine
- Local AI assistant
- Pytest foundation
- SQLite/PostgreSQL configuration
- Docker support

### Planned / Future Extensions

- External AI provider adapters
- PDF invoices
- Returns and refunds
- Notification services
- Advanced RBAC
- More comprehensive tests
- Production audit logging
- Advanced forecasting models
- Barcode/QR workflows
- Deployment automation
- Operational monitoring
- Compliance review

---

## License

Add the license appropriate to your intended GitHub distribution before publishing the repository.

## Disclaimer

This project is intended for educational, demonstration, and software-engineering purposes. It is not a certified pharmacy management, medical decision-support, or regulatory-compliance product.
