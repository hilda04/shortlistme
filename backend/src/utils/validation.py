from data.roles import ROLES
from utils.config import MAX_UPLOAD_BYTES


def validate_upload(file_name: str, size_bytes: int):
    if not file_name.lower().endswith(".pdf"):
        raise ValueError("Only PDF uploads are supported")
    if size_bytes > MAX_UPLOAD_BYTES:
        raise ValueError(f"File exceeds max upload size of {MAX_UPLOAD_BYTES} bytes")


def validate_role(target_role: str):
    if target_role not in ROLES:
        raise ValueError("Unsupported target role")
