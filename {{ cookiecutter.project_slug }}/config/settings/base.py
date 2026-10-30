import os
from datetime import timedelta
from pathlib import Path

from config.settings.env import env

{% if cookiecutter.database_engine == "mysql" %}
import pymysql

pymysql.install_as_MySQLdb()
{% endif %}

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Cross-origin access is disabled unless explicit origins are configured.
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", default=False)
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# Database-backed cache state is shared by all Django/Gunicorn workers.
# This keeps DRF throttling consistent without requiring an optional Redis service.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache",
    }
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "corsheaders",
    "django.contrib.staticfiles",
    {% if cookiecutter.use_drf == "y" and cookiecutter.database_engine != "sqlserver" %}
    "rest_framework_simplejwt.token_blacklist",
    {% endif %}
    {% if cookiecutter.use_drf == "y" %}
    "rest_framework",
    "apps.authentication",
    {% endif %}
    {% if cookiecutter.use_drf == "y" and cookiecutter.use_swagger == "y" %}
    "drf_spectacular",
    {% endif %}
    "apps.core",
    "apps.users",
]

DATABASES = {"default": {}}

{% if cookiecutter.database_engine == "sqlite" %}
os.makedirs(BASE_DIR / "data", exist_ok=True)
DATABASES["default"].update({
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "data" / "db.sqlite3",
})
{% elif cookiecutter.database_engine == "postgresql" %}
DATABASES["default"].update({
    "ENGINE": "django.db.backends.postgresql",
    "NAME": env("DB_NAME"),
    "USER": env("DB_USER"),
    "PASSWORD": env("DB_PASSWORD"),
    "HOST": env("DB_HOST"),
    "PORT": env("DB_PORT"),
})
{% elif cookiecutter.database_engine == "mysql" %}
DATABASES["default"].update({
    "ENGINE": "django.db.backends.mysql",
    "NAME": env("DB_NAME"),
    "USER": env("DB_USER"),
    "PASSWORD": env("DB_PASSWORD"),
    "HOST": env("DB_HOST"),
    "PORT": env("DB_PORT"),
    "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
})
{% elif cookiecutter.database_engine == "sqlserver" %}
DATABASES["default"].update({
    "ENGINE": "mssql",
    "NAME": env("DB_NAME"),
    "USER": env("DB_USER"),
    "PASSWORD": env("DB_PASSWORD"),
    "HOST": env("DB_HOST"),
    "PORT": env("DB_PORT"),
    "OPTIONS": {
        "driver": "ODBC Driver 18 for SQL Server",
        "extra_params": f"TrustServerCertificate={'yes' if env.bool('DB_TRUST_SERVER_CERTIFICATE', default=False) else 'no'}",
    },
})
{% endif %}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]
LANGUAGE_CODE = env("LANGUAGE_CODE", default="fa")
TIME_ZONE = env("TIME_ZONE", default="UTC")
USE_I18N = True
USE_TZ = True

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"
ROOT_URLCONF = "config.urls"

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"
AUTH_USER_MODEL = "users.User"

{% if cookiecutter.use_drf == "y" %}
REST_FRAMEWORK = {
    {% if cookiecutter.use_swagger == "y" %}
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    {% endif %}
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "login": "5/minute",
        "register": "3/hour",
    },
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    {% if cookiecutter.database_engine == "sqlserver" %}
    # mssql-django cannot alter AutoField to BigAutoField, as required by
    # SimpleJWT's token blacklist migration 0008.
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    {% else %}
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    {% endif %}
}
{% endif %}

{% if cookiecutter.use_drf == "y" and cookiecutter.use_swagger == "y" %}
SPECTACULAR_SETTINGS = {
    "TITLE": "{{ cookiecutter.project_slug }}" + " API",
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {"deepLinking": True},
}
{% endif %}

{% if cookiecutter.use_celery == "y" %}
# Celery Configuration
{% if cookiecutter.celery_broker == "redis" %}
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://broker:6379/0")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://broker:6379/0")
{% else %}
from urllib.parse import quote

CELERY_BROKER_URL = env("CELERY_BROKER_URL", default=None) or (
    f"amqp://{quote(env('RABBITMQ_DEFAULT_USER'), safe='')}:"
    f"{quote(env('RABBITMQ_DEFAULT_PASS'), safe='')}@broker:5672//"
)
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="rpc://")
{% endif %}
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
{% endif %}
