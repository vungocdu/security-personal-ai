"use client";

import { ArrowLeft, ChevronRight, FileText, Folder, FolderPlus, UploadCloud } from "lucide-react";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Collapsible, CollapsibleContent } from "@/components/ui/collapsible";
import { cn } from "@/lib/utils";
import { workspaceApi } from "@/lib/api";
import type { RepositoryListingResponse } from "@/lib/types";

type ListingMap = Record<string, RepositoryListingResponse | undefined>;

function joinPath(parent: string, name: string): string {
  const trimmed = parent.replace(/\/+$/, "");
  return trimmed ? `${trimmed}/${name}` : name;
}

function splitPath(path: string): string[] {
  return path
    .split("/")
    .map((part) => part.trim())
    .filter(Boolean);
}

export function RepositoryExplorer() {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [currentPath, setCurrentPath] = useState<string>("");
  const [expanded, setExpanded] = useState<Set<string>>(() => new Set([""]));
  const [listings, setListings] = useState<ListingMap>({});
  const [loading, setLoading] = useState(true);
  const [creatingFolder, setCreatingFolder] = useState(false);
  const [newFolderName, setNewFolderName] = useState("");
  const [uploadStatus, setUploadStatus] = useState<string>("No uploads in this session");
  const [error, setError] = useState<string | null>(null);

  const currentListing = listings[currentPath] ?? null;

  const breadcrumbParts = useMemo(() => splitPath(currentPath), [currentPath]);

  const fetchListing = useCallback(async (path: string) => {
    const response = await workspaceApi.listRepository(path || undefined);
    setListings((previous) => ({ ...previous, [path]: response }));
    return response;
  }, []);

  useEffect(() => {
    async function bootstrap() {
      setLoading(true);
      setError(null);
      try {
        await fetchListing("");
      } catch (caught) {
        setError(caught instanceof Error ? caught.message : "Failed to load repository.");
      } finally {
        setLoading(false);
      }
    }

    void bootstrap();
  }, [fetchListing]);

  const toggleFolder = useCallback(
    async (path: string) => {
      setError(null);
      setExpanded((previous) => {
        const next = new Set(previous);
        if (next.has(path)) {
          next.delete(path);
        } else {
          next.add(path);
        }
        return next;
      });

      if (!listings[path]) {
        try {
          await fetchListing(path);
        } catch (caught) {
          setError(caught instanceof Error ? caught.message : "Failed to load folder.");
        }
      }
    },
    [fetchListing, listings],
  );

  const navigateToFolder = useCallback(
    async (path: string) => {
      setCurrentPath(path);
      setError(null);
      if (!listings[path]) {
        try {
          await fetchListing(path);
        } catch (caught) {
          setError(caught instanceof Error ? caught.message : "Failed to load folder.");
        }
      }
      setExpanded((previous) => new Set(previous).add(path));
    },
    [fetchListing, listings],
  );

  async function handleCreateFolder() {
    const trimmed = newFolderName.trim();
    if (!trimmed) {
      setError("Folder name is required.");
      return;
    }
    setCreatingFolder(true);
    setError(null);
    try {
      const path = joinPath(currentPath, trimmed);
      await workspaceApi.createFolder(path);
      setNewFolderName("");
      await fetchListing(currentPath);
      setExpanded((previous) => new Set(previous).add(currentPath));
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Failed to create folder.");
    } finally {
      setCreatingFolder(false);
    }
  }

  async function handleUpload(files: FileList | null) {
    if (!files || files.length === 0) {
      return;
    }
    setError(null);
    try {
      const response = await workspaceApi.uploadRepositoryFile(files[0], currentPath || undefined);
      setUploadStatus(`Uploaded: ${response.file.path}`);
      await fetchListing(currentPath);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Upload failed.");
    }
  }

  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center justify-end gap-2">
        <div className="flex items-center gap-1">
          <Dialog>
            <DialogTrigger asChild>
              <Button variant="secondary" size="icon" aria-label="Create folder">
                <FolderPlus className="h-4 w-4" />
              </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-md">
              <DialogHeader>
                <DialogTitle>Create folder</DialogTitle>
                <DialogDescription>Creates a folder placeholder in Firebase Storage under the current path.</DialogDescription>
              </DialogHeader>
              <div className="space-y-2">
                <div className="text-xs text-slate">Parent: {currentPath ? `/${currentPath}` : "/"}</div>
                <Input
                  value={newFolderName}
                  onChange={(event) => setNewFolderName(event.target.value)}
                  placeholder="Folder name (e.g. 2026-Q2)"
                />
              </div>
              <DialogFooter className="gap-2 sm:gap-2">
                <Button variant="secondary" onClick={() => setNewFolderName("")} type="button">
                  Cancel
                </Button>
                <Button onClick={() => void handleCreateFolder()} disabled={creatingFolder} type="button">
                  {creatingFolder ? "Creating..." : "Create"}
                </Button>
              </DialogFooter>
            </DialogContent>
          </Dialog>

          <Button variant="accent" size="icon" aria-label="Upload file" onClick={() => fileInputRef.current?.click()}>
            <UploadCloud className="h-4 w-4" />
          </Button>
        </div>
      </div>

      <input ref={fileInputRef} className="hidden" type="file" onChange={(event) => void handleUpload(event.target.files)} />

      <div className="mt-3 rounded-2xl border border-line/70 bg-white/70 px-3 py-2 text-xs text-slate">
        <div className="flex items-center gap-2">
          <Button
            variant="secondary"
            size="icon"
            aria-label="Go up one folder"
            onClick={() => void navigateToFolder(breadcrumbParts.slice(0, -1).join("/"))}
            disabled={breadcrumbParts.length === 0}
          >
            <ArrowLeft className="h-3.5 w-3.5" />
          </Button>
          <div className="min-w-0 truncate">
            <span className="text-ink">/</span>
            {breadcrumbParts.length === 0 ? <span className="ml-1 text-ink/80">root</span> : <span className="ml-1">{breadcrumbParts.join(" / ")}</span>}
          </div>
        </div>
      </div>

      <div className="mt-3 rounded-2xl bg-sand p-3 text-xs text-slate">{uploadStatus}</div>
      {error ? <div className="mt-2 rounded-2xl border border-[#efc5c5] bg-[#fff4f4] px-3 py-2 text-xs text-[#8f3131]">{error}</div> : null}

      <Separator className="my-4" />

      <div className="flex min-h-0 flex-1 flex-col gap-3">
        <div className="text-xs font-semibold uppercase tracking-[0.24em] text-slate">Folders</div>
        <div className="min-h-0 flex-1 overflow-hidden rounded-2xl border border-line/70 bg-white/70" data-testid="repository-folder-tree">
          <ScrollArea className="h-full">
            <div className="p-2">
              {loading ? (
                <div className="rounded-xl bg-mist px-3 py-3 text-sm text-slate">Loading...</div>
              ) : (
                <FolderTree
                  rootPath=""
                  currentPath={currentPath}
                  expanded={expanded}
                  listings={listings}
                  onToggle={toggleFolder}
                  onNavigate={navigateToFolder}
                />
              )}
            </div>
          </ScrollArea>
        </div>

        <div className="text-xs font-semibold uppercase tracking-[0.24em] text-slate">Contents</div>
        <div className="min-h-0 flex-1 overflow-hidden rounded-2xl border border-line/70 bg-white/70" data-testid="repository-contents">
          <ScrollArea className="h-full">
            <div className="p-2">
              {!currentListing ? (
                <div className="rounded-xl bg-mist px-3 py-3 text-sm text-slate">Select a folder.</div>
              ) : (
                <div className="space-y-1">
                  {currentListing.folders.map((folder) => (
                    <button
                      key={folder.path}
                      className="flex w-full items-center gap-2 rounded-xl px-2 py-2 text-left text-sm text-ink hover:bg-accentSoft"
                      type="button"
                      onClick={() => void navigateToFolder(folder.path)}
                    >
                      <Folder className="h-4 w-4 text-warning" />
                      <span className="truncate">{folder.name}</span>
                    </button>
                  ))}
                  {currentListing.files.map((file) => (
                    <div key={file.path} className="flex items-center gap-2 rounded-xl px-2 py-2 text-sm text-ink">
                      <FileText className="h-4 w-4 text-slate" />
                      <span className="truncate">{file.name}</span>
                    </div>
                  ))}
                  {currentListing.folders.length === 0 && currentListing.files.length === 0 ? (
                    <div className="rounded-xl bg-mist px-3 py-3 text-sm text-slate">Empty folder.</div>
                  ) : null}
                </div>
              )}
            </div>
          </ScrollArea>
        </div>
      </div>
    </div>
  );
}

