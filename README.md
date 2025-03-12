# Text Summarization Web Application using Flask and BART

This project is a web application that allows users to upload a PDF or Word document, and it generates a summary of the document using the BART model for text 
summarization. The application is built using Flask and leverages the Hugging Face Transformers library to utilize the pre-trained facebook/bart-large-cnn model.

**Features:**
- Upload PDF or Word documents
- Text extraction from PDF and Word documents
- Summarize the extracted text using the BART model
- Returns the generated summary through a simple web interface


**Requirements:**

- Before running this application, ensure you have the following dependencies installed:

- Flask - Web framework to handle HTTP requests.
- Transformers - Hugging Face library to load the pre-trained BART model for summarization.
- Torch - Backend required by Hugging Face models.
- pdfplumber - To extract text from PDF documents.
- python-docx - To extract text from Word documents.

**Setup Instructions:**

Clone the Repository:

   git clone <repository_url>
   cd text-summarization-flask


**Ensure the following structure exists:**

- app.py: Flask application that manages routes and file uploads.
- model/summarization.py: Contains functions for text extraction and summarization.
- templates/index.html: Frontend interface where users upload documents.
- uploads/: Directory where the uploaded files are saved temporarily.
- Running the Application:


**To run the Flask application, use the following command:**

'python app.py'

This will start a local development server at http://127.0.0.1:5000/.

Accessing the Application:

Open a web browser and navigate to:

http://127.0.0.1:5000/
You should see the web interface with an upload form.

Uploading a Document:

Click the "Choose File" button to upload a PDF or Word document.
After uploading, the server will extract the text and generate a summary using the BART model.
The generated summary will be displayed on the page.
