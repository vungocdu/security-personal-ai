import type {
  CitationResource,
  DocumentCollection,
  DocumentVersionCollection,
  EvidenceItem,
  PreviewResource,
  RepositoryNode,
} from "@/lib/types";

export function mapDocumentsToTree(documents: DocumentCollection, versionsMap: Record<string, DocumentVersionCollection | undefined>): RepositoryNode[] {
  const bySource = new Map<string, Map<string, RepositoryNode[]>>();

  for (const document of documents.data) {
    const sourceMap = bySource.get(document.source) ?? new Map<string, RepositoryNode[]>();
    const tickerKey = document.ticker ?? "UNASSIGNED";
    const tickerNodes = sourceMap.get(tickerKey) ?? [];
    const currentVersion = versionsMap[document.document_id]?.data.find((item) => item.is_current_version);
    tickerNodes.push({
      id: document.document_id,
      label: document.title,
      type: "document",
      meta: {
        status: document.index_status,
        version: currentVersion?.version_label ?? "v?",
        documentType: document.document_type,
      },
    });
    sourceMap.set(tickerKey, tickerNodes);
    bySource.set(document.source, sourceMap);
  }

  return Array.from(bySource.entries()).map(([source, tickerMap]) => ({
    id: source,
    label: source.replaceAll("_", " "),
    type: "source",
    children: Array.from(tickerMap.entries()).map(([ticker, children]) => ({
      id: `${source}-${ticker}`,
      label: ticker,
      type: "ticker",
      children,
    })),
  }));
}

export function mapCitationToEvidenceItem(citation: CitationResource, preview: PreviewResource | null): EvidenceItem {
  return {
    id: citation.citation_id,
    title: citation.title,
    subtitle: `${citation.source} • ${citation.section_heading ?? "No section"} • ${citation.version_label}`,
    snippet: citation.snippet,
    pageLabel: citation.page_number ? `Trang ${citation.page_number}` : "No page",
    preview,
    citation,
  };
}
