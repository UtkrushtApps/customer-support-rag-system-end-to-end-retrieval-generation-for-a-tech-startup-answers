import numpy as np
import hashlib

# Simulate basic embedding (replace with real model in prod)
def fake_embed(text: str) -> np.ndarray:
    # Deterministic fake embedding: seed by hash, generate random vector
    seed = int(hashlib.sha256(text.encode()).hexdigest(), 16) % (2**32 - 1)
    rng = np.random.default_rng(seed)
    return rng.normal(size=(384,))  # Assume 384 dim embeddings

def batch_embed_texts(texts):
    return np.stack([fake_embed(text) for text in texts])
