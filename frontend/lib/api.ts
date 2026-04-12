import {
  fixtureCitations,
  fixtureDocuments,
  fixturePreview,
  fixtureQueryResponse,
  fixtureSearchResponse,
  fixtureVersions,
} from "@/lib/fixtures";
import type {
  AuthMeResponse,
  CitationResource,
  CreateFolderResponse,
  DocumentCollection,
  DocumentUploadAcceptedResponse,
  DocumentVersionCollection,
  PreviewResource,
  QueryRequest,
  QueryResponse,
  RepositoryListingResponse,
  SearchRequest,
  SearchResponse,
  UploadRepositoryFileResponse,
} from "@/lib/types";
import { getFirebaseIdToken } from "@/lib/firebase";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL?.trim();

type FixtureRepositoryStore = Record<string, RepositoryListingResponse>;

// Fixture-mode repository store so the explorer UI can behave like a real object store
// without requiring Firebase/Qdrant connectivity during local/dev/test.
const fixtureRepositoryStore: FixtureRepositoryStore = {
  "": {
    path: "",
    folders: [
      { name: "Reports", path: "Reports" },
      { name: "Models", path: "Models" },
    ],
    files: [
      {
        name: "readme.txt",
        path: "readme.txt",
        size_bytes: 128,
        content_type: "text/plain",
        updated_at: null,
      },
    ],
  },
  Reports: {
    path: "Reports",
    folders: [{ name: "2026", path: "Reports/2026" }],
    files: [],
  },
  Models: {
    path: "Models",
    folders: [],
    files: [{ name: "DCF.xlsx", path: "Models/DCF.xlsx", size_bytes: 24_576, content_type: "application/vnd.ms-excel", updated_at: null }],
  },
  "Reports/2026": {
    path: "Reports/2026",
    folders: [],
    files: [],
  },
};

function fixtureGetListing(path: string): RepositoryListingResponse {
  const listing = fixtureRepositoryStore[path];
  if (listing) {
    // Return a shallow clone to prevent accidental caller mutation.
    return { ...listing, folders: [...listing.folders], files: [...listing.files] };
  }
  const created: RepositoryListingResponse = { path, folders: [], files: [] };
  fixtureRepositoryStore[path] = created;
  return { ...created, folders: [], files: [] };
}

function fixtureParentPath(path: string): string {
  const trimmed = path.replace(/\/+$/, "");
  const parts = trimmed.split("/").filter(Boolean);
  if (parts.length <= 1) {
    return "";
  }
  return parts.slice(0, -1).join("/");
}

export class ApiClientError extends Error {
  constructor(
    message: string,
    public readonly status: number,
    public readonly code?: string,
  ) {
    super(message);
    this.name = "ApiClientError";
  }
}

function parseApiError(payload: unknown): { code?: string; message: string } | null {
  if (!payload || typeof payload !== "object") {
    return null;
  }
  const maybeError = (payload as { error?: { code?: string; message?: string } }).error;
  if (!maybeError || typeof maybeError !== "object") {
    return null;
  }
  const message = typeof maybeError.message === "string" ? maybeError.message : "Request failed.";
  const code = typeof maybeError.code === "string" ? maybeError.code : undefined;
  return { code, message };
}

async function jsonFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const authHeader = await buildAuthorizationHeader();
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(authHeader ? { Authorization: authHeader } : {}),
      ...(init?.headers ?? {}),
    },
  });
  if (!response.ok) {
    const payload = (await response.json().catch(() => null)) as unknown;
    const parsed = parseApiError(payload);
    throw new ApiClientError(parsed?.message ?? `Request failed: ${response.status}`, response.status, parsed?.code);
  }
  return (await response.json()) as T;
}

async function buildAuthorizationHeader(): Promise<string | null> {
  if (!API_BASE_URL) {
    return null;
  }
  const token = await getFirebaseIdToken();
  return token ? `Bearer ${token}` : null;
}

