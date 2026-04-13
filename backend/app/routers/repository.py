from __future__ import annotations

from fastapi import APIRouter, Depends, File, Form, UploadFile, status

from app.auth import AuthenticatedUser, require_authenticated_user
from app.schemas import (
    CreateFolderRequest,
    CreateFolderResponse,
    RepositoryListingResponse,
    RepositoryFileResource,
    RepositoryFolderResource,
    UploadRepositoryFileResponse,
)
from app.services import RepositoryService


router = APIRouter(prefix="/api/v1/repository", tags=["Repository"])
service = RepositoryService()


@router.get("", response_model=RepositoryListingResponse, summary="List repository nodes under a folder path")
async def list_repository(path: str | None = None, user: AuthenticatedUser = Depends(require_authenticated_user)) -> RepositoryListingResponse:
    listing = service.list(uid=user.uid, path=path)
    return RepositoryListingResponse(
        path=listing.path,
        folders=[RepositoryFolderResource(name=item.name, path=item.path) for item in listing.folders],
        files=[
            RepositoryFileResource(
                name=item.name,
                path=item.path,
                size_bytes=item.size_bytes,
                content_type=item.content_type,
                updated_at=item.updated_at,
            )
            for item in listing.files
        ],
    )


@router.post(
    "/folders",
    response_model=CreateFolderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a folder in repository (creates a placeholder object)",
)
async def create_folder(payload: CreateFolderRequest, user: AuthenticatedUser = Depends(require_authenticated_user)) -> CreateFolderResponse:
    folder = service.create_folder(uid=user.uid, path=payload.path)
    return CreateFolderResponse(folder=RepositoryFolderResource(name=folder.name, path=folder.path))


@router.post(
    "/files",
    response_model=UploadRepositoryFileResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload a file into a repository folder",
)
async def upload_repository_file(
    file: UploadFile = File(...),
    folder_path: str | None = Form(default=None),
    user: AuthenticatedUser = Depends(require_authenticated_user),
) -> UploadRepositoryFileResponse:
    stored = service.upload(uid=user.uid, folder_path=folder_path, upload=file)
    return UploadRepositoryFileResponse(
        file=RepositoryFileResource(
            name=stored.name,
            path=stored.path,
            size_bytes=stored.size_bytes,
            content_type=stored.content_type,
            updated_at=stored.updated_at,
        )
    )
