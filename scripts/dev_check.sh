#!/usr/bin/env bash
set -euo pipefail
black dclean.py src tests || true
ruff check . || true
pytest -q || true
