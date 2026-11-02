import logging

from config.settings.env import env


def configure_sentry():
    """Initialize Sentry only when a DSN is explicitly configured."""
    dsn = env("SENTRY_DSN", default="").strip()
    if not dsn:
        return

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    # Sample rates are environment-driven so production cost and volume can be tuned.
    sentry_sdk.init(
        dsn=dsn,
        integrations=[
            DjangoIntegration(),
            LoggingIntegration(
                level=logging.INFO,
                event_level=logging.ERROR,
            ),
        ],
        environment=env("SENTRY_ENVIRONMENT", default="development"),
        traces_sample_rate=env.float("SENTRY_TRACES_SAMPLE_RATE", default=0.0),
        profiles_sample_rate=env.float("SENTRY_PROFILES_SAMPLE_RATE", default=0.0),
        send_default_pii=env.bool("SENTRY_SEND_DEFAULT_PII", default=False),
    )
