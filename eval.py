from typing import List, Dict

def precision_at_k(relevant: List[str], retrieved: List[str], k: int) -> float:
    if k == 0: return 0.0
    retrieved_at_k = retrieved[:k]
    hits = sum(1 for doc_id in retrieved_at_k if doc_id in relevant)
    return hits / k

def recall_at_k(relevant: List[str], retrieved: List[str], k: int) -> float:
    if not relevant: return 0.0
    retrieved_at_k = retrieved[:k]
    hits = sum(1 for doc_id in retrieved_at_k if doc_id in relevant)
    return hits / len(relevant)

def evaluate(queries: List[Dict], chroma_manager, embed_func, k: int = 3):
    total_p, total_r, count = 0.0, 0.0, 0
    for q in queries:
        query_embed = embed_func(q['query'])
        hits = chroma_manager.search(query_embed, k=k)
        retrieved_ids = [hit['chunk_id'] for hit in hits]
        # For simulation, relevant is any chunk from the "doc_id" gold list
        relevant = [cid for cid in retrieved_ids if any(doc_id in cid for doc_id in q['relevant_doc_ids'])]
        p = precision_at_k([cid for doc_id in q['relevant_doc_ids'] for cid in retrieved_ids if doc_id in cid], retrieved_ids, k)
        r = recall_at_k([cid for doc_id in q['relevant_doc_ids'] for cid in retrieved_ids if doc_id in cid], retrieved_ids, k)
        print(f"Query: {q['query']}")
        print(f"Precision@{k}: {p:.2f}  Recall@{k}: {r:.2f}")
        total_p += p
        total_r += r
        count += 1
    print(f"\nAvg Precision@{k}: {total_p/count:.2f}, Avg Recall@{k}: {total_r/count:.2f}")
