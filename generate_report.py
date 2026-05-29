from fpdf import FPDF
from datetime import datetime

class ReportPDF(FPDF):
    def header(self):
        # We don't want the header text/line on the cover page
        if self.page_no() > 1:
            self.set_y(15)
            self.set_font('Helvetica', 'I', 9)
            self.set_text_color(100, 116, 139) # Light grey
            self.cell(0, 5, 'AI-Powered Resume Parser - Project Report | Nemapu Navaneeth', align='C')
            self.ln(6)
            
            # Teal Line across the top
            self.set_draw_color(0, 150, 136) # Teal
            self.set_line_width(0.8)
            self.line(20, self.get_y(), 190, self.get_y())
            self.ln(10)

    def chapter_title(self, num, title):
        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(21, 30, 61) # Navy Blue
        self.cell(0, 10, title, border=0, new_x="LMARGIN", new_y="NEXT", align='L')
        
        # Teal accent line directly under title
        self.set_draw_color(0, 150, 136) # Teal
        self.set_line_width(1.5)
        # We estimate the width of the text roughly
        self.line(self.get_x(), self.get_y() + 1, self.get_x() + 90, self.get_y() + 1)
        self.ln(8)

    def chapter_body(self, text, indent=False):
        self.set_font('Helvetica', '', 12)
        self.set_text_color(51, 65, 85) # Slate 700
        if indent:
            self.set_x(25)
        self.multi_cell(0, 8, text)
        self.ln(6)
        
    def add_bullet(self, text):
        self.set_font('Helvetica', '', 12)
        self.set_text_color(51, 65, 85)
        self.set_x(25)
        self.multi_cell(0, 8, f"- {text}")
        self.ln(2)
        
    def add_link_bullet(self, text, url):
        self.set_x(25)
        self.set_font('Helvetica', '', 12)
        self.set_text_color(51, 65, 85)
        
        prefix = f"- {text} "
        w = self.get_string_width(prefix)
        self.cell(w, 8, prefix, new_x="RIGHT", new_y="TOP")
        
        self.set_font('Helvetica', 'U', 12)
        self.set_text_color(0, 150, 136) # Teal
        self.cell(0, 8, '[Link]', new_x="LMARGIN", new_y="NEXT", link=url)
        self.ln(2)

