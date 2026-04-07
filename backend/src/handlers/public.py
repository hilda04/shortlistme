from services.roles_service import list_roles
from utils.response import json_response


def health_handler(event, context, params):
    return json_response(200, {"status": "ok", "service": "shortlistme-api"})


def roles_handler(event, context, params):
    return json_response(200, {"roles": list_roles()})
