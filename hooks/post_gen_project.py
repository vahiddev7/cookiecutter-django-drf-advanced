from pathlib import Path
import secrets
import shutil

project_dir = Path.cwd()
database_engine = "{{ cookiecutter.database_engine }}"
project_slug = "{{ cookiecutter.project_slug }}"

# Give each generated project a usable local environment without overwriting
# an existing .env file or copying real credentials into version control.
env_file = project_dir / ".env"
env_example = project_dir / ".env.example"
if not env_file.exists() and env_example.exists():
    content = env_example.read_text(encoding="utf-8")
    secret_key = secrets.token_urlsafe(48)
    content = content.replace("SECRET_KEY=\n", f"SECRET_KEY={secret_key}\n", 1)

    database_password = secrets.token_urlsafe(24)
    database_settings = {
        "postgresql": {
            "DB_NAME": project_slug,
            "DB_USER": project_slug,
            "DB_PASSWORD": database_password,
            "DB_HOST": "localhost",
            "DB_PORT": "5432",
        },
        "mysql": {
            "DB_NAME": project_slug,
            "DB_USER": project_slug,
            "DB_PASSWORD": database_password,
            "DB_HOST": "localhost",
            "DB_PORT": "3306",
        },
        "sqlserver": {
            "DB_NAME": project_slug,
            "DB_USER": "sa",
            "DB_PASSWORD": database_password,
            "DB_HOST": "localhost",
            "DB_PORT": "1433",
        },
    }.get(database_engine)

    if database_settings:
        content += "\n# Active settings for the selected database engine\n"
        content += "".join(
            f"{key}={value}\n" for key, value in database_settings.items()
        )

    env_file.write_text(content, encoding="utf-8")

if "{{ cookiecutter.use_docker }}" != "y":
    docker_compose = project_dir / "docker-compose.yml"
    docker_dir = project_dir / "docker"
    if docker_compose.exists():
        docker_compose.unlink()
    if docker_dir.exists():
        shutil.rmtree(docker_dir)
