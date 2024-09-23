import json
from pathlib import Path
from fastapi.openapi.utils import get_openapi
from app.main import app

ALLOW_PATHS = ["/upload/", "/upload-many/"]


def save_openapi_json():
    """
    Generate and save the OpenAPI JSON schema for the FastAPI app
    """
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["paths"] = {
        path: operations
        for path, operations in openapi_schema["paths"].items()
        if path in ALLOW_PATHS
    }

    output_path = Path(__file__).parent.parent / "docs" / "openapi.json"

    with open(output_path, "w") as f:
        json.dump(openapi_schema, f, indent=2)
        f.write("\n")

    print(f"OpenAPI JSON saved to {output_path}")


if __name__ == "__main__":
    save_openapi_json()
