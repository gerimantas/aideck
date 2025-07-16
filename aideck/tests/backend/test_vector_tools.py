import pytest
from aideck.backend.modules.utils.vector_tools import EmbeddingTools

def dummy_embedding_fn(text):
    return [float(ord(c)) for c in text]

def test_embed_and_query_project():
    tools = EmbeddingTools()
    project_id = "proj123"
    text = "buggy code"
    embedding = tools.embed_project(project_id, text, dummy_embedding_fn)
    assert isinstance(embedding, list)
    results = tools.query_project_vectors(project_id, embedding)
    assert isinstance(results, list)
