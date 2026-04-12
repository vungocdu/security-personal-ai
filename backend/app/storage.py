from __future__ import annotations

from dataclasses import dataclass

from firebase_admin import storage as firebase_storage
from fastapi import UploadFile

from app.config import AppConfig, load_config
from app.firebase import firebase_app


class StorageConfigError(RuntimeError):
    pass


def _resolve_bucket_name(config: AppConfig) -> str:
    if config.firebase_storage_bucket:
        return config.firebase_storage_bucket
    if config.firebase_project_id:
        return f"{config.firebase_project_id}.firebasestorage.app"
    raise StorageConfigError("Missing FIREBASE_STORAGE_BUCKET or FIREBASE_PROJECT_ID.")


def _object_path(*, document_id: str, document_version_id: str, filename: str) -> str:
    sanitized = filename.strip().replace("/", "_") or "uploaded-document"
    return f"documents/{document_id}/versions/{document_version_id}/source/{sanitized}"


@dataclass(slots=True)
class StoredObject:
    bucket: str
    object_path: str

    @property
    def gs_uri(self) -> str:
        return f"gs://{self.bucket}/{self.object_path}"


def store_uploaded_source(
    *,
    upload: UploadFile,
    document_id: str,
    document_version_id: str,
    config: AppConfig | None = None,
) -> StoredObject | None:
    settings = config or load_config()

    # In fixture mode we keep the behavior fast and offline.
    if not settings.auth_enforce:
        return None

    bucket_name = _resolve_bucket_name(settings)
    bucket = firebase_storage.bucket(name=bucket_name, app=firebase_app())

    path = _object_path(
        document_id=document_id,
        document_version_id=document_version_id,
        filename=upload.filename or "uploaded-document",
    )
    blob = bucket.blob(path)
    blob.metadata = {
        "document_id": document_id,
        "document_version_id": document_version_id,
    }

    # UploadFile.file is a file-like object; upload streaming avoids loading full content to memory.
    upload.file.seek(0)
    blob.upload_from_file(
        upload.file,
        content_type=upload.content_type or "application/octet-stream",
        rewind=True,
    )
    return StoredObject(bucket=bucket.name, object_path=path)

