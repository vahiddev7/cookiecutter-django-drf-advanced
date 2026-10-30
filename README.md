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

Cookiecutter creates a local `.env` from `.env.example` after generation and fills in a fresh Django `SECRET_KEY`. It never overwrites an existing `.env`. Before starting Docker, review the database values in `.env` for the selected database engine. The generated `.env` is ignored by Git and should not be committed.

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

The script also adds `apps.<app_name>` to `INSTALLED_APPS` and includes the app's URL module under `/api/<app_name>/`. Add endpoint patterns to `apps/<app_name>/urls.py`, then define models and run migrations as needed.

---

## 🔐 Authentication Included

When `use_drf=y`, the generated project exposes these endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/api/auth/register/` | Create an account with username, email, and password |
| `POST` | `/api/auth/login/` | Obtain a JWT access/refresh token pair |
| `POST` | `/api/auth/token/` | Backwards-compatible alias for JWT token obtain |
| `POST` | `/api/auth/token/refresh/` | Refresh an access token |

Registration validates passwords with Django's configured password validators. The password is write-only and is never included in the response. Login accepts the username/password fields expected by SimpleJWT.

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

Each app owns its tests under `apps/<app_name>/tests/`, grouped by test scope:

```text
tests/
  unit/
  integration/
  e2e/
```

- **Unit:** test a small piece of behavior in isolation.
- **Integration:** test interactions between components, such as database queries and services.
- **E2E:** test complete user-facing flows through the application.

Keep tests close to the app they cover. Create test files and subpackages only when they are needed; the app generator creates the three scope directories without pre-populating empty categories. Run the suite from the generated project root with `pytest`.



### Docker Compose network exposure and HTTPS

The production Compose template publishes only Nginx on host port `80`. The application, database, and Celery broker services communicate over the private Compose network; their ports are not published directly to the host. This avoids exposing database listeners, Gunicorn, or the RabbitMQ management UI on every host interface by default.

For production deployments, terminate HTTPS at a trusted reverse proxy or load balancer and forward traffic to Nginx. Do not expose the HTTP endpoint publicly without an appropriate TLS-terminating layer. If you need to access a database or the RabbitMQ management UI from your own machine for development, use a separate local-only Compose override that binds the required port to `127.0.0.1`, and do not use that override in production.
