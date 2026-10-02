from pathlib import Path
import shutil

if "{{ cookiecutter.use_docker }}" != "y":
    project_dir = Path.cwd()

    docker_compose = project_dir / "docker-compose.yml"
    docker_dir = project_dir / "docker"

    if docker_compose.exists():
        docker_compose.unlink()

    if docker_dir.exists():
        shutil.rmtree(docker_dir)
