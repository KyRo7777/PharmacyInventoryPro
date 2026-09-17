PharmacyInventoryPro 🏥💊An intelligent, multilingual Pharmacy Inventory Management System built with Python. This application integrates AI-powered analytics, localized healthcare data management, and comprehensive inventory tracking to streamline clinical pharmacy operations.🚀 Key Features🌍 Full Multilingual Support (Localization)Designed to be accessible in diverse regional clinical environments, the system features complete UI and medical terminology translation across three languages:English (en.json) - Default global interface.Hindi (hi.json) - Widespread regional accessibility.Bengali (bn.json) - Specialized regional clinical support (Highly relevant for localized medical AI datasets and training).🤖 AI-Powered Clinical IntelligenceSmart Analytics (ai.py): Integrates generative AI to analyze inventory trends and provide actionable predictions.Automated Structuring: Helps in structuring raw medical and inventory data into readable, standardized formats.Intelligent Reporting: Generates insights based on purchase history and batch expiration rates.📦 Advanced Inventory & Batch TrackingMedicine Cataloging: Categorize drugs by therapeutic class and supplier.Batch & Expiry Management: Track individual batches (batch_form.html) to prevent the dispensation of expired medications and reduce revenue leakage.Supplier Tracking: Manage distributor relationships and track inbound purchase orders.📊 Interactive Clinical DashboardReal-time Metrics (analytics.py): Monitor daily sales, active inventory, and critical stock alerts.Visual Data: Clean, responsive UI for clinical staff to quickly assess pharmacy health.🛠️ Tech Stack & ArchitectureBackend: Python (Flask web framework)Database: SQLite (pharmacy.db) / SQLAlchemy ORMFrontend: HTML5, CSS3, Vanilla JavaScript, Jinja2 TemplatingAI Integration: Custom AI processing pipelines and analytics engineDeployment: Docker & Docker Compose containerization📂 Project Structure OverviewPharmacyInventoryPro/
├── app/
│   ├── models/          # Database schemas (User, Catalog, Transaction)
│   ├── routes/          # API endpoints and view controllers (Sales, AI, Batches)
│   ├── services/        # Core business logic (AI, Analytics, Inventory, Localization)
│   ├── templates/       # Jinja2 HTML templates for the dashboard and forms
│   └── translations/    # Localization files (en.json, hi.json, bn.json)
├── docs/                # Comprehensive architecture and AI handoff documentation
├── tests/               # Automated testing suite (pytest)
├── docker-compose.yml   # Container orchestration
├── Dockerfile           # Application container image definition
├── requirements.txt     # Python dependencies
└── run.py               # Main application entry point
⚙️ Local Setup & InstallationOption 1: Using Docker (Recommended)The easiest way to run the application is using Docker, which handles all dependencies automatically.Ensure Docker Desktop is installed and running.Clone the repository:git clone https://github.com/YourUsername/PharmacyInventoryPro.git
cd PharmacyInventoryPro
Build and spin up the containers:docker-compose up --build
Access the application at http://localhost:5000 in your browser.Option 2: Standard Python EnvironmentClone the repository and navigate to the directory.Create and activate a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:pip install -r requirements.txt
Configure environment variables (Copy .env.example to .env and add your keys).Run the application:python run.py
🏥 Clinical & AI RelevanceThis project was developed with a strict focus on structured healthcare data, medical terminology localization, and operational accuracy. It serves as a practical demonstration of integrating AI and Data Science into HealthTech, specifically aligning with standards for medical data annotation, clinical scenario structuring, and bilingual (Bengali/English) patient-provider software solutions.
