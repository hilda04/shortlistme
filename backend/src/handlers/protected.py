import json
import uuid
from repositories.analysis_repository import AnalysisRepository
from services.analysis_service import AnalysisService
from services.storage_service import StorageService
from utils.auth import get_user_id
from utils.response import json_response
from utils.validation import validate_role, validate_upload


analysis_repo = AnalysisRepository()
storage = StorageService()
analysis_service = AnalysisService()


def me_handler(event, context, params):
    user_id = get_user_id(event)
    return json_response(200, {"userId": user_id})


def presign_upload_handler(event, context, params):
    user_id = get_user_id(event)
    payload = json.loads(event.get("body") or "{}")
    file_name = payload.get("fileName", "")
    size_bytes = int(payload.get("sizeBytes", 0))

    try:
        validate_upload(file_name, size_bytes)
    except ValueError as err:
        return json_response(400, {"error": "ValidationError", "message": str(err)})

    object_key = f"uploads/{user_id}/{uuid.uuid4()}-{file_name}"
    upload_url = storage.presign_upload(object_key)
    return json_response(200, {"uploadUrl": upload_url, "objectKey": object_key})


def create_analysis_handler(event, context, params):
    user_id = get_user_id(event)
    payload = json.loads(event.get("body") or "{}")
    try:
        validate_role(payload.get("targetRole", ""))
        if not payload.get("cvObjectKey", "").startswith(f"uploads/{user_id}/"):
            return json_response(400, {"error": "ValidationError", "message": "Invalid cvObjectKey for user"})
    except ValueError as err:
        return json_response(400, {"error": "ValidationError", "message": str(err)})

    created = analysis_service.run_analysis(user_id, payload)
    return json_response(201, created)


def list_analyses_handler(event, context, params):
    user_id = get_user_id(event)
    return json_response(200, {"items": analysis_repo.list(user_id)})


def get_analysis_handler(event, context, params):
    user_id = get_user_id(event)
    item = analysis_repo.get(user_id, params["analysisId"])
    if not item:
        return json_response(404, {"error": "NotFound", "message": "Analysis not found"})
    return json_response(200, item)


def download_analysis_handler(event, context, params):
    user_id = get_user_id(event)
    item = analysis_repo.get(user_id, params["analysisId"])
    if not item:
        return json_response(404, {"error": "NotFound", "message": "Analysis not found"})

    file_type = params["type"]
    key_map = {"improved-cv": item.get("improvedCvKey"), "cover-letter": item.get("coverLetterKey")}
    target_key = key_map.get(file_type)
    if not target_key:
        return json_response(400, {"error": "ValidationError", "message": "Unsupported download type"})

    return json_response(200, {"downloadUrl": storage.presign_download(target_key)})
