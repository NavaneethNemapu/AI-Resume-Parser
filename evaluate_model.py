import pandas as pd
from sklearn.metrics import accuracy_score, silhouette_score
import numpy as np

# Import our existing preprocessing and clustering logic
from preprocessing import load_and_preprocess_data
from clustering import perform_clustering

def evaluate_model():
    print("--- Starting AI Model Evaluation ---")
    dataset_path = 'UpdatedResumeDataSet.csv'
    
    try:
        # 1. Load Data
        print("\n1. Loading Dataset...")
        df = load_and_preprocess_data(dataset_path)
        
        # 2. Get true labels (Categories)
        true_labels = df['Category']
        unique_categories = true_labels.unique()
        num_categories = len(unique_categories)
        print(f"Found {num_categories} unique job categories in dataset.")
        
        # 3. Perform Clustering
        print(f"\n2. Running KMeans Clustering (k={num_categories})...")
        # Note: We use the exact number of real categories to get a fair accuracy score
        df, vectorizer, kmeans_model = perform_clustering(df, num_clusters=num_categories)
        
        # 4. Map Clusters to True Categories (to calculate accuracy)
        # Since KMeans assigns arbitrary numbers (0, 1, 2) to clusters, 
        # we have to figure out which number corresponds to which string Category.
        print("\n3. Mapping AI Clusters to Real Job Categories...")
        cluster_mapping = {}
        for cluster_id in range(num_categories):
            # Find the most common real category inside this AI cluster
            most_common_category = df[df['Cluster'] == cluster_id]['Category'].mode()[0]
            cluster_mapping[cluster_id] = most_common_category
            
        # Create a new column with the AI's "Predicted Category"
        df['Predicted_Category'] = df['Cluster'].map(cluster_mapping)
        
        # 5. Calculate Metrics
        print("\n--- RESULTS ---")
        
        # Classification Accuracy
        acc = accuracy_score(df['Category'], df['Predicted_Category'])
        print(f"Model Classification Accuracy: {acc * 100:.2f}%")
        
        # Silhouette Score (Measures how distinct/separated the clusters are. 1 is best, -1 is worst)
        X = vectorizer.transform(df['processed_resume'])
        sil_score = silhouette_score(X, kmeans_model.labels_)
        print(f"Model Silhouette Score (Cluster Quality): {sil_score:.4f}")
        
        print("\nCategory-Specific Accuracies:")
        for category in unique_categories:
            cat_df = df[df['Category'] == category]
            if len(cat_df) > 0:
                cat_acc = accuracy_score(cat_df['Category'], cat_df['Predicted_Category'])
                print(f" - {category}: {cat_acc * 100:.2f}%")
                
    except Exception as e:
        print(f"Error during evaluation: {e}")

if __name__ == "__main__":
    evaluate_model()
