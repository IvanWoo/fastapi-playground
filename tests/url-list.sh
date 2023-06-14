#!/usr/bin/env bash
set -euo pipefail

curl -X 'GET' \
    "http://localhost:8000/url-list?token=jessica" \
    -H 'accept: application/json' \
    -d ''
