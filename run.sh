#!/usr/bin/env bash
set -e
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is required. Please install Python 3.10+."
  exit 1
fi
python3 src/near_miss.py
