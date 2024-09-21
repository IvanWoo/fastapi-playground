from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader


API_KEY_NAME = "X-API-Key"
API_KEY = "fake-super-secret-token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def authorized(api_token: str = Depends(api_key_header)) -> None:
    if api_token != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No jessica token provided")
