from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def perform_clustering(df, num_clusters=10):
    """
    Converts preprocessed resumes into TF-IDF vectors and performs KMeans clustering.
    Returns the dataframe with cluster labels, the vectorizer, and the kmeans model.
    """
    print("Vectorizing text using TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(df['processed_resume'])
    
    print(f"Applying KMeans clustering with {num_clusters} clusters...")
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    kmeans.fit(X)
    
    df['Cluster'] = kmeans.labels_
    
    # Optional: Print top terms per cluster to understand what they represent
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()
    
    print("\nTop terms per cluster:")
    for i in range(num_clusters):
        top_terms = [terms[ind] for ind in order_centroids[i, :10]]
        print(f"Cluster {i}: {', '.join(top_terms)}")
        
    return df, vectorizer, kmeans

def get_cluster_domain(kmeans_model, vectorizer, target_domain_text):
    """
    Given a target domain text (like job description), find which cluster it belongs to.
    """
    X_target = vectorizer.transform([target_domain_text])
    target_cluster = kmeans_model.predict(X_target)[0]
    return target_cluster
