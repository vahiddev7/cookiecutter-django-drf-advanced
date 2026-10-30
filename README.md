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

* 🧱 Modular architecture with optional service and selector layers
* 🔄 Scalable modular apps
* 🧪 Built-in testing structure
* ⚙️ Environment-based settings
* 🐳 Docker-ready
* 🔌 API-ready Django REST Framework foundation

---

## 🧠 Architecture (Opinionated)

```
Command: Request → View → Serializer → Service → Model/ORM → DB
Query:   Request → View → Selector → ORM → DB
```

### 🔹 Views

Thin layer (just HTTP handling)

### 🔹 Services

Optional application logic for commands and write operations

### 🔹 Selectors

Optional reusable read queries; use them when query logic deserves a name or reuse

### 🔹 Models

Django models define persisted data, relationships, and model-level behavior

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
  authentication/
    serializers/
    services/
    views/
    tests/
  users/
    models/
    migrations/
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
  apps.py
  admin.py
  urls.py
  models/
  migrations/
  tests/
    unit/
    integration/
    e2e/
```

The script creates only the Django app essentials and test-scope folders. Add `services/`, `selectors/`, `serializers/`, `permissions/`, or `views/` when the app actually needs them; they are conventions, not mandatory layers. The script also registers `apps.<app_name>` in `INSTALLED_APPS` and includes its URL module under `/api/<app_name>/`. Add endpoint patterns to `apps/<app_name>/urls.py`, then define models and run migrations as needed.

---

## 🔐 Authentication Included

When `use_drf=y`, the generated project exposes these endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/api/auth/register/` | Create an account with username, email, and password |
| `POST` | `/api/auth/login/` | Obtain a JWT access/refresh token pair |
| `POST` | `/api/auth/token/` | Backwards-compatible alias for JWT token obtain |
| `POST` | `/api/auth/token/refresh/` | Refresh an access token |

Registration requires a unique email address (case-insensitive) and a username. Email addresses are trimmed and stored in lowercase. Passwords are validated with Django's configured password validators; the password is write-only and is never included in the response. Login accepts the username/password fields expected by SimpleJWT.

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

Each app keeps its own tests in `apps/<app_name>/tests/`, organized by test scope:

* `unit/`
* `integration/`
* `e2e/`

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


### Production HTTPS and browser security

The production settings enable secure session and CSRF cookies, MIME-sniffing protection, clickjacking protection, and a restrictive referrer policy. Serve the application exclusively over HTTPS in production.

HTTPS redirect and HSTS are explicit deployment choices:

- Set `SECURE_SSL_REDIRECT=True` only after HTTPS is configured and every request reaching Django is correctly recognized as HTTPS.
- If TLS terminates at a trusted reverse proxy or load balancer, set `TRUST_PROXY_SSL_HEADER=True` only when that proxy **overwrites** the `X-Forwarded-Proto` header before forwarding requests. Never trust this header from arbitrary clients.
- Set `SECURE_HSTS_SECONDS` to a positive value only after HTTPS works reliably. Increase it gradually; enable subdomains or preload only when every affected hostname supports HTTPS.

The defaults keep redirect and HSTS disabled to avoid redirect loops or accidentally locking a domain into HTTPS before its infrastructure is ready. The secure-cookie defaults still require HTTPS for normal production browser sessions.


### CORS and CSRF trusted origins

Cross-origin browser access is disabled by default. If a separate frontend needs browser access to the API, set `CORS_ALLOWED_ORIGINS` to an explicit comma-separated list of full origins, including the scheme and port where applicable (for example, `https://frontend.example.com`). Do not use `*` as a production shortcut.

`CSRF_TRUSTED_ORIGINS` is a separate Django setting. Configure it only when a trusted frontend needs to submit cookie/session-authenticated unsafe requests across origins; list full origins including `https://`. CORS permission does not grant CSRF trust, and CSRF trust does not grant CORS access.

Keep `CORS_ALLOW_CREDENTIALS=False` unless the browser must send cookies or other credentials cross-origin. When credentials are enabled, continue using explicit origins and normal CSRF protections.


### Shared cache and API throttling

The default Django cache uses the database-backed cache table `django_cache`, created by the core app's initial migration. This gives all Gunicorn workers a shared cache and keeps DRF's built-in login and registration throttling counters consistent across processes without requiring Redis.

Database-backed caching is a practical default for a starter project and low-to-moderate traffic. For higher-throughput deployments, replace the cache backend with a shared Redis service and install the Redis Python client; do not switch to per-process `LocMemCache` when relying on throttling across multiple workers.

### Default API permissions

When Django REST Framework is enabled, API views require an authenticated user by default through `IsAuthenticated`. This is a secure baseline for new endpoints: explicitly use `AllowAny` only for intentionally public views.

The built-in registration, login, and JWT refresh endpoints are explicitly public because they must be reachable before a user has an access token. Keep authorization decisions close to each view and add object-level permissions where users must only access their own resources.
