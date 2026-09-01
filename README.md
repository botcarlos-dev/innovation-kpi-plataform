# Innovation KPI Platform

A full-stack web application for monitoring, calculating, and reporting Key Performance Indicators (KPIs) for innovation projects.

The platform provides automated KPI calculation, threshold-based status evaluation, alert generation, and a web dashboard for analysing project and KPI performance.

> **Project Status: Incomplete / Work in Progress**
>
> The core backend functionality and initial frontend dashboard are implemented and functional. Some planned features, visual improvements, and production-readiness work remain unfinished.

---

## Overview

Innovation teams often rely on manually maintained spreadsheets and reports to monitor project performance.

This project explores how KPI monitoring and reporting can be automated through a centralized platform capable of:

* Managing innovation projects
* Defining and maintaining KPIs
* Automatically calculating KPI measurements
* Evaluating KPI health against configurable thresholds
* Detecting warning and critical conditions
* Generating alerts
* Providing project-level performance analysis
* Visualizing KPI trends and historical measurements

The project was designed with an emphasis on **automation, maintainability, and separation of responsibilities** between the backend, business logic, and frontend.

---

## Architecture

```text
                    ┌─────────────────────┐
                    │      React UI       │
                    │                     │
                    │ Dashboard           │
                    │ Projects            │
                    │ KPIs                │
                    │ Measurements        │
                    │ Alerts              │
                    │ Project Performance │
                    └──────────┬──────────┘
                               │
                              HTTP
                               │
                    ┌──────────▼──────────┐
                    │      FastAPI        │
                    │       API           │
                    ├─────────────────────┤
                    │ Projects API        │
                    │ KPIs API            │
                    │ Measurements API    │
                    │ Financial Records   │
                    │ Alerts API          │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Service Layer     │
                    ├─────────────────────┤
                    │ KPI Engine          │
                    │ Measurement Service │
                    │ Alert Service       │
                    │ Business Logic      │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │     Database        │
                    │                     │
                    │ Projects            │
                    │ KPIs                │
                    │ Measurements        │
                    │ Alerts              │
                    │ Financial Records   │
                    └─────────────────────┘
```

---

## Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* Pytest

### Frontend

* React
* JavaScript
* Vite
* Axios
* Recharts

### Development

* Git
* Linux
* REST APIs
* Automated testing

---

## Core Features

### KPI Engine

The backend contains a dedicated KPI calculation engine supporting multiple KPI formula types.

Current examples include:

* Budget Variance
* Project Progress
* Innovation ROI
* Forecast Accuracy
* Schedule Variance

The calculation logic is separated from the API layer, allowing KPI calculations to be tested independently.

---

### KPI Status Evaluation

KPI measurements are automatically classified according to configurable thresholds.

Possible states include:

```text
HEALTHY
WARNING
CRITICAL
```

The evaluation takes into consideration whether a KPI is configured as **higher-is-better** or **lower-is-better**.

---

### Automated Alerts

Warning and critical measurements can automatically generate alerts.

The alert service also prevents duplicate alerts for the same measurement.

Example:

```text
KPI: Budget Variance
Value: 16.67%
Status: CRITICAL

Alert:
Budget Variance - CRITICAL
```

---

### Project Performance

The frontend provides project-level analysis including:

* Project selection
* Number of measurements
* Number of tracked KPIs
* Project alerts
* Latest KPI measurements
* KPI status
* Historical KPI trends

---

### KPI Trend Visualization

Historical KPI measurements can be visualized through interactive charts.

The interface displays:

* Historical KPI values
* Target value
* Warning threshold
* Critical threshold
* Measurement dates

This allows users to identify performance deterioration or improvement over time.

---

## API

The backend exposes REST endpoints for the main platform resources.

Examples:

```text
GET  /projects/
GET  /kpis/
GET  /kpi-measurements/
GET  /alerts/

POST /projects/
POST /kpis/
POST /kpi-measurements/
```

Additional endpoints are available for financial records and KPI calculations.

FastAPI automatically provides interactive API documentation.

When running locally:

```text
http://127.0.0.1:8000/docs
```

---

## Testing

The project includes automated tests covering core business logic.

Examples include:

* KPI calculations
* KPI status evaluation
* Budget variance calculation
* Project progress calculation
* ROI calculation
* Forecast accuracy
* Alert creation
* Duplicate alert prevention

Run the backend tests with:

```bash
pytest
```

---

## Running the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create and activate the virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## Running the Frontend

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

## Project Structure

```text
innovation-kpi-platform/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   └── tests/
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   │
│   └── package.json
│
└── README.md
```

---

## Current Project Status

### Implemented

* [x] FastAPI backend
* [x] Database models
* [x] Project management
* [x] KPI management
* [x] KPI calculation engine
* [x] KPI status evaluation
* [x] KPI measurements
* [x] Financial records
* [x] Budget variance calculation
* [x] Automated alert generation
* [x] Duplicate alert prevention
* [x] REST API
* [x] Automated backend tests
* [x] React frontend
* [x] Dashboard
* [x] Project performance page
* [x] KPI trend visualization
* [x] Backend/frontend integration
* [x] CORS configuration

### Planned / Incomplete

* [ ] Authentication and authorization
* [ ] User and role management
* [ ] Advanced filtering
* [ ] Date-range analysis
* [ ] Advanced KPI analytics
* [ ] Historical trend analysis improvements
* [ ] Production deployment
* [ ] Containerization
* [ ] CI/CD pipeline
* [ ] Improved frontend UX/UI
* [ ] Additional reporting capabilities
* [ ] Production database configuration
* [ ] API security hardening

---

## Design Goals

The project was developed around several principles:

**Separation of concerns**

Business logic is kept inside dedicated services instead of being implemented directly inside API endpoints.

**Testability**

Core KPI calculations and alert logic are covered by automated tests.

**Automation**

The platform aims to reduce manual KPI monitoring and reporting by automatically calculating measurements, evaluating their status, and generating alerts.

**Extensibility**

The KPI engine and service-based architecture are designed so additional KPI types and business rules can be introduced without rewriting the entire application.

---

## Future Improvements

The next development phase would focus on transforming the current prototype into a production-ready platform.

Potential improvements include:

1. Authentication and RBAC
2. PostgreSQL production database
3. Docker-based deployment
4. CI/CD pipeline
5. Advanced analytics
6. Automated reporting
7. KPI forecasting
8. Notification integrations
9. Audit logging
10. Cloud deployment

---

## Disclaimer

This repository represents a **portfolio / development project** created to explore the architecture and implementation of an automated KPI monitoring and reporting platform.

The current implementation should be considered a functional prototype rather than a production-ready enterprise system.

