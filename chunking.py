from typing import List, Dict
import math

def chunk_document(doc: Dict, chunk_size: int = 40, overlap: int = 10) -> List[Dict]:
    """
    Splits document content into overlapping chunks for embedding and retrieval.
    Returns list of chunks with metadata.
    """
    words = doc['content'].split()
    chunks = []
    i = 0
    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        text = ' '.join(chunk_words)
        # Metadata includes doc_id, source, and chunk index
        chunk = {
            'chunk_id': f"{doc['doc_id']}_chunk_{i//chunk_size}",
            'text': text,
            'doc_id': doc['doc_id'],
            'source': doc.get('source', ''),
            'title': doc.get('title', ''),
            'chunk_index': i // chunk_size
        }
        chunks.append(chunk)
        i += chunk_size - overlap if (chunk_size - overlap) > 0 else chunk_size
    return chunks

def chunk_corpus(corpus: List[Dict], chunk_size: int = 40, overlap: int = 10) -> List[Dict]:
    all_chunks = []
    for doc in corpus:
        chunks = chunk_document(doc, chunk_size, overlap)
        all_chunks.extend(chunks)
    return all_chunks