def create_report():
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # ---------------- PAGE 1: Cover Page ----------------
    pdf.add_page()
    
    pdf.set_y(50)
    pdf.set_font('Helvetica', 'B', 28)
    pdf.set_text_color(21, 30, 61) # Navy Blue
    pdf.cell(0, 15, 'AI-Powered Resume Parser', new_x="LMARGIN", new_y="NEXT", align='C')
    
    pdf.set_font('Helvetica', '', 16)
    pdf.set_text_color(0, 150, 136) # Teal
    pdf.cell(0, 10, 'Candidate Screening using TF-IDF & Strict Intersection', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(5)
    
    # Center Teal Line
    pdf.set_draw_color(0, 150, 136)
    pdf.set_line_width(1.5)
    pdf.line(75, pdf.get_y(), 135, pdf.get_y())
    pdf.ln(25)
    
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, 'PROJECT WORK REPORT', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(30)
    
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(21, 30, 61) # Navy Blue
    pdf.cell(0, 8, 'Nemapu Navaneeth', new_x="LMARGIN", new_y="NEXT", align='C')
    
    pdf.set_font('Helvetica', '', 12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 7, 'IIIT Senapati, Manipur', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 7, 'Department of CSE | Semester VI', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 7, 'Contact NO: +91 9381228761', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 7, 'Email ID: navaneethnemapu@gmail.com', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.cell(0, 7, 'Submission Date: 29-05-2026', new_x="LMARGIN", new_y="NEXT", align='C')

    pdf.ln(25)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 7, datetime.now().strftime("%B %Y"), new_x="LMARGIN", new_y="NEXT", align='C')

    # ---------------- PAGE 2: Project Overview ----------------
    pdf.add_page()
    pdf.chapter_title(2, 'Project Overview')
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, 'Problem Statement:', new_x="LMARGIN", new_y="NEXT")
    pdf.chapter_body('Recruiters and HR professionals spend countless hours manually skimming through hundreds of applications to find the best candidate for a job. Existing keyword-matching systems are often flawed or overly simplistic, relying on exact string matches without contextual understanding. There is a critical need for an intelligent, automated resume parser that can read raw physical documents (PDF, DOCX, TXT) in bulk, extract key technical skills, and accurately rank candidates against a target Job Description using advanced Natural Language Processing (NLP).', indent=True)
    
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, 'Objective:', new_x="LMARGIN", new_y="NEXT")
    pdf.chapter_body('To design and build a decoupled, full-stack AI-driven web application. The platform enables recruiters to seamlessly upload candidate resumes (or large batches of resumes in ZIP archives) and instantly receive a mathematically ranked leaderboard of candidates based on their contextual match to a provided Job Description, drastically reducing time-to-hire.', indent=True)
    
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, 'Technologies Used:', new_x="LMARGIN", new_y="NEXT")
    pdf.add_bullet('Python 3.11 (Backend Core & AI Logic)')
    pdf.add_bullet('React.js & Vite (Frontend UI & State Management)')
    pdf.add_bullet('Flask & Flask-CORS (RESTful API Server)')
    pdf.add_bullet('Scikit-Learn (TF-IDF Vectorization & KMeans Clustering)')
    pdf.add_bullet('NLTK (Natural Language Toolkit for Stopword Removal)')
    pdf.add_bullet('PyPDF2 & python-docx (Binary Document Extraction)')
    
    # ---------------- PAGE 3: Dataset Details ----------------
    pdf.add_page()
    pdf.chapter_title(3, 'Dataset Details')
    pdf.chapter_body('To train the initial contextual AI models, a vast dataset of real-world resumes was required to map out the vocabulary of different industries.')
    pdf.ln(5)
    pdf.add_bullet('Dataset Name: UpdatedResumeDataSet')
    pdf.add_bullet('Dataset Source: Kaggle')
    pdf.add_bullet('Number of Records: 962 Resumes')
    pdf.add_bullet('Number of Categories: 25 distinct job roles (e.g., Data Science, HR, Mechanical Engineer)')
    pdf.add_bullet('Dataset Link: Embedded locally within project repository.')
    
    try:
        pdf.ln(10)
        pdf.image('cluster_distribution.png', x=15, w=180)
        pdf.set_font('Helvetica', 'I', 10)
        pdf.set_text_color(100, 116, 139)
        pdf.ln(5)
        pdf.cell(0, 6, 'Figure 1: Distribution of 962 Resumes across 25 Job Categories in the Training Dataset', align='C', new_x="LMARGIN", new_y="NEXT")
    except:
        pdf.chapter_body('[Graph: cluster_distribution.png not found]')

    # ---------------- PAGE 4: Project Workflow ----------------
    pdf.add_page()
    pdf.chapter_title(4, 'Project Workflow')
    pdf.chapter_body("The system follows a strict, 7-step automated pipeline from data ingestion to candidate scoring:")
    pdf.ln(5)
    pdf.add_bullet('1. Data Collection: Sourced 962 raw text resumes spanning 25 industries from Kaggle.')
    pdf.add_bullet('2. Data Preprocessing: Deployed an NLTK pipeline to strip punctuation, convert text to lowercase, remove English stop words, and tokenize the remaining critical nouns/verbs.')
    pdf.add_bullet('3. AI Initialization: Trained a TF-IDF Vectorizer to mathematically weight rare technical terms, and fitted a KMeans clustering model to map the semantic relationships between the resumes.')
    pdf.add_bullet('4. Frontend Integration: Built a responsive, modern React UI featuring glassmorphism design, allowing users to paste Job Descriptions and upload batch files.')
    pdf.add_bullet('5. Backend Processing: Flask REST API receives the multipart form data, unpacks ZIP files in memory, and extracts raw text using PyPDF2 and python-docx.')
    pdf.add_bullet('6. Matching Engine: The server calculates the strict contextual keyword overlap ratio between the Candidate and the target Job Description.')
    pdf.add_bullet('7. Result Prediction: The backend algorithm scores the match on a 0.0 to 10.0 scale and returns a sorted JSON array to the React UI for rendering as a Leaderboard.')

    # ---------------- PAGE 5: Model / Algorithm Used ----------------
    pdf.add_page()
    pdf.chapter_title(5, 'Model / Algorithm Used')
    pdf.chapter_body('The system relies on a hybrid approach using established ML clustering and custom deterministic extraction.')
    pdf.ln(5)
    pdf.add_bullet('TF-IDF (Term Frequency-Inverse Document Frequency)')
    pdf.add_bullet('KMeans Clustering (k=25)')
    pdf.add_bullet('Custom Deterministic Set-Intersection Matching Algorithm')
    pdf.ln(10)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, 'Why Selected:', new_x="LMARGIN", new_y="NEXT")
    pdf.chapter_body("Initially, TF-IDF and KMeans were selected to understand the broader context of the resume dataset. The vectorizer successfully mapped words into mathematical space, allowing the KMeans model to group similar resumes together. However, a critical flaw was discovered during testing: The global TF-IDF model suffered from 'Vocabulary Blind Spots'. If a user uploaded a Job Description for a 'Nurse', the model ignored the word 'Nurse' entirely because it wasn't present in the Kaggle dataset vocabulary (which was limited to 1000 features).", indent=True)
    pdf.chapter_body("To solve this, the final candidate scoring was shifted away from predictive Cosine Similarity. Instead, a Custom Deterministic Set-Intersection Algorithm was deployed. This algorithm bypasses the global vocabulary entirely. It dynamically extracts the exact vocabulary from the user's uploaded Job Description in real-time, counts the strict intersections with the Resume, and mathematically calculates an exact Keyword Overlap Ratio. This guarantees 100% precision in keyword filtering and successfully punishes unrelated domain resumes.", indent=True)

    # ---------------- PAGE 6: Implementation ----------------
    pdf.add_page()
    pdf.chapter_title(6, 'Implementation')
    pdf.chapter_body('The implementation of this project follows a microservices approach, completely separating the AI Engine from the User Interface.')
    pdf.ln(2)
    pdf.add_bullet('Important Code Snippets: Provided in the Source Code ZIP (see app.py for the strict scoring algorithm, and preprocessing.py for the NLTK pipeline).')
    pdf.add_bullet('Architecture: Fully decoupled Client-Server architecture running concurrently. React is served via Vite on Port 5173, while Flask handles heavy AI processing on Port 5000.')
    pdf.add_bullet('Accuracy Evaluation: The underlying KMeans baseline model achieved 71.10% classification accuracy on 25 distinct job categories without supervised labels.')
    
    try:
        pdf.ln(5)
        pdf.image('architecture.png', x=15, w=180)
        pdf.set_font('Helvetica', 'I', 10)
        pdf.set_text_color(100, 116, 139)
        pdf.ln(2)
        pdf.cell(0, 6, 'Figure 2: Decoupled AI Pipeline Architecture', align='C', new_x="LMARGIN", new_y="NEXT")
        pdf.ln(10)
    except Exception as e:
        pdf.chapter_body(f'[Graph: architecture.png not found] {e}')

    # ---------------- PAGE 7: Results ----------------
    pdf.add_page()
    pdf.chapter_title(7, 'Results & Performance Analysis')
    pdf.chapter_body('The system effectively parses diverse file types (PDF, Word, TXT) and outputs highly accurate predictions mapped to a beautiful 0.0 - 10.0 leaderboard scale in the React UI.')
    
    try:
        pdf.ln(5)
        pdf.image('category_accuracy.png', x=15, w=180)
        pdf.set_font('Helvetica', 'I', 10)
        pdf.set_text_color(100, 116, 139)
        pdf.ln(5)
        pdf.cell(0, 6, 'Figure 3: AI Model Classification Accuracy across 25 Job Categories', align='C', new_x="LMARGIN", new_y="NEXT")
        pdf.ln(10)
    except:
        pdf.chapter_body('[Graph: category_accuracy.png not found]')

    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, 'Performance Analysis:', new_x="LMARGIN", new_y="NEXT")
    pdf.chapter_body('As shown in Figure 3, the baseline AI clustering model achieved 100% accuracy on distinct, highly technical domains such as Civil Engineering, SAP Development, and Blockchain. However, it struggled with overly generic titles (e.g., Advocate, Automation Testing) because those resumes shared too much generic vocabulary with adjacent fields.', indent=True)
    pdf.chapter_body('To counter this, the custom Set-Intersection Scoring Engine was built. This engine successfully identifies perfect matches (scoring > 8.0/10.0) while correctly punishing totally unrelated resumes. For example, testing a Technical Resume against a Nursing Job Description accurately yields a strict 0.0 score due to the robust 20% overlap penalty threshold.', indent=True)

    # ---------------- PAGE 8: Challenges Faced ----------------
    pdf.add_page()
    pdf.chapter_title(8, 'Challenges Faced')
    pdf.chapter_body('During development, several complex architectural and AI-related hurdles were overcome.')
    pdf.ln(5)
    pdf.add_bullet('Vocabulary Blind Spots: The initial AI model ignored words outside of its training dataset. This was fixed by implementing a dynamic vocabulary engine based strictly on the uploaded Job Description.')
    pdf.add_bullet('False Positives: Common resume fluff words (e.g., "experience", "seeking", "certified") artificially inflated cosine similarity scores. Fixed by switching to a direct Keyword Overlap Ratio that mathematically calculates strict noun intersections.')
    pdf.add_bullet('File Extraction & Bulk Uploads: Handling multiple disparate file formats (PDF, DOCX) and nested zip archives required custom in-memory stream processing using `io.BytesIO`. This prevents cluttering the server disk with temporary files while safely parsing thousands of candidate documents concurrently.')
    pdf.add_bullet('CORS and Microservices: Splitting the app into React and Flask caused Cross-Origin Resource Sharing blocks. Resolved by implementing the Flask-CORS middleware for secure inter-process communication.')

    # ---------------- PAGE 9: Conclusion ----------------
    pdf.add_page()
    pdf.chapter_title(9, 'Conclusion')
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, 'What was achieved:', new_x="LMARGIN", new_y="NEXT")
    pdf.chapter_body('We successfully engineered a full-stack, decoupled AI resume parser that can ingest batch files, parse complex binary documents natively, and accurately score candidates against a dynamic job description in real-time. The React-based UI provides a seamless, premium, glassmorphism experience for recruiters, abstracting away the complex Python AI pipeline.', indent=True)
    
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 8, 'Future improvements:', new_x="LMARGIN", new_y="NEXT")
    pdf.chapter_body('1. Semantic NLP Integration: Integrating advanced Word Embeddings (like Word2Vec or BERT) to provide Semantic Matching. This would allow the AI to recognize that terms like "iOS" and "Swift" are highly related concepts, rather than relying purely on exact string keyword intersections.', indent=True)
    pdf.chapter_body('2. Cloud Deployment: Containerizing the React and Flask applications using Docker and deploying them to a managed cloud service like AWS or Google Cloud for global scalability.', indent=True)

    # ---------------- PAGE 10: References ----------------
    pdf.add_page()
    pdf.chapter_title(10, 'References')
    pdf.chapter_body('The following resources and documentation were vital to the successful completion of this project.')
    pdf.ln(5)
    pdf.add_link_bullet('Dataset: Kaggle "UpdatedResumeDataSet"', 'https://www.kaggle.com/datasets/jillanisofttech/updated-resume-dataset')
    pdf.add_link_bullet('Machine Learning: Scikit-Learn Official Documentation', 'https://scikit-learn.org/')
    pdf.add_link_bullet('Natural Language Processing: NLTK Documentation', 'https://www.nltk.org/')
    pdf.add_link_bullet('Frontend Development: React.js & Vite Frameworks', 'https://react.dev/')
    pdf.add_link_bullet('Backend API: Flask API Framework', 'https://flask.palletsprojects.com/')
    pdf.add_link_bullet('Document Parsing: PyPDF2 Documentation', 'https://pypi.org/project/PyPDF2/')

    # ---------------- PAGE 11: Thank You ----------------
    pdf.add_page()
    
    # Vertically center the text
    pdf.set_y(120)
    
    pdf.set_font('Helvetica', 'B', 32)
    pdf.set_text_color(21, 30, 61) # Navy Blue
    pdf.cell(0, 15, 'Thank You', new_x="LMARGIN", new_y="NEXT", align='C')
    
    pdf.set_font('Helvetica', 'I', 16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, '- Nemapu Navaneeth', new_x="LMARGIN", new_y="NEXT", align='C')

    pdf.output('Navaneeth_ResumeParser.pdf')
    print("11-Page Designed PDF generated successfully: Navaneeth_ResumeParser.pdf")

if __name__ == '__main__':
    create_report()
