from rag_pipeline import ingest_and_index, answer_query
from eval import evaluate
from embedding import fake_embed

# Sample queries for evaluation (with expected doc_ids that should be relevant)
sample_eval_queries = [
    {
        'query': "How can I reset my device?",
        'relevant_doc_ids': ['faq_1', 'faq_3']
    },
    {
        'query': "Device won't turn on. What should I do?",
        'relevant_doc_ids': ['troubleshoot_1', 'faq_1']
    },
    {
        'query': "How do I charge my device?",
        'relevant_doc_ids': ['manual_1']
    },
    {
        'query': "How to connect to Wi-Fi?",
        'relevant_doc_ids': ['faq_2']
    }
]

if __name__ == '__main__':
    # Build and index corpus
    chroma = ingest_and_index()

    # Quick demo
    user_query = "My device doesn't power on, what should I check?"
    answer, hits = answer_query(user_query, chroma)
    print("\n---\nDEMO ANSWER\n---")
    print(f"Q: {user_query}\nA: {answer}")

    # Evaluate retrieval
    print("\n---\nEVALUATION\n---")
    from chroma_utils import ChromaManager
    evaluate(sample_eval_queries, chroma, fake_embed, k=3)
