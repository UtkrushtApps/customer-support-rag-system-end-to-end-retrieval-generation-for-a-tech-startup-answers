from support_corpus import load_corpus
from chunking import chunk_corpus
from embedding import batch_embed_texts, fake_embed
from chroma_utils import ChromaManager
from generator import generate_answer


def ingest_and_index():
    # 1. Load corpus
    corpus = load_corpus()
    # 2. Chunk
    chunks = chunk_corpus(corpus, chunk_size=40, overlap=10)
    # 3. Embed
    emb_matrix = batch_embed_texts([c['text'] for c in chunks])
    # 4. Populate Chroma
    chroma = ChromaManager()
    chroma.clear()
    chroma.add_chunks(chunks, emb_matrix)
    print(f"Ingested {len(chunks)} chunks.")
    return chroma


def answer_query(query: str, chroma, k: int = 3):
    # 1. Embed query
    q_emb = fake_embed(query)
    # 2. Retrieve context
    hits = chroma.search(q_emb, k=k)
    # 3. Generate answer
    answer = generate_answer(query, hits)
    return answer, hits

if __name__ == "__main__":
    # Sample usage
    chroma = ingest_and_index()
    for query in [
        "How do I reset my device?",
        "What to do if device does not charge?",
        "How can I connect to WiFi?",
        "How to perform a factory reset?",
        "What if device won't power on?"
    ]:
        answer, hits = answer_query(query, chroma, k=3)
        print(f"\nQ: {query}\nA: {answer}\n---")
