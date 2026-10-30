import os
import subprocess
import sys


def test_documented_environment_settings_are_applied():
    environment = os.environ.copy()
    environment.update(
        {
            "LANGUAGE_CODE": "en-us",
            "TIME_ZONE": "Europe/Berlin",
            "STATIC_URL": "/assets/",
            "MEDIA_URL": "/uploads/",
            "STATIC_ROOT": "var/static",
            "MEDIA_ROOT": "/srv/project-media",
        }
    )
    script = """
from pathlib import Path
from config.settings import base

assert base.LANGUAGE_CODE == "en-us"
assert base.TIME_ZONE == "Europe/Berlin"
assert base.STATIC_URL == "/assets/"
assert base.MEDIA_URL == "/uploads/"
assert base.STATIC_ROOT == base.BASE_DIR / "var/static"
assert base.MEDIA_ROOT == Path("/srv/project-media")
"""
    subprocess.run(
        [sys.executable, "-c", script],
        check=True,
        env=environment,
    )
