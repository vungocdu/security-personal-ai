import type {
  CitationResource,
  DocumentCollection,
  DocumentVersionCollection,
  PreviewResource,
  QueryResponse,
  SearchResponse,
} from "@/lib/types";

export const fixtureDocuments: DocumentCollection = {
  page: 1,
  limit: 20,
  total: 3,
  data: [
    {
      document_id: "doc_hpg_ar_2024",
      title: "HPG Annual Report 2024",
      document_type: "annual_report",
      ticker: "HPG",
      source: "internal_repository",
      language: "vi",
      publication_date: "2025-03-29",
      current_version_id: "docver_hpg_ar_2024_v1",
      access_level: "internal",
      index_status: "indexed",
    },
    {
      document_id: "doc_ssi_research_2024q4",
      title: "SSI Research Report Q4 2024",
      document_type: "research_report",
      ticker: "SSI",
      source: "broker_feed",
      language: "en",
      publication_date: "2024-12-18",
      current_version_id: "docver_ssi_research_2024q4_v2",
      access_level: "licensed",
      index_status: "indexed",
    },
    {
      document_id: "doc_fpt_fin_2024q4",
      title: "FPT Financial Statement Q4 2024",
      document_type: "financial_statement",
      ticker: "FPT",
      source: "issuer_upload",
      language: "vi",
      publication_date: "2025-01-22",
      current_version_id: "docver_fpt_fin_2024q4_v1",
      access_level: "internal",
      index_status: "indexing",
    },
  ],
};

export const fixtureVersions: Record<string, DocumentVersionCollection> = {
  doc_hpg_ar_2024: {
    document_id: "doc_hpg_ar_2024",
    data: [
      {
        document_id: "doc_hpg_ar_2024",
        document_version_id: "docver_hpg_ar_2024_v1",
        version_label: "v1",
        is_current_version: true,
        supersedes_version_id: null,
        publication_date: "2025-03-29",
        parse_status: "indexed",
      },
    ],
  },
  doc_ssi_research_2024q4: {
    document_id: "doc_ssi_research_2024q4",
    data: [
      {
        document_id: "doc_ssi_research_2024q4",
        document_version_id: "docver_ssi_research_2024q4_v1",
        version_label: "v1",
        is_current_version: false,
        supersedes_version_id: null,
        publication_date: "2024-12-10",
        parse_status: "superseded",
      },
      {
        document_id: "doc_ssi_research_2024q4",
        document_version_id: "docver_ssi_research_2024q4_v2",
        version_label: "v2",
        is_current_version: true,
        supersedes_version_id: "docver_ssi_research_2024q4_v1",
        publication_date: "2024-12-18",
        parse_status: "indexed",
      },
    ],
  },
};

export const fixtureCitations: Record<string, CitationResource> = {
  cit_hpg_risk_001: {
    citation_id: "cit_hpg_risk_001",
    document_id: "doc_hpg_ar_2024",
    document_version_id: "docver_hpg_ar_2024_v1",
    title: "HPG Annual Report 2024",
    source: "internal_repository",
    document_type: "annual_report",
    page_number: 87,
    section_heading: "Risk Factors",
    chunk_id: "chk_hpg_009182",
    snippet: "Biến động giá quặng sắt và than cốc có thể ảnh hưởng đáng kể đến biên lợi nhuận gộp.",
    preview_url: "/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/87",
    viewer_anchor: "page=87&chunk=chk_hpg_009182",
    version_label: "v1",
    confidence: 0.91,
  },
  cit_hpg_cashflow_002: {
    citation_id: "cit_hpg_cashflow_002",
    document_id: "doc_hpg_ar_2024",
    document_version_id: "docver_hpg_ar_2024_v1",
    title: "HPG Annual Report 2024",
    source: "internal_repository",
    document_type: "annual_report",
    page_number: 104,
    section_heading: "Capital Expenditure",
    chunk_id: "chk_hpg_009399",
    snippet: "Áp lực dòng tiền đến từ chu kỳ đầu tư lớn và nhu cầu vốn lưu động tăng theo sản lượng.",
    preview_url: "/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/104",
    viewer_anchor: "page=104&chunk=chk_hpg_009399",
    version_label: "v1",
    confidence: 0.88,
  },
  cit_ssi_covenant_003: {
    citation_id: "cit_ssi_covenant_003",
    document_id: "doc_ssi_research_2024q4",
    document_version_id: "docver_ssi_research_2024q4_v2",
    title: "SSI Research Report Q4 2024",
    source: "broker_feed",
    document_type: "research_report",
    page_number: 12,
    section_heading: "Balance Sheet Pressure",
    chunk_id: "chk_ssi_1102",
    snippet: "Covenant pressure remains manageable, but margin lending exposure is rising.",
    preview_url: "/api/v1/documents/doc_ssi_research_2024q4/versions/docver_ssi_research_2024q4_v2/preview/12",
    viewer_anchor: "page=12&chunk=chk_ssi_1102",
    version_label: "v2",
    confidence: 0.86,
  },
};

