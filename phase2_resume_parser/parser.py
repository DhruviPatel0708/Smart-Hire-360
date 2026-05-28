import re
import spacy

nlp = spacy.load("en_core_web_sm")

# ==========================================
# EXTRACT EMAIL
# ==========================================

def extract_email(text):

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"

    emails = re.findall(email_pattern, text)

    if emails:
        return emails[0]

    return "Not Found"


# ==========================================
# EXTRACT NAME
# ==========================================

def extract_name(text):

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return "Not Found"


# ==========================================
# EXTRACT SKILLS
# ==========================================

def extract_skills(text):

    skills_list = [
        "python",
        "java",
        "flask",
        "django",
        "mongodb",
        "sql",
        "machine learning",
        "deep learning",
        "aws",
        "docker",
        "html",
        "css",
        "javascript",
        "react",
        "nodejs",
        "data science",
        "nlp",
        "tensorflow",
        "pandas",
        "numpy"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skills_list:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


# ==========================================
# EXTRACT EXPERIENCE
# ==========================================

def extract_experience(text):

    experience_pattern = r'(\d+)\s+years'

    match = re.search(experience_pattern, text.lower())

    if match:
        return match.group(1) + " years"

    return "Not Found"


# ==========================================
# EXTRACT EDUCATION
# ==========================================

def extract_education(text):

    education_keywords = [
        "b.tech",
        "m.tech",
        "bachelor",
        "master",
        "bsc",
        "msc",
        "phd",
        "mba"
    ]

    found_education = []

    text_lower = text.lower()

    for edu in education_keywords:

        if edu in text_lower:
            found_education.append(edu)

    return found_education
# MAIN found_education
def parse_resume(text):

    data = {

        "email": extract_email(text),

        "name": extract_name(text),

        "skills": extract_skills(text),

        "experience": extract_experience(text),

        "education": extract_education(text)

    }

    return data