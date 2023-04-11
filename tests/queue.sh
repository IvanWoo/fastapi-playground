for i in {40..45}; do
    curl -X 'POST' \
        "http://localhost:8000/queue?item=$i&token=jessica" \
        -H 'accept: application/json' \
        -d ''
done
