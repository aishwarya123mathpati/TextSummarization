import re
import pdfplumber
from docx import Document
from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained BART model and tokenizer
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')


# Function to extract text from PDF files
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


# Function to extract text from Word files
def extract_text_from_word(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


# Function to preprocess the extracted text
def preprocess_text(text):
    # Remove unwanted characters like newlines, extra spaces, and page numbers
    text = text.replace('\n', ' ').replace('\r', '')
    text = ' '.join(text.split())  # Remove extra spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    text = text.lower()
    text = re.sub(r'\d+\s?page\s?\d+', '', text)  # Remove page numbers
    return text


# Function to generate a summary using BART
def generate_summary(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# Function to summarize text from different document types
def summarize_document(file_path):
    # Extract text based on file type
    file_extension = file_path.split('.')[-1].lower()
    if file_extension == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif file_extension == 'docx':
        text = extract_text_from_word(file_path)
    else:
        raise ValueError("Unsupported file format")

    # Preprocess the extracted text
    cleaned_text = preprocess_text(text)

    # Generate the summary
    return generate_summary(cleaned_text)