function FolderTree(props: {
  rootPath: string;
  currentPath: string;
  expanded: Set<string>;
  listings: ListingMap;
  onToggle: (path: string) => Promise<void>;
  onNavigate: (path: string) => Promise<void>;
}) {
  const listing = props.listings[props.rootPath];
  if (!listing) {
    return null;
  }

  return (
    <div className="space-y-1">
      {listing.folders.map((folder) => (
        <FolderNode
          key={folder.path}
          path={folder.path}
          name={folder.name}
          depth={0}
          currentPath={props.currentPath}
          expanded={props.expanded}
          listings={props.listings}
          onToggle={props.onToggle}
          onNavigate={props.onNavigate}
        />
      ))}
      {listing.folders.length === 0 ? <div className="px-2 py-2 text-sm text-slate">No folders.</div> : null}
    </div>
  );
}

function FolderNode(props: {
  path: string;
  name: string;
  depth: number;
  currentPath: string;
  expanded: Set<string>;
  listings: ListingMap;
  onToggle: (path: string) => Promise<void>;
  onNavigate: (path: string) => Promise<void>;
}) {
  const isOpen = props.expanded.has(props.path);
  const isActive = props.currentPath === props.path;
  const listing = props.listings[props.path];

  return (
    <div>
      <Collapsible open={isOpen} className="w-full">
        <div className={cn("flex items-center gap-1 rounded-xl pr-2 text-sm hover:bg-accentSoft", isActive ? "bg-accentSoft" : "")}>
          <button
            className="flex h-8 w-8 items-center justify-center rounded-lg text-slate hover:text-ink"
            type="button"
            aria-label={`Toggle folder ${props.name}`}
            onClick={() => void props.onToggle(props.path)}
          >
            <ChevronRight className={cn("h-4 w-4 transition-transform", isOpen ? "rotate-90" : "rotate-0")} />
          </button>
          <button
            className={cn("flex min-w-0 flex-1 items-center gap-2 rounded-lg py-2 text-left", isActive ? "text-ink" : "text-ink")}
            type="button"
            onClick={() => void props.onNavigate(props.path)}
          >
            <Folder className="h-4 w-4 text-warning" />
            <span className="truncate" style={{ paddingLeft: `${props.depth * 12}px` }}>
              {props.name}
            </span>
          </button>
        </div>
        <CollapsibleContent className="ml-4 border-l border-line/60 pl-2">
          <div className="space-y-1 py-1">
            {isOpen && !listing ? <div className="px-2 py-2 text-xs text-slate">Loading...</div> : null}
            {listing?.folders?.map((child) => (
              <FolderNode
                key={child.path}
                path={child.path}
                name={child.name}
                depth={props.depth + 1}
                currentPath={props.currentPath}
                expanded={props.expanded}
                listings={props.listings}
                onToggle={props.onToggle}
                onNavigate={props.onNavigate}
              />
            ))}
            {listing && listing.folders.length === 0 ? <div className="px-2 py-2 text-xs text-slate">Empty</div> : null}
          </div>
        </CollapsibleContent>
      </Collapsible>
    </div>
  );
}
