import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

client = chromadb.Client()
embedding_fn = SentenceTransformerEmbeddingFunction()

collection = client.get_or_create_collection("meetings", embedding_function=embedding_fn)

def store_document(text: str, metadata: dict):
    collection.add(documents=[text], metadatas=[metadata], ids=[metadata["id"]])

def retrieve_relevant_chunks(query: str, k: int = 3):
    results = collection.query(query_texts=[query], n_results=k)
    return " ".join(results["documents"][0])