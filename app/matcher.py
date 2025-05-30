from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_resumes(jd_text, resumes):
    resume_names = [res["filename"] for res in resumes]
    resume_texts = [res["text"] for res in resumes]

    embeddings = model.encode([jd_text] + resume_texts)
    scores = cosine_similarity([embeddings[0]], embeddings[1:])[0]
    
    results = [
        {"filename": name, "score": float(np.round(score * 100, 2))}
        for name, score in zip(resume_names, scores)
    ]
    
    return sorted(results, key=lambda x: x["score"], reverse=True)
