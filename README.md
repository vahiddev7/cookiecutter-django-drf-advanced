# Django DRF Advanced Cookiecutter

A production-oriented, configurable project template for building maintainable Django backend applications. It provides a consistent starting point for project configuration, optional Django REST Framework support, Docker-based development, testing, and a modular application structure.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-supported-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Cookiecutter](https://img.shields.io/badge/Cookiecutter-template-d4aa00)](https://cookiecutter.readthedocs.io/)

[**Read the documentation website**](https://vahiddev7.github.io/cookiecutter-django-drf-advanced/) · [Quick start](https://vahiddev7.github.io/cookiecutter-django-drf-advanced/quickstart.html) · [Architecture](https://vahiddev7.github.io/cookiecutter-django-drf-advanced/architecture.html)

## Why this template?

Starting a backend project involves repeatedly making the same foundational decisions. This template packages those decisions into a configurable scaffold, so a team can spend more time on product behavior and less time on setup.

The template emphasizes:

- **Modularity:** keep Django applications organized around clear responsibilities.
- **Optional layers:** add services and selectors when they provide real value; avoid empty architectural placeholders.
- **Configurable foundations:** choose database, API, documentation, Docker, and task-queue options during generation.
- **Testability:** organize tests by scope inside each application.
- **Operational awareness:** provide environment-based settings and container configuration as a starting point.

## Features

- Django project scaffold with separated base, development, and production settings.
- Optional Django REST Framework integration.
- Optional API documentation configuration.
- Configurable database selection: PostgreSQL, MySQL, SQLite, or SQL Server.
- Optional Docker setup.
- Optional Celery integration with Redis or RabbitMQ as the broker.
- App-generation script that creates and registers a new Django application.
- Per-app test layout for unit, integration, and end-to-end tests.
- Optional authentication app when DRF is enabled.

## Quick start

### 1. Install Cookiecutter

```bash
python -m pip install --upgrade cookiecutter
```

### 2. Generate a project

```bash
cookiecutter https://github.com/vahiddev7/cookiecutter-django-drf-advanced
```

Cookiecutter asks for the project name and the options described below. It then creates a new project directory using your answers.

### 3. Configure environment variables

The generated project includes an `.env.example`. The post-generation hook creates a local `.env` file and generates a Django secret key when appropriate. Review the generated values—especially database credentials and service URLs—before starting the application.

Do not commit your real `.env` file or production secrets.

### 4. Start the project

If you enabled Docker, run the command from the generated project directory:

```bash
docker compose up --build
```

For projects generated without Docker, install the development dependencies and follow the generated project's settings and application entry points.

## Configuration options

The Cookiecutter prompts let you tailor the generated project:

| Option | Choices / behavior |
| --- | --- |
| Django REST Framework | Enable or disable DRF |
| API documentation | Select whether to include the configured Swagger/OpenAPI support |
| Docker | Enable or disable the Docker setup |
| Database | PostgreSQL, MySQL, SQLite, or SQL Server |
| Celery | Enable or disable background task processing |
| Celery broker | Redis or RabbitMQ, when Celery is enabled |

The authentication application is generated only when DRF is enabled. Optional features should be selected based on the requirements of the project being generated.

## Architecture

The template encourages a clear separation between HTTP handling, application behavior, and data access without forcing every layer into every app.

### Command / write flow

```text
Request -> View -> Serializer -> Service -> Model / ORM -> Database
```

### Query / read flow

```text
Request -> View -> Selector -> ORM -> Database
```

- **Views** handle HTTP concerns and coordinate the request/response lifecycle.
- **Serializers** validate and represent API data when DRF is enabled.
- **Services** hold application or business operations when the logic benefits from being separated from the view.
- **Selectors** encapsulate reusable or sufficiently complex read queries.
- **Models** represent persisted domain data and Django ORM behavior.

Services and selectors are conventions, not mandatory layers. Keep simple behavior simple; introduce an abstraction when it improves clarity, reuse, or testability.

## Generated project structure

The exact structure depends on the selected options. A typical generated project follows this general layout:

```text
.
├── apps/
│   ├── users/
│   └── authentication/       # generated when DRF is enabled
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   └── ...
├── docker/
├── requirements/
├── scripts/
├── .env.example
├── docker-compose.yml
└── manage.py
```

Treat this as an overview rather than a promise that every optional directory exists in every generated configuration.

## Create a new Django app

Generated projects include an app-generation script:

```bash
./scripts/start_app.sh blog
```

The script creates the Django app essentials, registers the app in `INSTALLED_APPS`, and includes its URL module under the API routing structure. Add models, endpoints, migrations, and any additional modules required by the app.

Create `services/`, `selectors/`, `serializers/`, `permissions/`, or `views/` only when the app needs them. These modules are not required just to satisfy a directory convention.

## Authentication

When DRF is enabled, the generated authentication app provides the configured registration and JWT authentication endpoints. The current scaffold includes:

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `POST` | `/api/auth/register/` | Register an account |
| `POST` | `/api/auth/login/` | Obtain an access/refresh token pair |
| `POST` | `/api/auth/token/` | Token-obtain compatibility endpoint |
| `POST` | `/api/auth/token/refresh/` | Refresh an access token |

Registration validates the submitted account data and password using the generated Django configuration. Review the generated authentication settings and permissions before exposing an application publicly.

## Testing

Tests live inside the application they cover and are grouped by scope:

```text
apps/
└── example/
    └── tests/
        ├── unit/
        ├── integration/
        └── e2e/
```

- **Unit tests** check focused behavior in isolation.
- **Integration tests** check interactions between components, such as services and database access.
- **End-to-end tests** exercise complete user-facing flows.

Run the test suite from the generated project root:

```bash
pytest
```

The available test configuration and dependencies depend on the selected project options.

## Dependency management

The generated project provides pip requirements and Poetry configuration. Use the development dependency set while working locally and the production dependency set for deployment. When changing dependencies or optional features, keep the pip and Poetry declarations consistent.

## Deployment and security notes

This template is a starting point, not a substitute for a deployment security review.

- Store secrets in environment variables or a dedicated secret manager; never commit credentials.
- Use HTTPS in production and configure trusted proxy headers only when the reverse proxy overwrites them.
- Keep database and message-broker ports private; expose only the services that must be reachable.
- Configure CORS and CSRF trusted origins explicitly for the frontend origins you operate.
- Review default API permissions, authentication settings, allowed hosts, cookie settings, and throttling before deployment.
- Apply migrations and test the selected database backend in an environment representative of production.

Some database backends have different capabilities and may require different authentication or migration behavior. Verify the generated settings for the database option you choose.

## Contributing

Issues, bug reports, and focused pull requests are welcome.

When proposing a change:

1. Explain the problem and the expected behavior.
2. Keep optional feature combinations working.
3. Add or update tests for changed behavior.
4. Update the documentation when prompts, generated files, or setup steps change.

## Roadmap

Potential areas for future improvement include:

- More example projects generated from different option combinations.
- Expanded deployment and observability documentation.
- Additional integration coverage for optional feature combinations.
- A first stable tagged release with a documented compatibility matrix.

## License

This repository currently does not contain a license file. Until a license is added, the project should not be assumed to grant permission to reuse, modify, or redistribute its contents. A license should be selected and added explicitly by the repository owner.

---

If this template is useful, consider starring the repository and sharing feedback through GitHub Issues.

**Repository:** [vahiddev7/cookiecutter-django-drf-advanced](https://github.com/vahiddev7/cookiecutter-django-drf-advanced)
