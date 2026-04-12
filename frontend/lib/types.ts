export type DocumentType =
  | "annual_report"
  | "financial_statement"
  | "research_report"
  | "legal_document"
  | "disclosure"
  | "internal_note";

export type IndexStatus = "accepted" | "indexing" | "indexed" | "failed" | "superseded";
export type ParseStatus = IndexStatus | "withdrawn" | "invalidated";
export type ResultType = "chunk" | "document";

export interface FilterObject {
  ticker?: string[];
  document_type?: DocumentType[];
  source?: string[];
  language?: string[];
  date_from?: string;
  date_to?: string;
  reporting_period?: string[];
  sector?: string[];
  market?: string[];
}

export interface QueryRequest {
  query: string;
  filters?: FilterObject;
  options?: {
    include_debug?: boolean;
    max_citations?: number;
  };
}

export interface AnswerObject {
  summary: string;
  confidence: "low" | "medium" | "high";
  insufficient_evidence: boolean;
  disclaimer?: string;
}

export interface CitationResource {
  citation_id: string;
  document_id: string;
  document_version_id: string;
  title: string;
  source: string;
  document_type: DocumentType;
  page_number?: number;
  section_heading?: string;
  chunk_id: string;
  snippet: string;
  text_offset_start?: number;
  text_offset_end?: number;
  preview_url?: string;
  viewer_anchor?: string;
  version_label: string;
  confidence?: number;
}

export interface QueryResponse {
  request_id: string;
  query: string;
  filters?: FilterObject;
  answer: AnswerObject;
  citations: CitationResource[];
}

export interface SearchRequest {
  query: string;
  filters?: FilterObject;
  page?: number;
  limit?: number;
}

export interface SearchResult {
  result_type: ResultType;
  document_id: string;
  document_version_id: string;
  title: string;
  document_type: DocumentType;
  ticker?: string;
  publication_date?: string;
  page_number?: number;
  section_heading?: string;
  chunk_id?: string;
  snippet?: string;
  preview_url?: string;
  viewer_anchor?: string;
  source?: string;
  language?: string;
}

export interface SearchResponse {
  request_id: string;
  query: string;
  page: number;
  limit: number;
  total: number;
  results: SearchResult[];
}

export interface DocumentResource {
  document_id: string;
  title: string;
  document_type: DocumentType;
  ticker?: string;
  source: string;
  language: string;
  publication_date: string;
  current_version_id: string;
  access_level: string;
  index_status: IndexStatus;
}

export interface DocumentCollection {
  page: number;
  limit: number;
  total: number;
  data: DocumentResource[];
}

export interface DocumentVersionResource {
  document_id: string;
  document_version_id: string;
  version_label: string;
  is_current_version: boolean;
  supersedes_version_id?: string | null;
  publication_date: string;
  parse_status: ParseStatus;
}

export interface DocumentVersionCollection {
  document_id: string;
  data: DocumentVersionResource[];
}

export interface PreviewResource {
  document_id: string;
  document_version_id: string;
  page_number: number;
  mime_type: string;
  preview_url: string;
  viewer_anchor?: string;
  expires_at: string;
}

export interface DocumentUploadAcceptedResponse {
  document_id: string;
  document_version_id: string;
  index_job_id: string;
  status: "accepted";
}

export interface AuthMeResponse {
  uid: string;
  email?: string | null;
  name?: string | null;
}

export interface RepositoryNode {
  id: string;
  label: string;
  type: "source" | "ticker" | "document";
  children?: RepositoryNode[];
  meta?: {
    status?: string;
    version?: string;
    documentType?: string;
  };
}

export interface EvidenceItem {
  id: string;
  title: string;
  subtitle: string;
  snippet: string;
  pageLabel: string;
  preview?: PreviewResource | null;
  citation: CitationResource;
}
