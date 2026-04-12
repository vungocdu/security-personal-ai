import {
  fixtureCitations,
  fixtureDocuments,
  fixturePreview,
  fixtureQueryResponse,
  fixtureSearchResponse,
  fixtureVersions,
} from "@/lib/fixtures";
import type {
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

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL?.trim();

async function jsonFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
  });
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return (await response.json()) as T;
}

export const workspaceApi = {
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

  async uploadDocument(file: File): Promise<DocumentUploadAcceptedResponse> {
    if (!API_BASE_URL) {
      return {
        document_id: "doc_uploaded_fixture",
        document_version_id: "docver_uploaded_fixture_v1",
        index_job_id: "job_fixture_001",
        status: "accepted",
      };
    }

    const form = new FormData();
    form.append("file", file);
    const response = await fetch(`${API_BASE_URL}/api/v1/documents`, {
      method: "POST",
      body: form,
    });
    if (!response.ok) {
      throw new Error(`Upload failed: ${response.status}`);
    }
    return (await response.json()) as DocumentUploadAcceptedResponse;
  },
};
