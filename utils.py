import os
import zipfile
import io
import PyPDF2
import docx

def extract_text_from_pdf(file_stream):
    try:
        reader = PyPDF2.PdfReader(file_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_text_from_docx(file_stream):
    try:
        doc = docx.Document(file_stream)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return ""

def extract_text_from_txt(file_stream):
    try:
        return file_stream.read().decode('utf-8')
    except Exception as e:
        print(f"Error reading TXT: {e}")
        return ""

def process_uploaded_file(file_obj, filename):
    """
    Processes a single file (PDF, DOCX, TXT, or ZIP).
    Returns a dictionary of {filename: text_content}.
    """
    results = {}
    ext = os.path.splitext(filename.lower())[1]

    if ext == '.zip':
        try:
            with zipfile.ZipFile(file_obj) as z:
                for zinfo in z.infolist():
                    if zinfo.is_dir() or zinfo.filename.startswith('__MACOSX'):
                        continue
                        
                    inner_ext = os.path.splitext(zinfo.filename.lower())[1]
                    if inner_ext in ['.pdf', '.docx', '.txt']:
                        with z.open(zinfo.filename) as inner_file:
                            file_stream = io.BytesIO(inner_file.read())
                            
                            if inner_ext == '.pdf':
                                text = extract_text_from_pdf(file_stream)
                            elif inner_ext == '.docx':
                                text = extract_text_from_docx(file_stream)
                            elif inner_ext == '.txt':
                                text = extract_text_from_txt(file_stream)
                                
                            if text.strip():
                                results[zinfo.filename] = text
        except Exception as e:
            print(f"Error reading ZIP: {e}")
            
    else:
        # Single file
        if ext == '.pdf':
            text = extract_text_from_pdf(file_obj)
        elif ext == '.docx':
            text = extract_text_from_docx(file_obj)
        elif ext == '.txt':
            text = extract_text_from_txt(file_obj)
        else:
            text = ""
            
        if text.strip():
            results[filename] = text

    return results
