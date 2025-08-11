# Solution Steps

1. 1. Create a small, realistic support document corpus with representative FAQs, manuals, and troubleshooting guides in support_corpus.py.

2. 2. Implement chunking.py to split long documents into overlapping text chunks and preserve essential metadata (doc_id, title, source, chunk index).

3. 3. Implement embedding.py with a deterministic, mock embedding function (for production, replace with a true sentence transformer model). Add batch embedding logic.

4. 4. Build chroma_utils.py to wrap ChromaDB collection management: creating/clearing collections, batch adding chunks+embeddings, and performing similarity search with retrieval of both documents and metadata.

5. 5. Implement generator.py to take a query and retrieved context chunks, then compose a customer-facing answer citing all sources.

6. 6. Create rag_pipeline.py for end-to-end ingestion: corpus loading, chunking, embedding, population of ChromaDB, and a function to answer queries via retrieval and generation.

7. 7. Implement eval.py for retrieval quality measurement, computing precision@k and recall@k given lists of retrieved and gold-relevant doc_ids, plus an 'evaluate' function for running on a sample query set.

8. 8. Build main.py to tie everything together, including ingesting the corpus, running a sample question/answer, and invoking the retrieval evaluation.

9. 9. Test the whole system: ingest, query, and evaluate precision/recall, ensuring answers cite the correct sources and retrieval is accurate.

