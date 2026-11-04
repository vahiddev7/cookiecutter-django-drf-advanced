# Quick start

This guide generates a new Django project from the Cookiecutter template.

## 1. Install Cookiecutter

Use an isolated Python environment where practical, then install Cookiecutter:

```bash
python -m pip install --upgrade cookiecutter
```

## 2. Generate a project

Run:

```bash
cookiecutter https://github.com/vahiddev7/cookiecutter-django-drf-advanced
```

Cookiecutter prompts for the project name and optional integrations. Answer the prompts to generate a new project directory.

For repeatable generation, pin to a published tag:

```bash
cookiecutter https://github.com/vahiddev7/cookiecutter-django-drf-advanced --checkout v0.1.0
```

Do not use a version tag until it exists on the repository's Releases page.

## 3. Configure environment variables

The generated project includes an `.env.example`. Review it and create the local environment file expected by the generated configuration. Set database credentials, service URLs, Django secret values, and any provider-specific settings.

Never commit real credentials or production secrets.

## 4. Start the project

If Docker was enabled during generation:

```bash
docker compose up --build
```

If Docker was not selected, install the generated development dependencies and follow the local setup commands included in the generated project.

## 5. Create an application

The generated project includes an app-generation script. For example:

```bash
./scripts/start_app.sh blog
```

Review the generated application and keep only the modules needed for its responsibilities.

## Next steps

Read the [configuration reference](../configuration/options.md), review the [architecture overview](../architecture/overview.md), and establish a [testing strategy](../development/testing.md) before adding substantial application behavior.
