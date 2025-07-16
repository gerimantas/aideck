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
        self.vector_store.add_vector(embedding, metadata=metadata)
        return embedding

    def query_project_vectors(self, project_id: str, query_embedding, top_k=5):
        results = self.vector_store.query(query_embedding, top_k=top_k)
        # Filter by project_id
        return [r for r in results if r.get("metadata", {}).get("project_id") == project_id]
