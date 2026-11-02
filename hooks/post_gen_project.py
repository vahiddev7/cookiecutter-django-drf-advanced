from pathlib import Path
import secrets
import re
import shutil
import string

project_dir = Path.cwd()
database_engine = "{{ cookiecutter.database_engine }}"
cloud_storage = "{{ cookiecutter.cloud_storage }}"
project_slug = "{{ cookiecutter.project_slug }}"

database_identifier = re.sub(r"[^A-Za-z0-9_]", "_", project_slug)

env_file = project_dir / ".env"
env_example = project_dir / ".env.example"
if not env_file.exists() and env_example.exists():
    content = env_example.read_text(encoding="utf-8")
    secret_key = secrets.token_urlsafe(48)
    content = content.replace("SECRET_KEY=\n", f"SECRET_KEY={secret_key}\n", 1)
    password_characters = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("_-"),
    ]
    password_alphabet = string.ascii_letters + string.digits + "_-"
    password_characters.extend(
        secrets.choice(password_alphabet) for _ in range(28)
    )
    secrets.SystemRandom().shuffle(password_characters)
    database_password = "".join(password_characters)
    database_settings = {
        "postgresql": {
            "DB_NAME": database_identifier,
            "DB_USER": database_identifier,
            "DB_PASSWORD": database_password,
            "DB_HOST": "localhost",
            "DB_PORT": "5432",
        },
        "mysql": {
            "DB_NAME": database_identifier,
            "DB_USER": database_identifier,
            "DB_PASSWORD": database_password,
            "DB_HOST": "localhost",
            "DB_PORT": "3306",
        },
        "sqlserver": {
            "DB_NAME": database_identifier,
            "DB_USER": "sa",
            "DB_PASSWORD": database_password,
            "DB_HOST": "localhost",
            "DB_PORT": "1433",
            "DB_TRUST_SERVER_CERTIFICATE": "True",
        },
    }.get(database_engine)

    if database_settings:
        content += "\n# Active settings for the selected database engine\n"
        content += "".join(
            f"{key}={value}\n" for key, value in database_settings.items()
        )

    if "{{ cookiecutter.use_celery }}" == "y" and "{{ cookiecutter.celery_broker }}" == "rabbitmq":
        rabbitmq_user = "app_" + secrets.token_hex(8)
        rabbitmq_password = secrets.token_urlsafe(32)
        content += "\n# Active RabbitMQ credentials for this generated project\n"
        content += f"RABBITMQ_DEFAULT_USER={rabbitmq_user}\n"
        content += f"RABBITMQ_DEFAULT_PASS={rabbitmq_password}\n"

    env_file.write_text(content, encoding="utf-8")

if cloud_storage == "none":
    storage_settings = project_dir / "config" / "settings" / "storage.py"
    if storage_settings.exists():
        storage_settings.unlink()

if "{{ cookiecutter.use_drf }}" != "y":
    authentication_app = project_dir / "apps" / "authentication"
    if authentication_app.exists():
        shutil.rmtree(authentication_app)

if "{{ cookiecutter.use_celery }}" != "y":
    celery_config = project_dir / "config" / "celery.py"
    if celery_config.exists():
        celery_config.unlink()

if "{{ cookiecutter.use_drf }}" != "y" or "{{ cookiecutter.use_swagger }}" != "y":
    swagger_assets = project_dir / "static" / "swagger"
    if swagger_assets.exists():
        shutil.rmtree(swagger_assets)

if "{{ cookiecutter.use_docker }}" != "y":
    docker_compose = project_dir / "docker-compose.yml"
    docker_dir = project_dir / "docker"
    if docker_compose.exists():
        docker_compose.unlink()
    if docker_dir.exists():
        shutil.rmtree(docker_dir)

if "{{ cookiecutter.use_drf }}" != "y":
    authentication_app = project_dir / "apps" / "authentication"
    if authentication_app.exists():
        shutil.rmtree(authentication_app)
