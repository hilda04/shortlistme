import boto3
from utils.config import ARTIFACTS_BUCKET_NAME

s3 = boto3.client("s3")


class StorageService:
    bucket_name = ARTIFACTS_BUCKET_NAME

    def presign_upload(self, key: str, expires_in: int = 600):
        return s3.generate_presigned_url(
            "put_object",
            Params={"Bucket": self.bucket_name, "Key": key, "ContentType": "application/pdf"},
            ExpiresIn=expires_in,
        )

    def presign_download(self, key: str, expires_in: int = 600):
        return s3.generate_presigned_url(
            "get_object", Params={"Bucket": self.bucket_name, "Key": key}, ExpiresIn=expires_in
        )

    def get_bytes(self, key: str) -> bytes:
        obj = s3.get_object(Bucket=self.bucket_name, Key=key)
        return obj["Body"].read()

    def put_bytes(self, key: str, body: bytes, content_type: str = "application/pdf"):
        s3.put_object(Bucket=self.bucket_name, Key=key, Body=body, ContentType=content_type)
