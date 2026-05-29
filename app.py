from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pandas as pd

from preprocessing import load_and_preprocess_data, preprocess_text, clean_resume_text
from clustering import perform_clustering
from scorer import calculate_score_by_target
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils import process_uploaded_file

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

print("--- Initializing AI Models ---")
dataset_path = 'UpdatedResumeDataSet.csv'

# Load models globally so it only happens once on startup
if os.path.exists(dataset_path):
    print("1. Loading and preprocessing data...")
    df = load_and_preprocess_data(dataset_path)
    
    print("2. Performing clustering (to fit Vectorizer)...")
    df, vectorizer, kmeans_model = perform_clustering(df, num_clusters=10)
    print("--- Initialization Complete ---")
else:
    df = None
    vectorizer = None
    print("Dataset not found! Please place UpdatedResumeDataSet.csv in the directory.")


@app.route('/api/score', methods=['POST'])
def score_resumes():
    if vectorizer is None:
        return jsonify({"error": "AI Engine not initialized (Missing dataset)"}), 500
        
    job_description = request.form.get('job_description', '')
    
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    if not job_description:
        return jsonify({"error": "Job description is required."}), 400

    # Extract text from the uploaded file or ZIP
    extracted_texts = process_uploaded_file(file, file.filename)
    
    if not extracted_texts:
        return jsonify({"error": "Could not extract any text from the uploaded file(s)."}), 400

    cleaned_jd = preprocess_text(clean_resume_text(job_description))
    X_jd = vectorizer.transform([cleaned_jd])

    results = []
    
    for filename, text in extracted_texts.items():
        cleaned_resume = preprocess_text(clean_resume_text(text))
        X_resume = vectorizer.transform([cleaned_resume])
        # Calculate direct keyword overlap percentage.
        # This completely bypasses the global TF-IDF vocabulary so rare words are checked perfectly.
        jd_words = set(cleaned_jd.split())
        resume_words = set(cleaned_resume.split())
        overlap_ratio = len(jd_words.intersection(resume_words)) / len(jd_words) if len(jd_words) > 0 else 0
        
        # If overlap is very low (<= 20%), force it into the 0 to 1 range.
        if overlap_ratio <= 0.20:
            final_score = overlap_ratio * 4.0  # Max score here is 0.8
        else:
            # For decent matches, scale it up so a 60-80% overlap achieves a near 10.
            final_score = overlap_ratio * 13.0
            
        score = round(float(min(10.0, final_score)), 2)
        
        results.append({
            "filename": filename,
            "score": score
        })
        
    # Sort results descending
    results.sort(key=lambda x: x['score'], reverse=True)
    
    return jsonify({
        "results": results
    })

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)