export const workspaceApi = {
  async getMe(): Promise<AuthMeResponse> {
    if (!API_BASE_URL) {
      return { uid: "fixture-user", email: "fixture@example.com", name: "Fixture User" };
    }
    return jsonFetch<AuthMeResponse>("/api/v1/auth/me");
  },

  async listDocuments(): Promise<DocumentCollection> {
    if (!API_BASE_URL) {
      return fixtureDocuments;
    }
    return jsonFetch<DocumentCollection>("/api/v1/documents?page=1&limit=20");
  },

  async listVersions(documentId: string): Promise<DocumentVersionCollection> {
    if (!API_BASE_URL) {
      return fixtureVersions[documentId] ?? { document_id: documentId, data: [] };
    }
    return jsonFetch<DocumentVersionCollection>(`/api/v1/documents/${documentId}/versions`);
  },

  async executeQuery(payload: QueryRequest): Promise<QueryResponse> {
    if (!API_BASE_URL) {
      if (payload.filters?.ticker?.[0] === "SSI") {
        return {
          ...fixtureQueryResponse,
          query: payload.query,
          citations: [fixtureCitations.cit_ssi_covenant_003],
        };
      }
      return { ...fixtureQueryResponse, query: payload.query };
    }
    return jsonFetch<QueryResponse>("/api/v1/query", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  },

  async search(payload: SearchRequest): Promise<SearchResponse> {
    if (!API_BASE_URL) {
      return { ...fixtureSearchResponse, query: payload.query };
    }
    return jsonFetch<SearchResponse>("/api/v1/search", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  },

  async getCitation(citationId: string): Promise<CitationResource> {
    if (!API_BASE_URL) {
      return fixtureCitations[citationId];
    }
    return jsonFetch<CitationResource>(`/api/v1/citations/${citationId}`);
  },

  async getPreview(documentId: string, versionId: string, pageNumber: number): Promise<PreviewResource> {
    if (!API_BASE_URL) {
      return fixturePreview(documentId, versionId, pageNumber);
    }
    return jsonFetch<PreviewResource>(`/api/v1/documents/${documentId}/versions/${versionId}/preview/${pageNumber}`);
  },

  async uploadDocument(file: File, documentId?: string): Promise<DocumentUploadAcceptedResponse> {
    if (!API_BASE_URL) {
      return {
        document_id: documentId ?? "doc_uploaded_fixture",
        document_version_id: documentId ? `${documentId.replace("doc_", "docver_")}_v99` : "docver_uploaded_fixture_v1",
        index_job_id: "job_fixture_001",
        status: "accepted",
      };
    }

    const form = new FormData();
    form.append("file", file);
    if (documentId) {
      form.append("document_id", documentId);
    }
    const authHeader = await buildAuthorizationHeader();
    const response = await fetch(`${API_BASE_URL}/api/v1/documents`, {
      method: "POST",
      body: form,
      headers: authHeader ? { Authorization: authHeader } : undefined,
    });
    if (!response.ok) {
      const payload = (await response.json().catch(() => null)) as unknown;
      const parsed = parseApiError(payload);
      throw new ApiClientError(parsed?.message ?? `Upload failed: ${response.status}`, response.status, parsed?.code);
    }
    return (await response.json()) as DocumentUploadAcceptedResponse;
  },

  async listRepository(path?: string): Promise<RepositoryListingResponse> {
    if (!API_BASE_URL) {
      return fixtureGetListing(path ?? "");
    }
    const query = path ? `?path=${encodeURIComponent(path)}` : "";
    return jsonFetch<RepositoryListingResponse>(`/api/v1/repository${query}`);
  },

  async createFolder(path: string): Promise<CreateFolderResponse> {
    if (!API_BASE_URL) {
      const folderName = path.split("/").pop() ?? path;
      const parent = fixtureParentPath(path);
      const parentListing = fixtureGetListing(parent);
      if (!parentListing.folders.some((item) => item.path === path)) {
        parentListing.folders.push({ name: folderName, path });
        parentListing.folders.sort((a, b) => a.name.localeCompare(b.name));
        fixtureRepositoryStore[parent] = parentListing;
      }
      fixtureGetListing(path);
      return { folder: { name: folderName, path } };
    }
    const response = await jsonFetch<{ folder: { name: string; path: string } }>(`/api/v1/repository/folders`, {
      method: "POST",
      body: JSON.stringify({ path }),
    });
    return response;
  },

  async uploadRepositoryFile(file: File, folderPath?: string): Promise<UploadRepositoryFileResponse> {
    if (!API_BASE_URL) {
      const listingPath = folderPath ?? "";
      const listing = fixtureGetListing(listingPath);
      const storedPath = folderPath ? `${folderPath}/${file.name}` : file.name;
      if (!listing.files.some((item) => item.path === storedPath)) {
        listing.files.push({ name: file.name, path: storedPath, size_bytes: file.size, content_type: file.type });
        listing.files.sort((a, b) => a.name.localeCompare(b.name));
        fixtureRepositoryStore[listingPath] = listing;
      }
      return { file: { name: file.name, path: storedPath, size_bytes: file.size, content_type: file.type } };
    }

    const form = new FormData();
    form.append("file", file);
    if (folderPath) {
      form.append("folder_path", folderPath);
    }
    const authHeader = await buildAuthorizationHeader();
    const response = await fetch(`${API_BASE_URL}/api/v1/repository/files`, {
      method: "POST",
      body: form,
      headers: authHeader ? { Authorization: authHeader } : undefined,
    });
    if (!response.ok) {
      const payload = (await response.json().catch(() => null)) as unknown;
      const parsed = parseApiError(payload);
      throw new ApiClientError(parsed?.message ?? `Upload failed: ${response.status}`, response.status, parsed?.code);
    }
    return (await response.json()) as UploadRepositoryFileResponse;
  },
};
