import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
import pytest
from aideck.backend.modules.utils.vector_tools import EmbeddingTools

def dummy_embedding_fn(text):
    return [0.0] * 1536  # Fiksuota dimensija

def test_embed_and_query_project():
    tools = EmbeddingTools()
    project_id = "proj123"
    text = "buggy code"
    embedding = tools.embed_project(project_id, text, dummy_embedding_fn)
    assert isinstance(embedding, list)
    results = tools.query_project_vectors(project_id, embedding)
    print("DEBUG QUERY RESULT:", results)
    assert isinstance(results, list)

def test_rag_retrieve():
    tools = EmbeddingTools()
    project_id = "projRAG"
    text = "test RAG"
    tools.embed_project(project_id, text, dummy_embedding_fn)
    results = tools.rag_retrieve(project_id, text, dummy_embedding_fn, top_k=3)
    print("DEBUG RAG RESULT:", results)
    assert isinstance(results, list)
    assert any(isinstance(r, dict) and r.get("project_id") == project_id for r in results)
