# 🤖 AI Resume Screener

An AI-powered resume screening tool that ranks candidate resumes based on their similarity to a job description using transformer-based NLP models.

## 📌 Features

- Upload a Job Description (JD)
- Upload multiple resumes (PDF or DOCX)
- Automatically extract text from resumes
- Generate sentence embeddings using `all-MiniLM-L6-v2`
- Rank resumes by semantic similarity
- Intuitive Streamlit frontend

## 🚀 Demo

Screenshot attached in the directory
(app_demo.png)

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP**: [Sentence Transformers](https://www.sbert.net/)
- **PDF/DOCX Parsing**: PyMuPDF (`fitz`), python-docx

## 🗂️ Project Structure
resume-screener/
├── app/
│ ├── matcher.py # Core ranking logic
│ └── resume_parser.py # Resume/JD text extraction
├── streamlit_app.py # Main Streamlit UI
├── requirements.txt
└── README.md

Create Virtual Environment

python -m venv venv
.\venv\Scripts\activate   # Windows

Install Dependencies

pip install -r requirements.txt

Run the App
streamlit run streamlit_app.py
 
