#!/bin/sh
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$BASE_DIR/../.."

OPENAPI_CLIENT_JSON="$ROOT_DIR/docs/openapi.json"
OPENAPI_CLIENT_DEST="$ROOT_DIR/src/client/_generated/"
OPENAPI_CLIENT_CONFIG="$ROOT_DIR/scripts/openapi/openapi_client_config.json"

echo "Generating openapi client schema"
pdm run openapi-save

echo "Cleaning up"
rm -rf $OPENAPI_CLIENT_DEST

echo "Generating the client"
openapi-generator generate -i $OPENAPI_CLIENT_JSON -g python -o $OPENAPI_CLIENT_DEST -c $OPENAPI_CLIENT_CONFIG

echo "Flatting the generated folder"
mv $OPENAPI_CLIENT_DEST/client/_generated/* $OPENAPI_CLIENT_DEST
rm -rf $OPENAPI_CLIENT_DEST/client
