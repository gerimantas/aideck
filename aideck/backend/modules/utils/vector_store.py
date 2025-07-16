from chromadb import Client as ChromaClient
# from pinecone import Client as PineconeClient  # Uncomment if Pinecone is used


class VectorStore:
    def __init__(self, backend: str = "chromadb", config: dict = None, collection_name: str = "aideck_vectors"):
        self.backend = backend
        self.config = config or {}
        self.collection_name = collection_name
        if backend == "chromadb":
            self.client = ChromaClient(**self.config)
            # Create or get collection
            if hasattr(self.client, "get_or_create_collection"):
                self.collection = self.client.get_or_create_collection(name=self.collection_name)
            else:
                # For older chromadb versions
                try:
                    self.collection = self.client.get_collection(name=self.collection_name)
                except Exception:
                    self.collection = self.client.create_collection(name=self.collection_name)
        # elif backend == "pinecone":
        #     self.client = PineconeClient(**self.config)
        else:
            raise ValueError(f"Unsupported backend: {backend}")

    def add_vector(self, vector, metadata=None, ids=None):
        # ChromaDB expects vectors as list, ids as list, metadata as list of dicts
        if self.backend == "chromadb":
            if ids is None:
                import uuid
                ids = [str(uuid.uuid4())]
            if not isinstance(vector[0], (list, tuple)):
                vector = [vector]
            metadata = [metadata or {}]
            return self.collection.add(embeddings=vector, ids=ids, metadatas=metadata)
        # elif self.backend == "pinecone":
        #     ...

    def query(self, query_vector, top_k=5):
        if self.backend == "chromadb":
            if not isinstance(query_vector[0], (list, tuple)):
                query_vector = [query_vector]
            return self.collection.query(query_embeddings=query_vector, n_results=top_k)
        # elif self.backend == "pinecone":
        #     ...

    def switch_backend(self, backend: str, config: dict = None):
        self.__init__(backend, config, self.collection_name)
