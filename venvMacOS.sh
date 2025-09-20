#!/usr/bin/env bash

#===============================================================================
#   mac_setup_python_env_fixed.sh
#
#   This script (for macOS) will:
#     - ensure pyenv is initialized properly
#     - install a specified Python version (if requested)
#     - create a project directory and virtual environment
#     - fallback to python3 if `python` is missing (especially when pyenv version is "system")
#     - install dependencies if a requirements file is given
#
#   Usage (source this so activation persists):
#     source mac_setup_python_env_fixed.sh \
#         [--py-version 3.11.5] \
#         [--project-dir myproject] \
#         [--venv-dir .venv] \
#         [--req requirements.txt]
#===============================================================================

set -e  # Exit on error

# Defaults
PY_VERSION=""             # e.g. "3.11.5"; if blank, uses pyenv's current or latest stable
PROJECT_DIR="."
VENV_DIR=".venv"
REQUIREMENTS_FILE=""

# Help message
usage() {
  cat <<EOF
Usage: source mac_setup_python_env_fixed.sh [OPTIONS]

Options:
  --py-version VERSION      Python version to install/use via pyenv (e.g. 3.11.5)
  --project-dir DIR         Directory for your project (default: ${PROJECT_DIR})
  --venv-dir DIR            Name or path of virtual environment inside project (default: ${VENV_DIR})
  --req FILE                Path to requirements.txt to install dependencies
  --help                    Show this help message

Example:
  source mac_setup_python_env_fixed.sh --py-version 3.12.1 --project-dir ~/projects/myapp --venv-dir .venv --req requirements.txt
EOF
}

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --py-version)
      shift
      PY_VERSION="$1"
      ;;
    --project-dir)
      shift
      PROJECT_DIR="$1"
      ;;
    --venv-dir)
      shift
      VENV_DIR="$1"
      ;;
    --req)
      shift
      REQUIREMENTS_FILE="$1"
      ;;
    --help)
      usage
      return 0
      ;;
    *)
      echo "Unknown option: $1"
      usage
      return 1
      ;;
  esac
  shift
done

# -------------------------------------------------------------------------------
#  Ensure pyenv is installed & shell is set up
# -------------------------------------------------------------------------------

if ! command -v pyenv >/dev/null 2>&1; then
  echo "Error: pyenv is not installed. Please install pyenv first (e.g. via brew)."
  return 1
fi

# Initialize pyenv in this shell
export PYENV_ROOT="$HOME/.pyenv"
# ensure pyenv's bin is in PATH
if [[ -d "$PYENV_ROOT/bin" ]]; then
  export PATH="$PYENV_ROOT/bin:$PATH"
fi
# load pyenv
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# -------------------------------------------------------------------------------
#  Install or pick Python version via pyenv
# -------------------------------------------------------------------------------

if [[ -n "$PY_VERSION" ]]; then
  if ! pyenv versions --bare | grep -qx "$PY_VERSION"; then
    echo "Installing Python ${PY_VERSION} via pyenv..."
    pyenv install "$PY_VERSION"
  else
    echo "Python ${PY_VERSION} already installed via pyenv."
  fi
  # set local version for this project
  pyenv local "$PY_VERSION"
  ACTIVE_PY_VERSION="$PY_VERSION"
else
  # If no version specified, check what pyenv version is active
  ACTIVE_PY_VERSION="$(pyenv version-name)"
  if [[ "$ACTIVE_PY_VERSION" == "system" ]]; then
    echo "Using pyenv version 'system'. Beware: 'python' may not exist in this mode."
  else
    echo "Using pyenv version '${ACTIVE_PY_VERSION}'."
  fi
fi

# -------------------------------------------------------------------------------
#  Ensure project directory
# -------------------------------------------------------------------------------

echo "Project directory: ${PROJECT_DIR}"
mkdir -p "${PROJECT_DIR}"
cd "${PROJECT_DIR}"

# -------------------------------------------------------------------------------
#  Determine the python executable to use (for venv creation)
# -------------------------------------------------------------------------------

PY_EXEC=""

if [[ "$ACTIVE_PY_VERSION" == "system" ]]; then
  # With macOS 12.3+, system python (python2) is usually gone; default to python3
  if command -v python >/dev/null 2>&1; then
    PY_EXEC="python"
  elif command -v python3 >/dev/null 2>&1; then
    PY_EXEC="python3"
  else
    echo "Error: No 'python' or 'python3' command found for system version. Please install Python or choose a pyenv version."
    return 1
  fi
else
  # Non-system pyenv version should provide python via shims
  if pyenv which python >/dev/null 2>&1; then
    PY_EXEC="python"
  else
    # fallback
    if command -v python3 >/dev/null 2>&1; then
      PY_EXEC="python3"
    else
      echo "Error: python executable not found under selected pyenv version."
      return 1
    fi
  fi
fi

echo "Using python executable: ${PY_EXEC}"

# -------------------------------------------------------------------------------
#  Create virtual environment
# -------------------------------------------------------------------------------

VENV_FULL_PATH="${PROJECT_DIR}/${VENV_DIR}"

if [[ -d "${VENV_FULL_PATH}" ]]; then
  echo "Virtual environment directory '${VENV_FULL_PATH}' already exists."
else
  echo "Creating virtual environment '${VENV_DIR}' in ${PROJECT_DIR}..."
  # Use $PY_EXEC to create
  $PY_EXEC -m venv "${VENV_DIR}"
  echo "Virtual environment created at ${VENV_FULL_PATH}."
fi

# -------------------------------------------------------------------------------
#  Activate the virtual environment
# -------------------------------------------------------------------------------

echo "Activating the virtual environment..."
# shellcheck disable=SC1090
source "${VENV_FULL_PATH}/bin/activate"

# -------------------------------------------------------------------------------
#  Upgrade pip, install dependencies if provided
# -------------------------------------------------------------------------------

echo "Upgrading pip..."
pip install --upgrade pip

if [[ -n "${REQUIREMENTS_FILE}" ]]; then
  if [[ -f "${PROJECT_DIR}/${REQUIREMENTS_FILE}" ]]; then
    echo "Installing requirements from ${REQUIREMENTS_FILE}..."
    pip install -r "${REQUIREMENTS_FILE}"
    echo "Dependencies installed."
  else
    echo "WARNING: requirements file '${REQUIREMENTS_FILE}' not found under ${PROJECT_DIR}. Skipping installation."
  fi
fi

echo "Done. Virtual environment '${VENV_DIR}' is active in directory '${PROJECT_DIR}'."