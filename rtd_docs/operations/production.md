# Production checklist

The generated project is a starting point. Review these areas before deploying it.

## Configuration and secrets

- Set a unique, secret `SECRET_KEY` using a secret manager or secure environment injection.
- Set `DEBUG=False` and configure `ALLOWED_HOSTS` explicitly.
- Keep production credentials out of source control, images, and logs.
- Use separate credentials for application, database, broker, and object storage access.

## Network and transport

- Serve public traffic over HTTPS.
- Keep database, cache, and message-broker ports on private networks.
- Configure trusted proxy headers only when the reverse proxy overwrites them safely.
- Set CORS and CSRF trusted origins to the exact origins that require access.

## Database and background work

- Test migrations against the production database engine.
- Back up persistent data and periodically test restoration.
- Configure Celery worker concurrency, retries, timeouts, and monitoring for the workload.
- Restrict Flower and other operational interfaces to authorized operators.

## Storage

- Use TLS and private networking for object storage where available.
- Grant the application only the permissions it needs.
- Review bucket/container public access, CORS, retention, and backup policies.
- Prefer workload identity or short-lived credentials where supported.

## Application security and observability

- Review default API permissions, authentication, throttling, and object-level access.
- Avoid logging secrets, tokens, or unnecessary personal information.
- Configure error monitoring and alerting appropriate to the service.
- Keep dependencies updated and review security advisories.

Complete a deployment-specific security review; this checklist is not a guarantee that an application is secure.
