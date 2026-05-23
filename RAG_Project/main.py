from sample_doc import documents

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(documents)

import faiss
import numpy as np

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))




query = "Which tool is used for caching?"
query_embedding = model.encode([query])

k = 2

distances, indices = index.search(
    np.array(query_embedding),
    k
)