# Class Diagram Specification

## 1. PURPOSE

Mo ta cau truc lop cua Search and Retrieval module.

## 2. CLASS DIAGRAM

```mermaid
classDiagram
    class SearchRouter {
        +searchDocuments(request: SearchRequest) SearchResponse
    }
    class SearchService {
        +search(request: SearchRequest) SearchResponse
    }
    class DenseRetriever {
        +retrieve(query: str, filters: NormalizedFilters) Candidate[]
    }
    class SparseRetriever {
        +retrieve(query: str, filters: NormalizedFilters) Candidate[]
    }
    class ResultFusion {
        +fuse(dense: Candidate[], sparse: Candidate[]) Candidate[]
    }
    class Reranker {
        +rerank(query: str, candidates: Candidate[]) Candidate[]
    }
    class SearchResultPresenter {
        +present(candidates: Candidate[], page: int, limit: int) SearchResponse
    }

    SearchRouter --> SearchService
    SearchService --> DenseRetriever
    SearchService --> SparseRetriever
    SearchService --> ResultFusion
    SearchService --> Reranker
    SearchService --> SearchResultPresenter
```

## 3. CLASS RESPONSIBILITY TABLE

| Class / Component | Responsibility | Key Operations | Dependencies | Notes |
| --- | --- | --- | --- | --- |
| SearchService | Dieu phoi retrieval/rerank/present | `search` | retrievers, fusion, rerank | Core module |
| DenseRetriever | Semantic retrieval | `retrieve` | vector store | Strategy 1 |
| SparseRetriever | Keyword retrieval | `retrieve` | sparse index | Strategy 2 |
| ResultFusion | Hop candidate | `fuse` | None | RRF/fusion contract |
| SearchResultPresenter | Map candidate sang OpenAPI union | `present` | None | API-facing |

## 4. DESIGN CONSIDERATIONS

- **Encapsulation & Cohesion:** Presenter khong tham gia retrieval logic.
- **Extensibility:** Co the doi retriever/reranker ma khong doi router.
- **Reusability:** SearchService duoc QueryService dung lai.
- **Compliance & Security:** Access filtering phai truoc presenter.

## 5. CHANGE HISTORY

| Version | Date | Description | Author | Reviewer |
| --- | --- | --- | --- | --- |
| 1.0 | 2026-04-12 | Initial release | OpenAI Codex | Pending |
