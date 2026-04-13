from __future__ import annotations

import json
from functools import lru_cache

import firebase_admin
from firebase_admin import credentials

from app.config import AppConfig, load_config


def _build_firebase_credential(config: AppConfig):
    if config.firebase_service_account_json:
        service_account_info = json.loads(config.firebase_service_account_json)
        return credentials.Certificate(service_account_info)
    if config.firebase_service_account_path:
        return credentials.Certificate(config.firebase_service_account_path)
    return credentials.ApplicationDefault()


@lru_cache(maxsize=1)
def firebase_app() -> firebase_admin.App:
    config = load_config()
    options = {"projectId": config.firebase_project_id} if config.firebase_project_id else None
    credential = _build_firebase_credential(config)
    try:
        return firebase_admin.get_app()
    except ValueError:
        return firebase_admin.initialize_app(credential=credential, options=options)

