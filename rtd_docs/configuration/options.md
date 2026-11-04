# Configuration reference

The Cookiecutter prompts let you select the capabilities needed by the generated project. Exact prompts and generated files are defined by the template's `cookiecutter.json` and template directory.

## Django REST Framework

DRF is optional. When enabled, the generated project includes the API foundation and related configuration. The authentication application is generated only when DRF is enabled.

Enable only the API and authentication features the project actually needs. Review default permissions and authentication behavior before exposing endpoints.

## Database

The template supports selecting a database backend, including:

- PostgreSQL
- MySQL
- SQLite
- SQL Server

Configure the corresponding environment variables and install the dependencies required by the selected backend. Validate migrations and database-specific behavior against the same engine used in production.

## Docker

Docker support provides a container-based development environment. Inspect the generated Compose file and environment variables before starting services. Keep database and broker ports private unless external access is explicitly required.

## Celery and brokers

Celery can be enabled with Redis or RabbitMQ as the broker. When enabled, the development Compose configuration also includes Flower for task monitoring.

Flower is an operational interface, not a public-facing application endpoint. Keep it access-controlled and do not expose it directly to the internet without an authenticated HTTPS reverse proxy.

## Logging and Sentry

Console logging is configured in the generated project and can be adjusted through the environment.

Sentry is optional. When enabled, configure the DSN and environment-specific sampling settings through environment variables. Keep personally identifiable information disabled unless there is a reviewed requirement to collect it. When Sentry is disabled during generation, its optional settings module is omitted.

## Object storage

The template supports local filesystem storage and optional cloud/object-storage integrations:

| Option | Intended use |
| --- | --- |
| Local filesystem | Development or deployments that intentionally use local persistent storage |
| AWS S3 | Managed S3 object storage |
| Silo | Self-hosted S3-compatible development or deployment |
| Google Cloud Storage | Google Cloud object storage |
| Azure Blob Storage | Microsoft Azure object storage |

Provider credentials must be supplied through environment variables, workload identity, or a secret manager. Do not commit credentials. Configure bucket/container permissions, CORS, TLS, and public/private access policy deliberately.

Silo is a community-maintained S3-compatible service and is not an official MinIO product.

## Generated files

Optional features may add or omit settings modules, dependencies, services, and application code. After generation, inspect the resulting project rather than assuming every optional component exists.
