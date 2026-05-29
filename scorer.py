import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score_by_target(df, vectorizer, target_description):
    """
    Calculates a score (0 to 10) for each resume based on its cosine similarity
    with the target job description or keywords.
    """
    # Transform resumes and target using the same vectorizer
    X_resumes = vectorizer.transform(df['processed_resume'])
    X_target = vectorizer.transform([target_description])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(X_resumes, X_target).flatten()
    
    # Normalize similarities to a 0-10 scale
    # If max similarity is 0, avoid division by zero
    max_sim = similarities.max()
    if max_sim > 0:
        normalized_scores = (similarities / max_sim) * 10
    else:
        normalized_scores = np.zeros_like(similarities)
        
    df['Score'] = np.round(normalized_scores, 2)
    return df

def calculate_score_by_cluster(df, vectorizer, kmeans_model, target_domain_text):
    """
    Alternatively, score resumes based on their distance to the cluster center 
    that best matches the target domain.
    """
    # Find which cluster best matches the target domain
    from clustering import get_cluster_domain
    target_cluster = get_cluster_domain(kmeans_model, vectorizer, target_domain_text)
    
    # Get the centroid of the target cluster
    centroid = kmeans_model.cluster_centers_[target_cluster]
    
    # Transform resumes
    X_resumes = vectorizer.transform(df['processed_resume'])
    
    # Calculate similarity to centroid
    similarities = cosine_similarity(X_resumes, centroid.reshape(1, -1)).flatten()
    
    max_sim = similarities.max()
    if max_sim > 0:
        normalized_scores = (similarities / max_sim) * 10
    else:
        normalized_scores = np.zeros_like(similarities)
        
    df['Cluster_Score'] = np.round(normalized_scores, 2)
    return df
