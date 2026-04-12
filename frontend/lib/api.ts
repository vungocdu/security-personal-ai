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
  DocumentCollection,
  DocumentUploadAcceptedResponse,
  DocumentVersionCollection,
  PreviewResource,
  QueryRequest,
  QueryResponse,
  SearchRequest,
  SearchResponse,
} from "@/lib/types";
import { getFirebaseIdToken } from "@/lib/firebase";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL?.trim();

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
};
