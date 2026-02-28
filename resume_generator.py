import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_resume(name, email, phone, education, skills, projects, experience, job_role):

    prompt = f"""
    Create a professional ATS-optimized resume for the role of {job_role}.

    Name: {name}
    Email: {email}
    Phone: {phone}

    Education:
    {education}

    Skills:
    {skills}

    Projects:
    {projects}

    Experience:
    {experience}

    Format it properly with sections:
    - Professional Summary
    - Education
    - Skills
    - Projects
    - Experience
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional resume writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800
    )

    return response.choices[0].message["content"]
