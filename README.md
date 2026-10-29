# 🚀 Django Clean Architecture Cookiecutter

<p align="center">
  <b>Production-ready Django template for scalable backend systems</b><br/>
  Built with clean architecture, best practices, and developer experience in mind.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.2-green.svg" />
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Docker-ready-blue.svg" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey.svg" />
</p>

---

## 🎬 Demo

> Coming soon (you can add a GIF here showing API usage or app generation)

---

## ✨ Why this template?

Most Django projects start simple… and become messy.

This template gives you a **solid foundation from day one**:

* 🧱 Clean Architecture (Service & Selector pattern)
* 🔄 Scalable modular apps
* 🧪 Built-in testing structure
* ⚙️ Environment-based settings
* 🐳 Docker-ready
* 🔌 API-first design with versioning

---

## 🧠 Architecture (Opinionated)

```
Request → View → Service → Selector → Model → DB
```

### 🔹 Views

Thin layer (just HTTP handling)

### 🔹 Services

Business logic & write operations

### 🔹 Selectors

Read-only queries

### 🔹 Models

Pure data layer

---

## 📊 Architecture Diagram

```
                ┌──────────────┐
                │    Client    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │     View     │
                └──────┬───────┘
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
┌──────────────┐              ┌──────────────┐
│   Service    │              │   Selector   │
│ (write logic)│              │ (read logic) │
└──────┬───────┘              └──────┬───────┘
       │                             │
       └──────────────┬──────────────┘
                      ▼
               ┌──────────────┐
               │    Model     │
               └──────────────┘
                      │
                      ▼
               ┌──────────────┐
               │   Database   │
               └──────────────┘
```

---

## ⚡ Quick Start

### 1. Install Cookiecutter

```bash
pip install cookiecutter
```

### 2. Generate your project

```bash
cookiecutter https://github.com/vahiddev7/cookiecutter-django-drf-advanced
```

### 3. Run with Docker

```bash
docker compose up --build
```

---

## 📁 Project Structure

```
apps/
  users/
    models/
    services/
    selectors/
    serializers/
    views/
    tests/

config/
  settings/
    base.py
    dev.py
    prod.py
```

---

## 🧩 Create New App (🔥 Killer Feature)

```bash
./scripts/start_app.sh blog
```

Generates:

```
apps/blog/
  models/
  services/
  selectors/
  serializers/
  views/api/v1/
  tests/
```

---

## 🔐 Authentication Included

* Register
* Login
* Extendable token system

---

## ⚙️ Configuration

During setup:

```json
{
  "project_name": "My Project",
  "project_slug": "my_project",
  "use_drf": "y",
  "use_swagger": ["y", "n"],
  "use_docker": "y",
  "database_engine": ["postgresql", "mysql", "sqlite", "sqlserver"],
  "use_celery": ["y", "n"],
  "celery_broker": ["redis", "rabbitmq"]
}
```

---

## 🧪 Testing

```bash
pytest
```

Structure:

* API tests
* Service tests
* Selector tests

---

## 🐳 Docker

Includes:

* Dev environment
* Production setup
* Nginx config

---

## 🌍 Environment Settings

```
settings/
  base.py
  dev.py
  prod.py
```

---

## 💡 When to Use

✅ Large-scale backend systems
✅ Team projects
✅ Clean architecture lovers

---

## ⚠️ When NOT to Use

❌ Simple scripts
❌ Small MVPs

---

## 🧠 Philosophy

This template is **opinionated**.

It favors:

* long-term maintainability
* scalability
* clear separation of concerns

over quick-and-dirty setups.

---

## 🗺 Roadmap

* [ ] Add CI/CD pipeline
* [ ] Add GraphQL option
* [ ] Add lightweight mode
* [ ] Add project CLI

---

## 🤝 Contributing

PRs, issues, and ideas are welcome.

---

## ⭐ Support

If this project helps you, give it a star ⭐
It helps others discover it.


### Per-app test layout

Every app owns its tests under `apps/<app_name>/tests/`. The app generator creates:

```text
tests/
  apis/
    unit_test/
    integration_test/
    e2e_test/
  models/
    unit_test/
    integration_test/
    e2e_test/
  permissions/
    unit_test/
    integration_test/
    e2e_test/
  selectors/
    unit_test/
    integration_test/
    e2e_test/
  serializers/
    unit_test/
    integration_test/
    e2e_test/
  services/
    unit_test/
    integration_test/
    e2e_test/
```

Use unit tests for isolated behavior, integration tests for interactions with the database or
other components, and end-to-end tests for complete request flows. Run tests from the
generated project root with `pytest`.
