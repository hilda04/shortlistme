from utils.response import json_response
from utils.router import Router
from handlers.public import health_handler, roles_handler
from handlers.protected import (
    me_handler,
    presign_upload_handler,
    create_analysis_handler,
    list_analyses_handler,
    get_analysis_handler,
    download_analysis_handler,
)

router = Router()
router.add("GET", "/health", health_handler, protected=False)
router.add("GET", "/roles", roles_handler, protected=False)
router.add("GET", "/me", me_handler, protected=True)
router.add("POST", "/uploads/presign", presign_upload_handler, protected=True)
router.add("POST", "/analyses", create_analysis_handler, protected=True)
router.add("GET", "/analyses", list_analyses_handler, protected=True)
router.add("GET", "/analyses/{analysisId}", get_analysis_handler, protected=True)
router.add(
    "GET",
    "/analyses/{analysisId}/download/{type}",
    download_analysis_handler,
    protected=True,
)


def lambda_handler(event, context):
    try:
        return router.dispatch(event, context)
    except Exception as exc:  # top-level guard
        return json_response(500, {"error": "InternalServerError", "message": str(exc)})
