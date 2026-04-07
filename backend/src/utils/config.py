import os


def get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default)


ANALYSES_TABLE_NAME = get_env("ANALYSES_TABLE_NAME")
ARTIFACTS_BUCKET_NAME = get_env("ARTIFACTS_BUCKET_NAME")
ALLOWED_ORIGIN = get_env("ALLOWED_ORIGIN", "*")
MAX_UPLOAD_BYTES = int(get_env("MAX_UPLOAD_BYTES", "5242880"))
