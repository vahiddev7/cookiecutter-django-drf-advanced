{% if cookiecutter.use_celery == 'y' %}
from config.settings.celery import app as celery_app

__all__ = ('celery_app',)
{% endif %}
