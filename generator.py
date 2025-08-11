from typing import List

# Rudimentary "generation" that answers from retrieved context with citations.
def generate_answer(query: str, contexts: List[dict]) -> str:
    """
    Given the original query and the list of retrieved context chunks,
    generate an answer string that incorporates content and cites sources.
    """
    cited_sources = set()
    answer_parts = []
    for ctx in contexts:
        answer_parts.append(ctx['document'])
        title = ctx['metadata'].get('title', ctx['chunk_id'])
        cited_sources.add(f"[{title}]")
    answer = " ".join(answer_parts)
    if not answer:
        answer = "Sorry, I do not have relevant information on that."
    else:
        answer += f"\n\nSources: {' '.join(sorted(cited_sources))}"
    return answer
