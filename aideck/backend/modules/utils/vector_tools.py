"""
Embedding tools for AIDECK (ChromaDB, Pinecone abstraction)
"""
from chromadb import Client as ChromaClient
from aideck.backend.modules.utils.vector_store import VectorStore

class EmbeddingTools:
    def __init__(self, backend: str = "chromadb", config: dict = None):
        self.vector_store = VectorStore(backend, config)
        self.chroma = ChromaClient(**(config or {})) if backend == "chromadb" else None

    def embed_project(self, project_id: str, text: str, embedding_fn):
        embedding = embedding_fn(text)
        metadata = {"project_id": project_id}
        ids = [project_id + "_" + str(hash(text))]
        self.vector_store.add_vector(embedding, metadata=metadata, ids=ids)
        return embedding

    def query_project_vectors(self, project_id: str, query_embedding, top_k=5):
        results = self.vector_store.query(query_embedding, top_k=top_k)
        # ChromaDB returns a dict with 'ids', 'embeddings', 'metadatas', etc.
        if isinstance(results, list):
            filtered = []
            for item in results:
                if isinstance(item, dict):
                    meta = item.get('metadata') or item.get('metadatas') or {}
                    if meta.get("project_id") == project_id:
                        filtered.append(meta)
            return filtered
        elif isinstance(results, dict):
            metadatas = results.get('metadatas', [])
            ids = results.get('ids', [])
            filtered = [m for m, i in zip(metadatas, ids) if isinstance(m, dict) and m.get("project_id") == project_id]
            return filtered
        return []

    def rag_retrieve(self, project_id: str, query_text: str, embedding_fn, top_k=5):
        query_embedding = embedding_fn(query_text)
        results = self.query_project_vectors(project_id, query_embedding, top_k=top_k)
        # Return top_k metadatas and optionally embeddings
        return results
