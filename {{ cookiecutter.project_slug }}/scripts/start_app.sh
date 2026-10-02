#!/bin/bash

set -euo pipefail

# --- Configuration ---
# Base directory for all apps, relative to the project root.
APPS_RELATIVE_DIR="apps"

# --- Script Logic ---

# Determine the project root directory by searching for manage.py
# This script assumes manage.py is in the project's root directory.
PROJECT_ROOT=$(pwd)
while [ ! -f "${PROJECT_ROOT}/manage.py" ]; do
  cd ..
  PROJECT_ROOT=$(pwd)

  # Safety break: if we go up too far and don't find manage.py
  if [ "$(pwd)" = "/" ]; then
    echo "Error: Could not find manage.py. Are you running this from within a Django project?"
    exit 1
  fi
done

# Now that we have the project root, construct the full path to the apps directory.
APPS_BASE_DIR="${PROJECT_ROOT}/${APPS_RELATIVE_DIR}"

# Check if an app name was provided.
if [ -z "${1:-}" ]; then
  echo "Usage: $0 <app_name> [verbose_name]"
  echo "Example: $0 users"
  echo "Example: $0 payment_history 'Payment History'"
  exit 1
fi

APP_NAME=$1
APP_VERBOSE_NAME="${2:-}"

# Validate the app name.
if [[ ! "${APP_NAME}" =~ ^[a-z][a-z0-9_]*$ ]]; then
  echo "Error: App name must start with a lowercase letter and contain only lowercase letters, numbers, and underscores."
  exit 1
fi

APP_FULL_PATH="${APPS_BASE_DIR}/${APP_NAME}"

# Check if an app directory already exists within the base apps directory.
if [ -d "${APP_FULL_PATH}" ]; then
  echo "Error: App '${APP_NAME}' already exists in '${APPS_BASE_DIR}/'."
  exit 1
fi

# Use a readable default verbose name when none is provided.
if [ -z "${APP_VERBOSE_NAME}" ]; then
  APP_VERBOSE_NAME=$(printf '%s' "${APP_NAME}" | tr '_' ' ' | sed 's/.*/\u&/')
fi

# Convert snake_case app names to PascalCase class names.
APP_CLASS_NAME=$(printf '%s' "${APP_NAME}" | awk -F_ '{
  for (i = 1; i <= NF; i++) {
    $i = toupper(substr($i, 1, 1)) substr($i, 2)
  }
  printf "%s", $1
  for (i = 2; i <= NF; i++) {
    printf "%s", $i
  }
}')

# Ensure the base apps directory exists.
mkdir -p "${APPS_BASE_DIR}"

# Create the main app directory inside the APPS_BASE_DIR.
echo "Creating app directory: ${APP_FULL_PATH}"
mkdir -p "${APP_FULL_PATH}"

# Define the content for apps.py.
APPS_PY_CONTENT=$(cat <<EOF
from django.apps import AppConfig


class ${APP_CLASS_NAME}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "${APPS_RELATIVE_DIR}.${APP_NAME}"
    verbose_name = "${APP_VERBOSE_NAME}"
EOF
)

# Create the necessary files and subdirectories with __init__.py.
echo "Creating structure and empty files..."

# Root files.
touch "${APP_FULL_PATH}/__init__.py"
printf '%s\n' "${APPS_PY_CONTENT}" > "${APP_FULL_PATH}/apps.py"

mkdir -p "${APP_FULL_PATH}/models"
touch "${APP_FULL_PATH}/models/__init__.py"

mkdir -p "${APP_FULL_PATH}/services"
touch "${APP_FULL_PATH}/services/__init__.py"

mkdir -p "${APP_FULL_PATH}/selectors"
touch "${APP_FULL_PATH}/selectors/__init__.py"

mkdir -p "${APP_FULL_PATH}/serializers"
touch "${APP_FULL_PATH}/serializers/__init__.py"

mkdir -p "${APP_FULL_PATH}/permissions"
touch "${APP_FULL_PATH}/permissions/__init__.py"

touch "${APP_FULL_PATH}/admin.py"
touch "${APP_FULL_PATH}/urls.py"

# Migrations subdirectory.
mkdir -p "${APP_FULL_PATH}/migrations"
touch "${APP_FULL_PATH}/migrations/__init__.py"

# Tests subdirectory.
mkdir -p "${APP_FULL_PATH}/tests"
touch "${APP_FULL_PATH}/tests/__init__.py"

mkdir -p "${APP_FULL_PATH}/tests/api"
touch "${APP_FULL_PATH}/tests/api/__init__.py"

mkdir -p "${APP_FULL_PATH}/tests/services"
touch "${APP_FULL_PATH}/tests/services/__init__.py"

mkdir -p "${APP_FULL_PATH}/tests/selectors"
touch "${APP_FULL_PATH}/tests/selectors/__init__.py"

# Views subdirectory.
mkdir -p "${APP_FULL_PATH}/views/api/v1"
touch "${APP_FULL_PATH}/views/__init__.py"
touch "${APP_FULL_PATH}/views/api/__init__.py"
touch "${APP_FULL_PATH}/views/api/v1/__init__.py"

echo ""
echo "--------------------------------------------------"
echo "App structure '${APP_NAME}' created successfully at '${APP_FULL_PATH}'"
echo "--------------------------------------------------"
echo ""
echo "Next steps:"
echo "1. Add 'apps.${APP_NAME}' to INSTALLED_APPS in your settings file."
echo "2. Manually create your models in ${APP_FULL_PATH}/models/, serializers, services, etc."
echo "3. Run 'python manage.py makemigrations ${APP_NAME}' to create initial migration files after defining models."
echo "4. Run 'python manage.py migrate' to apply migrations."
echo "5. Configure your project's urls.py to include the app's urls.py."
echo ""
echo "Happy coding!"
