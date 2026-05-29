import os
import pandas as pd
from preprocessing import load_and_preprocess_data
from clustering import perform_clustering
from scorer import calculate_score_by_target

def main():
    dataset_path = 'UpdatedResumeDataSet.csv'
    
    # Check if dataset exists
    if not os.path.exists(dataset_path):
        print(f"Error: {dataset_path} not found in the current directory.")
        print("Please download the Kaggle Resume Dataset and place it here.")
        print("You can download it from: https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset")
        return
        
    print("--- Starting Resume Parser Pipeline ---")
    
    # 1. Load and Preprocess
    df = load_and_preprocess_data(dataset_path)
    print(f"Successfully processed {len(df)} resumes.")
    
    # 2. Clustering
    print("\n--- Running Clustering ---")
    df, vectorizer, kmeans_model = perform_clustering(df, num_clusters=10)
    
    # 3. Scoring
    print("\n--- Scoring Resumes ---")
    # For demonstration, we use a sample target job description
    target_job_description = "HR Manager with experience in recruiting, employee relations, and onboarding."
    print(f"Target Job Description:\n'{target_job_description}'")
    
    df = calculate_score_by_target(df, vectorizer, target_job_description)
    
    # Sort resumes by score to find the best candidates
    top_candidates = df.sort_values(by='Score', ascending=False)
    
    print("\n--- Top 5 Candidates ---")
    print(top_candidates[['Category', 'Score']].head(5))
    
    # Save the results
    output_path = 'ScoredResumes.csv'
    top_candidates[['Category', 'Resume', 'Cluster', 'Score']].to_csv(output_path, index=False)
    print(f"\nResults saved to {output_path}")

if __name__ == "__main__":
    main()
