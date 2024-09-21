import os
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File, Form
from botocore.exceptions import NoCredentialsError
import boto3


router = APIRouter()

MINIO_URL = "http://localhost:9000"
ACCESS_KEY = "minio_access_key"
SECRET_KEY = "minio_secret_key"
BUCKET_NAME = "fastapi-playground"

s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="us-east-1",
)


def _upload_file_one(file: File) -> str:
    _, extension = os.path.splitext(file.filename)
    s3_file_name = f"{uuid4()}{extension}"

    # Upload file to Minio
    s3_client.upload_fileobj(file.file, BUCKET_NAME, s3_file_name)

    # Generate the signed URL
    url = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET_NAME, "Key": s3_file_name},
        ExpiresIn=600,
    )
    return {"filename": file.filename, "url": url}


@router.post("/upload/", tags=["upload"])
async def upload_file(file: UploadFile = File(...)):
    try:
        return _upload_file_one(file)

    except NoCredentialsError:
        return {"error": "Missing credentials"}


@router.post("/upload-many/", tags=["upload"])
async def upload_files(files: list[UploadFile], entity: str = Form(...)):
    ret = []
    for file in files:
        ret.append({**_upload_file_one(file), "entity": entity})
    return ret
