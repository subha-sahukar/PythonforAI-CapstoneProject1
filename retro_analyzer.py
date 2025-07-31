from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

def analyze_feedback(feedback_list, num_clusters=3):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(feedback_list)

    model = KMeans(n_clusters=num_clusters, random_state=42)
    model.fit(X)

    themes = {}
    for idx in range(num_clusters):
        cluster_indices = np.where(model.labels_ == idx)[0]
        cluster_texts = [feedback_list[i] for i in cluster_indices]
        themes[f"Theme {idx + 1}"] = cluster_texts

    return themes