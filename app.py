import streamlit as st
from resume_generator import generate_resume
from docx import Document
import io

st.set_page_config(page_title="AI Resume Builder", layout="centered")

st.title("AI Resume & Portfolio Builder")
st.write("Generate professional ATS-optimized resumes instantly.")

# User Inputs
st.header("Enter Your Details")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
education = st.text_area("Education Details")
skills = st.text_area("Skills (comma separated)")
projects = st.text_area("Projects")
experience = st.text_area("Work Experience")
job_role = st.text_input("Target Job Role")

if st.button("Generate Resume"):

    if name and education and skills:
        resume_text = generate_resume(
            name, email, phone,
            education, skills,
            projects, experience,
            job_role
        )

        st.subheader("Generated Resume")
        st.text_area("Preview", resume_text, height=400)

        # Create DOCX
        doc = Document()
        doc.add_paragraph(resume_text)

        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        st.download_button(
            label="Download Resume (DOCX)",
            data=buffer,
            file_name=f"{name}_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    else:
        st.error("Please fill required fields.")
