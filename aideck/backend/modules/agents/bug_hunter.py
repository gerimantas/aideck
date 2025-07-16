"""
BugHunter agent for AIDECK
"""
from .base import BaseAgent

class BugHunterAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="BugHunterAgent")

    def run(self, input_data):
        # RAG/embedding logic
        from aideck.backend.modules.utils.vector_tools import EmbeddingTools
        text = input_data.get("text", "")
        project_id = input_data.get("project_id", "")
        embedding_fn = input_data.get("embedding_fn")
        if embedding_fn and text and project_id:
            tools = EmbeddingTools()
            embedding = tools.embed_project(project_id, text, embedding_fn)
            related_vectors = tools.query_project_vectors(project_id, embedding)
            return {"embedding": embedding, "related_vectors": related_vectors}
        return {"bugs": ["No bugs found."]}
