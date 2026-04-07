from dataclasses import dataclass
from typing import Callable, Dict, Optional

from utils.auth import get_user_id
from utils.response import json_response


@dataclass
class Route:
    method: str
    path: str
    handler: Callable
    protected: bool


class Router:
    def __init__(self):
        self.routes = []

    def add(self, method: str, path: str, handler: Callable, protected: bool = False):
        self.routes.append(Route(method=method, path=path, handler=handler, protected=protected))

    def dispatch(self, event: dict, context: dict):
        method = event.get("requestContext", {}).get("http", {}).get("method", "")
        raw_path = event.get("requestContext", {}).get("http", {}).get("path", "")

        if method == "OPTIONS":
            return json_response(200, {"ok": True})

        for route in self.routes:
            params = self._match(route.path, raw_path)
            if route.method == method and params is not None:
                if route.protected:
                    user_id = get_user_id(event)
                    if user_id == "anonymous":
                        return json_response(401, {"error": "Unauthorized"})
                return route.handler(event, context, params)
        return json_response(404, {"error": "NotFound"})

    def _match(self, template: str, actual: str) -> Optional[Dict[str, str]]:
        t_parts = [p for p in template.split("/") if p]
        a_parts = [p for p in actual.split("/") if p]
        if len(t_parts) != len(a_parts):
            return None

        params = {}
        for t, a in zip(t_parts, a_parts):
            if t.startswith("{") and t.endswith("}"):
                params[t[1:-1]] = a
            elif t != a:
                return None
        return params
