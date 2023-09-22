import os
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File
from botocore.exceptions import NoCredentialsError
from botocore.client import Config
import boto3


router = APIRouter()

MINIO_URL = "http://localhost:9000"
ACCESS_KEY = "minio_access_key"
SECRET_KEY = "minio_secret_key"
BUCKET_NAME = "fastapi-playground"

s3 = boto3.resource(
    "s3",
    endpoint_url=MINIO_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1",
)


@router.post("/upload/", tags=["upload"])
async def upload_file(file: UploadFile = File(...)):
    try:
        _, extension = os.path.splitext(file.filename)
        s3_file_name = f"{uuid4()}{extension}"

        # Upload file to Minio
        s3.Bucket(BUCKET_NAME).put_object(Key=s3_file_name, Body=file.file.read())

        # Generate the signed URL
        url = s3.meta.client.generate_presigned_url(
            "get_object",
            Params={"Bucket": BUCKET_NAME, "Key": s3_file_name},
            ExpiresIn=600,
        )

        return {"filename": file.filename, "url": url}

    except NoCredentialsError:
        return {"error": "Missing credentials"}
