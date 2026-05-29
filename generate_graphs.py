import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score

from preprocessing import load_and_preprocess_data
from clustering import perform_clustering

def generate_graphs():
    print("Loading data and generating graphs...")
    df = load_and_preprocess_data('UpdatedResumeDataSet.csv')
    
    true_labels = df['Category']
    unique_categories = true_labels.unique()
    num_categories = len(unique_categories)
    
    # Run clustering
    df, vectorizer, kmeans = perform_clustering(df, num_clusters=num_categories)
    
    # Map clusters
    cluster_mapping = {}
    for cluster_id in range(num_categories):
        most_common = df[df['Cluster'] == cluster_id]['Category'].mode()[0]
        cluster_mapping[cluster_id] = most_common
    df['Predicted_Category'] = df['Cluster'].map(cluster_mapping)
    
    # Calculate category accuracies
    accuracies = []
    for category in unique_categories:
        cat_df = df[df['Category'] == category]
        if len(cat_df) > 0:
            acc = accuracy_score(cat_df['Category'], cat_df['Predicted_Category'])
            accuracies.append({'Category': category, 'Accuracy': acc * 100})
            
    acc_df = pd.DataFrame(accuracies).sort_values(by='Accuracy', ascending=False)
    
    # Plot 1: Category Accuracy Bar Chart
    plt.figure(figsize=(14, 8))
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x='Accuracy', y='Category', data=acc_df, palette='viridis')
    plt.title('AI Model Accuracy by Job Category (KMeans Clustering)', fontsize=16)
    plt.xlabel('Accuracy (%)', fontsize=12)
    plt.ylabel('Job Category', fontsize=12)
    plt.tight_layout()
    plt.savefig('category_accuracy.png', dpi=300)
    print("Saved category_accuracy.png")
    
    # Plot 2: Dataset Distribution
    plt.figure(figsize=(12, 8))
    cat_counts = df['Category'].value_counts()
    sns.barplot(x=cat_counts.values, y=cat_counts.index, palette='mako')
    plt.title('Distribution of Resumes Across Job Categories', fontsize=16)
    plt.xlabel('Number of Resumes', fontsize=12)
    plt.ylabel('Job Category', fontsize=12)
    plt.tight_layout()
    plt.savefig('cluster_distribution.png', dpi=300)
    print("Saved cluster_distribution.png")

if __name__ == '__main__':
    generate_graphs()
