#!/usr/bin/env bash
set -euo pipefail

echo "Uploading file..."
response=$(curl -X 'POST' \
    'http://localhost:8000/upload/?token=jessica' \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'file=@README.md')

# Extract filename and URL from the response JSON
filename=$(echo "$response" | jq -r '.filename')
url=$(echo "$response" | jq -r '.url')

echo "Downloading file..."
download_filename="round_trip.md"
curl -J -o $download_filename "$url"

echo "File downloaded successfully: $filename"

string_to_assert="fastapi-playground"

if grep -q "$string_to_assert" "$filename"; then
    echo "String '$string_to_assert' found in file"
else
    echo "String '$string_to_assert' not found in file"
fi

rm $download_filename
