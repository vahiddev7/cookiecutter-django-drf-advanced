#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
APPS_BASE_DIR="${PROJECT_ROOT}/apps"

usage() {
  echo "Usage: ./scripts/start_app.sh <app_name> [verbose_name]"
}

if [[ $# -lt 1 || $# -gt 2 ]]; then usage >&2; exit 2; fi
APP_NAME="$1"
APP_VERBOSE_NAME="${2:-}"

if [[ ! "${APP_NAME}" =~ ^[a-z][a-z0-9_]*$ ]]; then
  echo "Error: app name must start with a lowercase letter and contain only lowercase letters, numbers, and underscores." >&2
  exit 2
fi
APP_FULL_PATH="${APPS_BASE_DIR}/${APP_NAME}"
if [[ -e "${APP_FULL_PATH}" ]]; then
  echo "Error: app '${APP_NAME}' already exists." >&2
  exit 1
fi
if [[ -z "${APP_VERBOSE_NAME}" ]]; then
  APP_VERBOSE_NAME="$(printf '%s' "${APP_NAME}" | tr '_' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2); print}')"
fi
APP_CLASS_NAME="$(printf '%s' "${APP_NAME}" | awk -F_ '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2); printf "%s",$0}' | tr -d ' ')"

mkdir -p "${APP_FULL_PATH}"/{models,migrations}
touch "${APP_FULL_PATH}/__init__.py"
cat > "${APP_FULL_PATH}/apps.py" <<EOF
from django.apps import AppConfig


class ${APP_CLASS_NAME}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.${APP_NAME}"
    verbose_name = "${APP_VERBOSE_NAME}"
EOF
for package in models migrations; do
  touch "${APP_FULL_PATH}/${package}/__init__.py"
done
touch "${APP_FULL_PATH}/admin.py"
cat > "${APP_FULL_PATH}/urls.py" <<EOF
urlpatterns = []
EOF

# Register the generated app and expose its URL module under /api/<app_name>/.
python - "${PROJECT_ROOT}" "${APP_NAME}" <<'PY'
from pathlib import Path
import re
import sys

project_root = Path(sys.argv[1])
app_name = sys.argv[2]

settings_path = project_root / "config" / "settings" / "base.py"
settings_text = settings_path.read_text(encoding="utf-8")
app_config = f'"apps.{app_name}"'
if app_config not in settings_text:
    settings_text, count = re.subn(
        r"(INSTALLED_APPS\s*=\s*\[)",
        lambda match: f'{match.group(1)}\n    {app_config},',
        settings_text,
        count=1,
    )
    if count != 1:
        raise SystemExit(f"Could not find INSTALLED_APPS in {settings_path}")
    settings_path.write_text(settings_text, encoding="utf-8")

urls_path = project_root / "config" / "urls.py"
urls_text = urls_path.read_text(encoding="utf-8")
if "from django.urls import include, path" not in urls_text:
    if "from django.urls import path" in urls_text:
        urls_text = urls_text.replace(
            "from django.urls import path",
            "from django.urls import include, path",
            1,
        )
    else:
        urls_text = "from django.urls import include, path\n" + urls_text

route = f'path("api/{app_name}/", include("apps.{app_name}.urls"))'
if route not in urls_text:
    urls_text, count = re.subn(
        r"(urlpatterns\s*=\s*\[)",
        lambda match: f'{match.group(1)}\n    {route},',
        urls_text,
        count=1,
    )
    if count != 1:
        raise SystemExit(f"Could not find urlpatterns in {urls_path}")
    urls_path.write_text(urls_text, encoding="utf-8")
PY

# Keep tests grouped by test scope. Add files only when a test is needed.
TEST_ROOT="${APP_FULL_PATH}/tests"
mkdir -p "${TEST_ROOT}"
touch "${TEST_ROOT}/__init__.py"
for test_type in unit integration e2e; do
  mkdir -p "${TEST_ROOT}/${test_type}"
  touch "${TEST_ROOT}/${test_type}/__init__.py"
done

echo "Created app '${APP_NAME}' at ${APP_FULL_PATH}"
echo "Test layout created under ${TEST_ROOT}"\necho "Add service, selector, serializer, permission, and view modules only when needed."
echo "Registered apps.${APP_NAME} and /api/${APP_NAME}/ in project settings."
echo "Define models and run migrations before using database-backed features."
