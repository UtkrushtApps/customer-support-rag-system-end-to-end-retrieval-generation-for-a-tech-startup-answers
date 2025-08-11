import chromadb
import numpy as np
from typing import List, Dict

CHROMA_COLLECTION_NAME = 'customer_support_rag'

class ChromaManager:
    def __init__(self, url='http://localhost:8000', collection_name=CHROMA_COLLECTION_NAME):
        self.client = chromadb.HttpClient(host='localhost', port=8000)
        self.collection = self.client.get_or_create_collection(collection_name)

    def clear(self):
        self.client.delete_collection(self.collection.name)
        self.collection = self.client.get_or_create_collection(self.collection.name)

    def add_chunks(self, chunks: List[Dict], embeddings: np.ndarray):
        # Add to Chroma
        ids = [c['chunk_id'] for c in chunks]
        metadatas = [{k: v for k, v in c.items() if k != 'text' and k != 'chunk_id'} for c in chunks]
        texts = [c['text'] for c in chunks]
        self.collection.add(
            ids=ids,
            embeddings=embeddings.tolist(),
            documents=texts,
            metadatas=metadatas
        )

    def search(self, query_embedding: np.ndarray, k: int = 3):
        # Chroma VSS (returns top-k hits)
        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k,
            include=['metadatas', 'documents', 'distances', 'ids']
        )
        # Transform results
        hits = []
        for idx in range(len(results['ids'][0])):
            hit = {
                'chunk_id': results['ids'][0][idx],
                'distance': results['distances'][0][idx],
                'document': results['documents'][0][idx],
                'metadata': results['metadatas'][0][idx]
            }
            hits.append(hit)
        return hits
