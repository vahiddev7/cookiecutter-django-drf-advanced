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

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    {% if cookiecutter.use_drf == "y" %}
    'rest_framework',
    {% endif %}
    {% if cookiecutter.use_swagger == 'y' %}
    "drf_spectacular",
    {% endif %}
    'apps.common',
    'apps.users',
]

DATABASES = {
    "default": {}
}

{% if cookiecutter.database_engine == 'sqlite' %}
DATABASES['default'].update({
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
})
{% elif cookiecutter.database_engine == 'postgresql' %}
DATABASES['default'].update({
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env("DB_NAME"),
    'USER': env("DB_USER"),
    'PASSWORD': env("DB_PASSWORD"),
    'HOST': env("DB_HOST"),
    'PORT': env("DB_PORT"),    
})
{% elif cookiecutter.database_engine == 'mysql' %}
DATABASES['default'].update({
    'ENGINE': 'django.db.backends.mysql',
    'NAME': env("DB_NAME"),
    'USER': env("DB_USER"),
    'PASSWORD': env("DB_PASSWORD"),
    'HOST': env("DB_HOST"),
    'PORT': env("DB_PORT"), 
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    }
})
{% elif cookiecutter.database_engine == 'sqlserver' %}
DATABASES['default'].update({
    'ENGINE': 'sql_server.pyodbc',
    'NAME': env("DB_NAME"),
    'USER': env("DB_USER"),
    'PASSWORD': env("DB_PASSWORD"),
    'HOST': env("DB_HOST"),
    'PORT': env("DB_PORT"), 
    'OPTIONS': {
        'driver': 'ODBC Driver 17 for SQL Server',
    },
})
{% endif %}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

LANGUAGE_CODE = 'fa'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

WSGI_APPLICATION = 'config.wsgi.application'

# Asgi config for channels
ASGI_APPLICATION = "config.asgi.application"


ROOT_URLCONF = 'config.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'


AUTH_USER_MODEL = "users.User"


{% if cookiecutter.use_drf == "y" %}
REST_FRAMEWORK = {
    {% if cookiecutter.use_swagger == 'y' %}
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    {% endif %}
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
{% endif %}

{% if cookiecutter.use_swagger == 'y' %}
SPECTACULAR_SETTINGS = {
    "TITLE": "{{ cookiecutter.project_slug }}" + " API",
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {"deepLinking": True},
}
{% endif %}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}


{% if cookiecutter.use_celery == 'y' %}
# Celery Configuration
{% if cookiecutter.celery_broker == 'redis' %}
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://broker:6379/0")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://broker:6379/0")
{% else %}
CELERY_BROKER_URL = env(
    "CELERY_BROKER_URL",
    default="amqp://guest:guest@broker:5672//",
)
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="rpc://")
{% endif %}
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
{% endif %}
