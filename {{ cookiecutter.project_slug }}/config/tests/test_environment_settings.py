import os
import subprocess
import sys


def test_documented_environment_settings_are_applied():
    environment = os.environ.copy()
    environment.update(
        {
            "LANGUAGE_CODE": "en-us",
            "TIME_ZONE": "Europe/Berlin",
        }
    )
    script = """
from config.settings import base

assert base.LANGUAGE_CODE == "en-us"
assert base.TIME_ZONE == "Europe/Berlin"
assert base.STATIC_URL == "/static/"
assert base.MEDIA_URL == "/media/"
assert base.STATIC_ROOT == base.BASE_DIR / "staticfiles"
assert base.MEDIA_ROOT == base.BASE_DIR / "media"
"""
    subprocess.run(
        [sys.executable, "-c", script],
        check=True,
        env=environment,
    )
