from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from firebase_admin import storage as firebase_storage
from fastapi import UploadFile

from app.config import AppConfig, load_config
from app.firebase import firebase_app


class RepositoryConfigError(RuntimeError):
    pass


def _resolve_bucket_name(config: AppConfig) -> str:
    if not config.firebase_storage_bucket:
        raise RepositoryConfigError("Missing FIREBASE_STORAGE_BUCKET.")
    return config.firebase_storage_bucket


def _normalize_repo_path(raw: str | None) -> str:
    if not raw:
        return ""
    candidate = raw.strip().replace("\\", "/").strip("/")
    if not candidate:
        return ""
    parts: list[str] = []
    for segment in candidate.split("/"):
        seg = segment.strip()
        if not seg or seg in {".", ".."}:
            continue
        # Conservative sanitization to avoid confusing object keys.
        seg = "".join(ch for ch in seg if ch.isalnum() or ch in {" ", "_", "-", "."}).strip()
        if seg:
            parts.append(seg)
    return "/".join(parts)


def _sanitize_filename(raw: str | None) -> str:
    if not raw:
        return "uploaded-file"
    name = raw.strip().replace("\\", "/").split("/")[-1]
    name = "".join(ch for ch in name if ch.isalnum() or ch in {" ", "_", "-", "."}).strip()
    return name or "uploaded-file"


def _now() -> datetime:
    return datetime.now(tz=timezone.utc)


@dataclass(frozen=True, slots=True)
class RepositoryFolder:
    name: str
    path: str


@dataclass(frozen=True, slots=True)
class RepositoryFile:
    name: str
    path: str
    size_bytes: int | None
    content_type: str | None
    updated_at: datetime | None


@dataclass(frozen=True, slots=True)
class RepositoryListing:
    path: str
    folders: list[RepositoryFolder]
    files: list[RepositoryFile]


def list_repository(*, uid: str, path: str | None, config: AppConfig | None = None) -> RepositoryListing:
    settings = config or load_config()
    normalized = _normalize_repo_path(path)

    # Fixture mode keeps the UI usable offline.
    if not settings.auth_enforce:
        return RepositoryListing(path=normalized, folders=[], files=[])

    bucket_name = _resolve_bucket_name(settings)
    bucket = firebase_storage.bucket(name=bucket_name, app=firebase_app())

    root_prefix = f"users/{uid}/repo/"
    full_prefix = root_prefix + (normalized + "/" if normalized else "")

    iterator = bucket.list_blobs(prefix=full_prefix, delimiter="/")

    folders: list[RepositoryFolder] = []
    files: list[RepositoryFile] = []

    for page in iterator.pages:
        for subprefix in getattr(page, "prefixes", set()) or set():
            rel = subprefix[len(root_prefix) :].rstrip("/")
            if not rel:
                continue
            name = rel.split("/")[-1]
            folders.append(RepositoryFolder(name=name, path=rel))

        for blob in page:
            if not blob.name.startswith(root_prefix):
                continue
            if blob.name.endswith("/"):
                continue
            if blob.name.endswith("/.keep"):
                continue
            rel = blob.name[len(root_prefix) :]
            if "/" in rel.strip("/") and normalized == "":
                # Should not happen when delimiter is set, but keep defensive.
                pass
            name = rel.split("/")[-1]
            updated = blob.updated if getattr(blob, "updated", None) else None
            files.append(
                RepositoryFile(
                    name=name,
                    path=rel,
                    size_bytes=int(blob.size) if getattr(blob, "size", None) is not None else None,
                    content_type=getattr(blob, "content_type", None),
                    updated_at=updated,
                )
            )

    folders.sort(key=lambda item: item.name.lower())
    files.sort(key=lambda item: item.name.lower())
    return RepositoryListing(path=normalized, folders=folders, files=files)


def create_folder(*, uid: str, path: str, config: AppConfig | None = None) -> RepositoryFolder:
    settings = config or load_config()
    normalized = _normalize_repo_path(path)
    if not normalized:
        raise ValueError("Folder path is required.")

    if not settings.auth_enforce:
        return RepositoryFolder(name=normalized.split("/")[-1], path=normalized)

    bucket_name = _resolve_bucket_name(settings)
    bucket = firebase_storage.bucket(name=bucket_name, app=firebase_app())
    root_prefix = f"users/{uid}/repo/"

    placeholder = f"{root_prefix}{normalized}/.keep"
    blob = bucket.blob(placeholder)
    blob.metadata = {"kind": "folder", "uid": uid, "created_at": _now().isoformat()}
    blob.upload_from_string(b"", content_type="application/x-directory")

    return RepositoryFolder(name=normalized.split("/")[-1], path=normalized)


def upload_file(
    *,
    uid: str,
    folder_path: str | None,
    upload: UploadFile,
    config: AppConfig | None = None,
) -> RepositoryFile:
    settings = config or load_config()
    normalized_folder = _normalize_repo_path(folder_path)
    filename = _sanitize_filename(upload.filename)

    stored_rel = f"{normalized_folder}/{filename}" if normalized_folder else filename

    if not settings.auth_enforce:
        return RepositoryFile(name=filename, path=stored_rel, size_bytes=None, content_type=upload.content_type, updated_at=_now())

    bucket_name = _resolve_bucket_name(settings)
    bucket = firebase_storage.bucket(name=bucket_name, app=firebase_app())
    root_prefix = f"users/{uid}/repo/"
    blob = bucket.blob(f"{root_prefix}{stored_rel}")
    blob.metadata = {"uid": uid, "folder_path": normalized_folder or "", "original_filename": filename}

    upload.file.seek(0)
    blob.upload_from_file(
        upload.file,
        content_type=upload.content_type or "application/octet-stream",
        rewind=True,
    )

    updated = blob.updated if getattr(blob, "updated", None) else _now()
    return RepositoryFile(
        name=filename,
        path=stored_rel,
        size_bytes=int(blob.size) if getattr(blob, "size", None) is not None else None,
        content_type=getattr(blob, "content_type", None),
        updated_at=updated,
    )
