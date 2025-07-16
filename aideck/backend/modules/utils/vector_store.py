from chromadb import Client as ChromaClient
# from pinecone import Client as PineconeClient  # Uncomment if Pinecone is used

class VectorStore:
    def __init__(self, backend: str = "chromadb", config: dict = None):
        self.backend = backend
        self.config = config or {}
        if backend == "chromadb":
            self.client = ChromaClient(**self.config)
        # elif backend == "pinecone":
        #     self.client = PineconeClient(**self.config)
        else:
            raise ValueError(f"Unsupported backend: {backend}")

    def add_vector(self, vector, metadata=None):
        # Example for ChromaDB
        return self.client.add(vector, metadata=metadata)

    def query(self, query_vector, top_k=5):
        return self.client.query(query_vector, top_k=top_k)

    def switch_backend(self, backend: str, config: dict = None):
        self.__init__(backend, config)
