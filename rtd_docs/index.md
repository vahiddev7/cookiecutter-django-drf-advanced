# Django DRF Advanced Cookiecutter

A configurable **Django Cookiecutter template** for generating maintainable Python backend projects with optional Django REST Framework (DRF), Docker, Celery, multiple database backends, and cloud object storage.

Use this template when you want a repeatable foundation for Django applications and REST APIs without rebuilding the same project structure and infrastructure configuration for every service.

## What the template provides

- Django settings separated by environment.
- Optional Django REST Framework integration and API authentication.
- Optional Docker Compose development environment.
- Configurable PostgreSQL, MySQL, SQLite, or SQL Server database.
- Optional Celery with Redis or RabbitMQ, plus Flower monitoring.
- Optional Sentry error monitoring.
- Optional object storage integrations: AWS S3, Silo (S3-compatible), Google Cloud Storage, and Azure Blob Storage.
- Per-application test organization.
- Scripts and configuration intended to reduce repetitive project setup.

## Generate a project

```bash
python -m pip install --upgrade cookiecutter
cookiecutter https://github.com/vahiddev7/cookiecutter-django-drf-advanced
```

For reproducible generation, use a published release tag:

```bash
cookiecutter https://github.com/vahiddev7/cookiecutter-django-drf-advanced --checkout v0.1.0
```

Use a tag only after it has been published in the repository's [Releases](https://github.com/vahiddev7/cookiecutter-django-drf-advanced/releases).

## Documentation

- [Quick start](getting-started/quickstart.md)
- [Configuration reference](configuration/options.md)
- [Architecture overview](architecture/overview.md)
- [Testing strategy](development/testing.md)
- [Django REST Framework best practices](development/drf-best-practices.md)
- [Production checklist](operations/production.md)

## Project links

- [GitHub repository](https://github.com/vahiddev7/cookiecutter-django-drf-advanced)
- [Issues and feature requests](https://github.com/vahiddev7/cookiecutter-django-drf-advanced/issues)
- [Releases](https://github.com/vahiddev7/cookiecutter-django-drf-advanced/releases)

This template is a starting point, not a substitute for reviewing generated settings, dependencies, and deployment security before production use.