export const fixtureQueryResponse: QueryResponse = {
  request_id: "req_fixture_query_001",
  query: "Rủi ro lớn nhất của HPG trong 2024 là gì?",
  answer: {
    summary:
      "Ba nhóm rủi ro nổi bật là nhu cầu thép phục hồi chậm, biến động giá nguyên liệu, và áp lực dòng tiền từ chu kỳ đầu tư lớn.",
    confidence: "medium",
    insufficient_evidence: false,
    disclaimer: "Không coi đây là khuyến nghị đầu tư.",
  },
  citations: [fixtureCitations.cit_hpg_risk_001, fixtureCitations.cit_hpg_cashflow_002],
};

export const fixtureSearchResponse: SearchResponse = {
  request_id: "req_fixture_search_001",
  query: "covenant impairment",
  page: 1,
  limit: 20,
  total: 2,
  results: [
    {
      result_type: "chunk",
      document_id: "doc_ssi_research_2024q4",
      document_version_id: "docver_ssi_research_2024q4_v2",
      title: "SSI Research Report Q4 2024",
      document_type: "research_report",
      ticker: "SSI",
      publication_date: "2024-12-18",
      page_number: 12,
      section_heading: "Balance Sheet Pressure",
      chunk_id: "chk_ssi_1102",
      snippet: "Covenant pressure remains manageable, but margin lending exposure is rising.",
      preview_url: "/api/v1/documents/doc_ssi_research_2024q4/versions/docver_ssi_research_2024q4_v2/preview/12",
      viewer_anchor: "page=12&chunk=chk_ssi_1102",
    },
    {
      result_type: "document",
      document_id: "doc_hpg_ar_2024",
      document_version_id: "docver_hpg_ar_2024_v1",
      title: "HPG Annual Report 2024",
      document_type: "annual_report",
      ticker: "HPG",
      publication_date: "2025-03-29",
      source: "internal_repository",
      language: "vi",
      preview_url: "/api/v1/documents/doc_hpg_ar_2024/versions/docver_hpg_ar_2024_v1/preview/1",
    },
  ],
};

export function fixturePreview(documentId: string, versionId: string, pageNumber: number): PreviewResource {
  const mimeType =
    documentId === "doc_ssi_research_2024q4"
      ? "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
      : documentId === "doc_fpt_fin_2024q4"
        ? "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        : "application/pdf";

  return {
    document_id: documentId,
    document_version_id: versionId,
    page_number: pageNumber,
    mime_type: mimeType,
    preview_url: `https://signed.example.com/preview/${documentId}/${versionId}/page/${pageNumber}`,
    viewer_anchor: `page=${pageNumber}`,
    expires_at: "2026-04-12T11:30:00Z",
  };
}
