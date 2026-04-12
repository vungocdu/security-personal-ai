"use client";

import { FileSpreadsheet, FileText, FolderTree, Mic, PanelLeft, PanelRight, Search, Send, UploadCloud } from "lucide-react";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";

import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Textarea } from "@/components/ui/textarea";
import { workspaceApi } from "@/lib/api";
import { mapCitationToEvidenceItem, mapDocumentsToTree } from "@/lib/mappers";
import type {
  CitationResource,
  DocumentCollection,
  DocumentVersionCollection,
  EvidenceItem,
  QueryResponse,
} from "@/lib/types";
import { cn } from "@/lib/utils";

type PanelView = "desktop" | "left" | "right";

const FILTER_SUMMARY = ["Ticker", "Document type", "Time window", "Source"];

export function AnalystWorkspace() {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [documents, setDocuments] = useState<DocumentCollection | null>(null);
  const [versionsMap, setVersionsMap] = useState<Record<string, DocumentVersionCollection | undefined>>({});
  const [queryText, setQueryText] = useState("Rủi ro lớn nhất của HPG trong 2024 là gì?");
  const [activeResponse, setActiveResponse] = useState<QueryResponse | null>(null);
  const [activeEvidence, setActiveEvidence] = useState<EvidenceItem | null>(null);
  const [loading, setLoading] = useState(true);
  const [queryLoading, setQueryLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [uploadStatus, setUploadStatus] = useState<string>("No uploads in this session");
  const [selectedDocumentId, setSelectedDocumentId] = useState<string | null>(null);
  const [voiceDraft, setVoiceDraft] = useState<string | null>(null);
  const [panelView, setPanelView] = useState<PanelView>("desktop");

  const refreshRepository = useCallback(async () => {
    const collection = await workspaceApi.listDocuments();
    setDocuments(collection);
    const versions = await Promise.all(collection.data.map((document) => workspaceApi.listVersions(document.document_id)));
    const mapped = versions.reduce<Record<string, DocumentVersionCollection>>((accumulator, versionCollection) => {
      accumulator[versionCollection.document_id] = versionCollection;
      return accumulator;
    }, {});
    setVersionsMap(mapped);

    setSelectedDocumentId((previous) => (previous && !collection.data.some((item) => item.document_id === previous) ? null : previous));
  }, []);

  useEffect(() => {
    async function bootstrap() {
      try {
        await refreshRepository();
      } catch (caught) {
        setError(caught instanceof Error ? caught.message : "Failed to load documents.");
      } finally {
        setLoading(false);
      }
    }

    void bootstrap();
  }, [refreshRepository]);

  const tree = useMemo(() => (documents ? mapDocumentsToTree(documents, versionsMap) : []), [documents, versionsMap]);
  const selectedDocumentLabel = useMemo(() => {
    if (!documents || !selectedDocumentId) {
      return null;
    }
    return documents.data.find((item) => item.document_id === selectedDocumentId)?.title ?? null;
  }, [documents, selectedDocumentId]);

  async function handleSubmit() {
    setQueryLoading(true);
    setError(null);
    try {
      const response = await workspaceApi.executeQuery({
        query: queryText,
        filters: { ticker: ["HPG"], document_type: ["annual_report", "research_report"] },
        options: { max_citations: 8 },
      });
      setActiveResponse(response);
      const firstCitation = response.citations[0];
      if (firstCitation) {
        await selectCitation(firstCitation);
      }
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Query failed.");
    } finally {
      setQueryLoading(false);
    }
  }

  async function selectCitation(citation: CitationResource) {
    const preview = citation.page_number
      ? await workspaceApi.getPreview(citation.document_id, citation.document_version_id, citation.page_number)
      : null;
    setActiveEvidence(mapCitationToEvidenceItem(citation, preview));
    setPanelView("right");
  }

  async function handleCitationClick(citationId: string) {
    const citation = await workspaceApi.getCitation(citationId);
    await selectCitation(citation);
  }

  async function handleUpload(files: FileList | null) {
    if (!files || files.length === 0) {
      return;
    }
    setError(null);
    try {
      const upload = await workspaceApi.uploadDocument(files[0], selectedDocumentId ?? undefined);
      const modeLabel = selectedDocumentId ? "Appended version" : "Accepted new document";
      setUploadStatus(`${modeLabel}: ${upload.document_id} -> ${upload.document_version_id}`);
      await refreshRepository();
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Upload failed.");
    }
  }

  function handleVoiceDraft() {
    const transcript = "Tổng hợp các rủi ro chính của SSI trong báo cáo gần đây";
    setVoiceDraft(transcript);
    setQueryText(transcript);
  }

  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(156,107,48,0.08),_transparent_28%),linear-gradient(180deg,_#f7f3ec_0%,_#eff2f7_100%)] p-4 text-ink md:p-6">
      <div className="mx-auto flex max-w-[1600px] flex-col gap-4">
        <header className="flex items-center justify-between rounded-3xl border border-white/60 bg-white/70 px-5 py-4 backdrop-blur">
          <div>
            <p className="text-xs uppercase tracking-[0.32em] text-slate">Security Personal AI</p>
            <h1 className="mt-1 text-2xl font-semibold">Analyst Workspace</h1>
          </div>
          <div className="flex items-center gap-2 md:hidden">
            <Button variant="secondary" size="icon" aria-label="Open left panel" onClick={() => setPanelView("left")}>
              <PanelLeft className="h-4 w-4" />
            </Button>
            <Button variant="secondary" size="icon" aria-label="Open right panel" onClick={() => setPanelView("right")}>
              <PanelRight className="h-4 w-4" />
            </Button>
          </div>
        </header>

        <div className="grid gap-4 xl:grid-cols-[300px_minmax(0,1fr)_460px]">
          <PanelShell title="Repository" icon={<FolderTree className="h-4 w-4" />} mobileOpen={panelView === "left"} onClose={() => setPanelView("desktop")} className="xl:block">
            <div className="flex items-center justify-between gap-3">
              <div>
                <p className="text-xs uppercase tracking-[0.26em] text-slate">Source map</p>
                <h2 className="mt-1 text-lg font-semibold">Document tree</h2>
              </div>
              <Button variant="accent" size="sm" onClick={() => fileInputRef.current?.click()}>
                <UploadCloud className="mr-2 h-4 w-4" />
                {selectedDocumentId ? "Upload version" : "Upload"}
              </Button>
            </div>
            <input ref={fileInputRef} className="hidden" type="file" onChange={(event) => void handleUpload(event.target.files)} />
            <div className="mt-4 rounded-2xl bg-sand p-3 text-sm text-slate">{uploadStatus}</div>
            {selectedDocumentLabel ? (
              <div className="mt-2 rounded-2xl border border-accentSoft bg-[#fff8ec] p-3 text-xs text-[#6d531d]">
                Selected target for version upload: {selectedDocumentLabel}
              </div>
            ) : null}
            <div className="mt-4 flex flex-wrap gap-2">
              <Badge>By ticker</Badge>
              <Badge variant="accent">By source</Badge>
              <Badge>By document type</Badge>
            </div>
            <Separator className="my-4" />
            <div className="space-y-4" data-testid="repository-tree">
              {loading && <div className="rounded-2xl bg-mist p-4 text-sm text-slate">Loading repository…</div>}
              {!loading &&
                tree.map((sourceNode) => (
                  <div key={sourceNode.id} className="rounded-2xl border border-line/80 bg-mist/50 p-3">
                    <p className="text-xs font-semibold uppercase tracking-[0.24em] text-slate">{sourceNode.label}</p>
                    <div className="mt-3 space-y-3">
                      {sourceNode.children?.map((tickerNode) => (
                        <div key={tickerNode.id}>
                          <p className="text-sm font-medium text-ink">{tickerNode.label}</p>
                          <div className="mt-2 space-y-2">
                            {tickerNode.children?.map((document) => (
                              <button
                                key={document.id}
                                className={cn(
                                  "w-full rounded-2xl border px-3 py-3 text-left hover:border-accentSoft hover:bg-[#fffaf3]",
                                  selectedDocumentId === document.id ? "border-accent bg-[#fff7e8]" : "border-white bg-white",
                                )}
                                type="button"
                                onClick={() => setSelectedDocumentId(document.id)}
                              >
                                <div className="flex items-start justify-between gap-3">
                                  <div>
                                    <p className="text-sm font-medium text-ink">{document.label}</p>
                                    <p className="mt-1 text-xs text-slate">{document.meta?.documentType}</p>
                                  </div>
                                  <Badge variant={document.meta?.status === "indexed" ? "success" : "warning"}>{document.meta?.status}</Badge>
                                </div>
                                <p className="mt-2 text-xs text-slate">Current {document.meta?.version}</p>
                              </button>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
            </div>
          </PanelShell>

          <PanelShell title="Query workspace" icon={<Search className="h-4 w-4" />} mobileOpen className="xl:block">
            <div className="flex flex-wrap gap-2">
              {FILTER_SUMMARY.map((item) => (
                <Badge key={item}>{item}</Badge>
              ))}
            </div>
            <Card className="mt-4 overflow-hidden bg-white/90">
              <CardHeader>
                <CardTitle>Evidence-first query thread</CardTitle>
                <CardDescription>
                  Ask in natural language, then verify each point from the right-hand evidence panel.
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                  <div className="rounded-2xl bg-ink p-4 text-sm text-white">
                    <p className="text-xs uppercase tracking-[0.24em] text-white/60">Prompt</p>
                    <p className="mt-2" data-testid="current-prompt">
                      {queryText}
                    </p>
                  </div>
                {error ? (
                  <div className="rounded-2xl border border-[#efc5c5] bg-[#fff4f4] p-4 text-sm text-[#8f3131]">{error}</div>
                ) : null}
                {activeResponse ? (
                  <div className="space-y-4" data-testid="answer-card">
                    <div className="rounded-2xl border border-line bg-sand/60 p-4">
                      <p className="text-xs uppercase tracking-[0.24em] text-slate">Conclusion</p>
                      <p className="mt-2 text-base font-medium text-ink">{activeResponse.answer.summary}</p>
                    </div>
                    <div className="rounded-2xl border border-line bg-white p-4">
                      <p className="text-xs uppercase tracking-[0.24em] text-slate">Evidence</p>
                      <div className="mt-3 flex flex-wrap gap-2">
                        {activeResponse.citations.map((citation) => (
                          <button
                            key={citation.citation_id}
                            className="rounded-full border border-line px-3 py-2 text-xs font-medium text-ink hover:border-accent hover:bg-accentSoft"
                            type="button"
                            aria-label={`Open citation ${citation.title} page ${citation.page_number ?? "na"}`}
                            onClick={() => void handleCitationClick(citation.citation_id)}
                          >
                            {citation.title} • p.{citation.page_number}
                          </button>
                        ))}
                      </div>
                    </div>
                    {activeResponse.answer.disclaimer ? (
                      <div className="text-xs text-slate">{activeResponse.answer.disclaimer}</div>
                    ) : null}
                  </div>
                ) : (
                  <div className="rounded-2xl border border-dashed border-line bg-white/60 p-6 text-sm text-slate">
                    Try prompts like “Tổng hợp các rủi ro chính của VNM trong 3 báo cáo thường niên gần nhất”.
                  </div>
                )}
              </CardContent>
            </Card>

            <Card className="mt-4 bg-white/95">
              <CardHeader>
                <CardTitle>Composer</CardTitle>
                <CardDescription>Center panel remains primary on every screen size.</CardDescription>
              </CardHeader>
              <CardContent>
                <Textarea value={queryText} onChange={(event) => setQueryText(event.target.value)} aria-label="Query input" />
                <div className="mt-3 flex flex-wrap items-center justify-between gap-3">
                  <div className="flex flex-wrap gap-2">
                    <Button variant="secondary" type="button" onClick={handleVoiceDraft}>
                      <Mic className="mr-2 h-4 w-4" />
                      Voice draft
                    </Button>
                    {voiceDraft ? <Badge variant="accent">{voiceDraft}</Badge> : null}
                  </div>
                  <Button type="button" onClick={() => void handleSubmit()} disabled={queryLoading}>
                    <Send className="mr-2 h-4 w-4" />
                    {queryLoading ? "Querying…" : "Run query"}
                  </Button>
                </div>
              </CardContent>
            </Card>
          </PanelShell>

          <PanelShell title="Evidence preview" icon={<FileText className="h-4 w-4" />} mobileOpen={panelView === "right"} onClose={() => setPanelView("desktop")} className="xl:block">
            <Card className="bg-white/92">
              <CardHeader>
                <CardTitle>Snippet stack</CardTitle>
                <CardDescription>Right panel stays tied to citations and search evidence.</CardDescription>
              </CardHeader>
              <CardContent className="space-y-3" data-testid="evidence-panel">
                {activeResponse?.citations.map((citation) => {
                  const active = activeEvidence?.id === citation.citation_id;
                  return (
                    <button
                      key={citation.citation_id}
                      className={cn(
                        "w-full rounded-2xl border px-4 py-3 text-left transition-colors",
                        active ? "border-accent bg-accentSoft" : "border-line bg-mist/40 hover:bg-white",
                      )}
                      type="button"
                      onClick={() => void handleCitationClick(citation.citation_id)}
                    >
                      <div className="flex items-center justify-between gap-3">
                        <p className="text-sm font-medium text-ink">{citation.title}</p>
                        <Badge>{citation.page_number ? `p.${citation.page_number}` : "n/a"}</Badge>
                      </div>
                      <p className="mt-2 text-xs text-slate">{citation.section_heading}</p>
                      <p className="mt-2 text-sm text-ink">{citation.snippet}</p>
                    </button>
                  );
                }) ?? (
                  <div className="rounded-2xl border border-dashed border-line bg-white/70 p-5 text-sm text-slate">
                    Select a citation to preview the source file here.
                  </div>
                )}
              </CardContent>
            </Card>

            <Card className="mt-4 min-h-[360px] bg-[#fcfcfd]">
              <CardHeader>
                <CardTitle>{activeEvidence?.title ?? "Preview viewer"}</CardTitle>
                <CardDescription>{activeEvidence?.subtitle ?? "PDF, Word, and Excel previews will appear here."}</CardDescription>
              </CardHeader>
              <CardContent data-testid="preview-panel">
                {activeEvidence ? <PreviewSurface evidence={activeEvidence} /> : <div className="rounded-2xl bg-mist p-6 text-sm text-slate">No evidence selected.</div>}
              </CardContent>
            </Card>
          </PanelShell>
        </div>
      </div>
    </div>
  );
}

function PanelShell({
  children,
  title,
  icon,
  mobileOpen = false,
  onClose,
  className,
}: {
  children: React.ReactNode;
  title: string;
  icon: React.ReactNode;
  mobileOpen?: boolean;
  onClose?: () => void;
  className?: string;
}) {
  return (
    <aside
      className={cn(
        "rounded-[28px] border border-white/70 bg-white/70 p-4 shadow-panel backdrop-blur xl:min-h-[calc(100vh-132px)]",
        mobileOpen ? "block" : "hidden xl:block",
        className,
      )}
    >
      <div className="mb-4 flex items-center justify-between">
        <div className="flex items-center gap-2 text-sm font-semibold text-ink">
          {icon}
          <span>{title}</span>
        </div>
        {onClose ? (
          <Button variant="ghost" size="sm" className="xl:hidden" type="button" onClick={onClose}>
            Close
          </Button>
        ) : null}
      </div>
      {children}
    </aside>
  );
}

function PreviewSurface({ evidence }: { evidence: EvidenceItem }) {
  const preview = evidence.preview;
  const mime = preview?.mime_type ?? "application/pdf";
  const kind = mime.includes("spreadsheet")
    ? "Excel"
    : mime.includes("wordprocessingml")
      ? "Word"
      : "PDF";

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap items-center gap-2">
        <Badge variant="accent">{kind} preview</Badge>
        <Badge>{evidence.pageLabel}</Badge>
        <Badge variant={kind === "PDF" ? "success" : "warning"}>{preview ? "Preview resolved" : "Preview unavailable"}</Badge>
      </div>
      <div className="rounded-3xl border border-line bg-white p-4">
        <div className="flex items-center gap-3">
          {kind === "Excel" ? <FileSpreadsheet className="h-5 w-5 text-accent" /> : <FileText className="h-5 w-5 text-accent" />}
          <div>
            <p className="text-sm font-semibold text-ink">{evidence.title}</p>
            <p className="text-xs text-slate">{evidence.subtitle}</p>
          </div>
        </div>
        <p className="mt-4 text-sm text-ink">{evidence.snippet}</p>
      </div>
      <div className="rounded-3xl border border-dashed border-line bg-mist/60 p-5 text-sm text-slate">
        {preview && preview.preview_url.includes("signed.example.com") ? (
          <>
            Interactive preview is unavailable in fixture mode. This panel is ready to load the signed preview URL from backend when
            `NEXT_PUBLIC_API_BASE_URL` is configured.
            <div className="mt-3 break-all text-xs text-slate">{preview.preview_url}</div>
          </>
        ) : preview ? (
          <iframe className="min-h-[320px] w-full rounded-2xl border border-line" src={preview.preview_url} title={evidence.title} />
        ) : (
          "Preview artifact is not ready. The user can still inspect citation metadata and use the download action."
        )}
      </div>
      <div className="flex flex-wrap gap-2">
        <Button variant="secondary" type="button">
          Open source
        </Button>
        <Button variant="ghost" type="button">
          Download file
        </Button>
      </div>
    </div>
  );
}
