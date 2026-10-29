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

mkdir -p "${APP_FULL_PATH}"/{models,services,selectors,serializers,permissions,migrations,views/api/v1}
touch "${APP_FULL_PATH}/__init__.py"
cat > "${APP_FULL_PATH}/apps.py" <<EOF
from django.apps import AppConfig


class ${APP_CLASS_NAME}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.${APP_NAME}"
    verbose_name = "${APP_VERBOSE_NAME}"
EOF
for package in models services selectors serializers permissions migrations views views/api views/api/v1; do
  touch "${APP_FULL_PATH}/${package}/__init__.py"
done
touch "${APP_FULL_PATH}/admin.py" "${APP_FULL_PATH}/urls.py"

TEST_ROOT="${APP_FULL_PATH}/tests"
touch "${APP_FULL_PATH}/tests/__init__.py"
for category in apis models permissions selectors serializers services; do
  mkdir -p "${TEST_ROOT}/${category}"
  touch "${TEST_ROOT}/${category}/__init__.py"
  for test_type in unit_test integration_test e2e_test; do
    mkdir -p "${TEST_ROOT}/${category}/${test_type}"
    touch "${TEST_ROOT}/${category}/${test_type}/__init__.py"
  done
done

echo "Created app '${APP_NAME}' at ${APP_FULL_PATH}"
echo "Test layout created under ${TEST_ROOT}"
echo "Add apps.${APP_NAME} to INSTALLED_APPS, then define models and run migrations."
