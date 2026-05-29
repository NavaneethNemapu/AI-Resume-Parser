# AI-Powered Resume Parser & Matcher

Welcome to the **AI-Powered Resume Parser**, a decoupled full-stack web application designed to automate candidate screening. This system processes raw physical documents (PDF, DOCX) and accurately ranks candidates against a target Job Description using advanced Natural Language Processing (NLP).

## 🚀 Key Features
- **Intelligent Document Parsing**: Automatically extracts text from uploaded PDF and DOCX files.
- **Dynamic Contextual Scoring**: Bypasses traditional word-matching blind spots by dynamically extracting exact vocabulary from the target Job Description in real-time.
- **Strict Overlap Penalty**: Punishes unrelated domain resumes with a harsh cutoff threshold to ensure 100% precision in keyword filtering.
- **Modern User Interface**: A responsive, premium Glassmorphism-style dashboard built with React.js that displays a real-time leaderboard of candidates.
- **Batch Processing**: Supports uploading massive batches of resumes inside nested ZIP archives, processed entirely in-memory to preserve server disk space.

## 🛠️ Technology Stack
### Frontend (Client)
- **React.js & Vite**: Lightning-fast UI rendering and state management.
- **Vanilla CSS**: Custom Glassmorphism design system.

### Backend (Server & AI Engine)
- **Python 3.11**: Core AI logic.
- **Flask**: RESTful API Server.
- **Flask-CORS**: Secure Cross-Origin Resource Sharing.
- **Scikit-Learn**: TF-IDF Vectorization & KMeans Clustering baseline models.
- **NLTK (Natural Language Toolkit)**: Text preprocessing, stop-word removal, and tokenization.
- **PyPDF2 & python-docx**: Binary document extraction.

---

## ⚙️ Local Setup & Installation

This project uses a decoupled microservices architecture. You will need to run the **Backend** and **Frontend** servers concurrently in two separate terminal windows.

### 1. Backend (Flask API) Setup
Open a terminal in the root project directory:
```bash
# 1. (Optional) Create a virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows

# 2. Install Python dependencies
pip install -r requirement.txt

# 3. Run the Flask Server
python app.py
```
*The Flask API will start running on `http://127.0.0.1:5000`*

### 2. Frontend (React UI) Setup
Open a **new** second terminal and navigate to the frontend directory:
```bash
# 1. Navigate to the frontend directory
cd frontend

# 2. Install Node dependencies
npm install

# 3. Start the Vite development server
npm run dev
```
*The React UI will start running on `http://localhost:5173`*

---

## 📈 Project Report & Architecture
A comprehensive 12-page PDF report detailing the AI methodology, dataset distribution (Kaggle), and the complete custom set-intersection algorithm is included in this repository:
👉 `Navaneeth_ResumeParser.pdf`

## 👨‍💻 Author
**Nemapu Navaneeth**  
Computer Science Engineering, 2023 - 2027  
Indian Institute of Information Technology, Senapati, Manipur
