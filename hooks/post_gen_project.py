from pathlib import Path
import secrets
import shutil
import string

project_dir = Path.cwd()

# Give each generated project a usable local environment without overwriting
# an existing .env file or copying real credentials into version control.
env_file = project_dir / ".env"
env_example = project_dir / ".env.example"
if not env_file.exists() and env_example.exists():
    content = env_example.read_text(encoding="utf-8")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secret_key = "".join(secrets.choice(alphabet) for _ in range(64))
    content = content.replace("SECRET_KEY=\n", f"SECRET_KEY={secret_key}\n", 1)
    env_file.write_text(content, encoding="utf-8")

if "{{ cookiecutter.use_docker }}" != "y":
    docker_compose = project_dir / "docker-compose.yml"
    docker_dir = project_dir / "docker"
    if docker_compose.exists():
        docker_compose.unlink()
    if docker_dir.exists():
        shutil.rmtree(docker_dir)
