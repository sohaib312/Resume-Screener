import streamlit as st
from app.resume_parser import extract_text
from app.matcher import rank_resumes
import tempfile

st.title("🧠 AI Resume Screening Tool")

# Upload JD
st.subheader("📄 Upload Job Description")
jd_file = st.file_uploader("Upload JD (PDF or DOCX)", type=["pdf", "docx"])

# Upload Resumes
st.subheader("📑 Upload Resumes")
resume_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

# Process
if jd_file and resume_files:
    with tempfile.NamedTemporaryFile(delete=False, suffix=jd_file.name[-5:]) as tmp_jd:
        tmp_jd.write(jd_file.read())
        jd_text = extract_text(tmp_jd.name)

    resumes = []
    for file in resume_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=file.name[-5:]) as tmp_file:
            tmp_file.write(file.read())
            resumes.append({"filename": file.name, "text": extract_text(tmp_file.name)})

    results = rank_resumes(jd_text, resumes)

    st.success("✅ Matching Complete!")

    st.subheader("📊 Results:")
    for res in results:
        st.write(f"**{res['filename']}** — Match Score: {res['score']}%")
