import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

def download_nltk_data():
    try:
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('stopwords')
        nltk.download('wordnet')
        nltk.download('punkt')
        nltk.download('punkt_tab')

def clean_resume_text(text):
    """
    Cleans the resume text by removing URLs, RTs, CCs, hashtags, 
    mentions, extra whitespaces, and special characters.
    """
    text = re.sub('http\S+\s*', ' ', text)  # remove URLs
    text = re.sub('RT|cc', ' ', text)  # remove RT and cc
    text = re.sub('#\S+', '', text)  # remove hashtags
    text = re.sub('@\S+', '  ', text)  # remove mentions
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # remove punctuations
    text = re.sub(r'[^\x00-\x7f]',r' ', text) 
    text = re.sub('\s+', ' ', text)  # remove extra whitespace
    return text.lower()

def preprocess_text(text):
    """
    Tokenizes, removes stopwords, and lemmatizes the cleaned text.
    """
    # Tokenization
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    
    return ' '.join(lemmatized_tokens)

def load_and_preprocess_data(filepath):
    """
    Loads dataset and applies preprocessing steps.
    """
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    
    print("Cleaning and preprocessing resume text...")
    df['cleaned_resume'] = df['Resume'].apply(clean_resume_text)
    
    download_nltk_data()
    df['processed_resume'] = df['cleaned_resume'].apply(preprocess_text)
    
    return df

if __name__ == "__main__":
    download_nltk_data()
