import re

def clean_resume_text(text):
    # 1. Replace newlines with space
    text = text.replace("\n", " ")

    # 2. Add space between lowercase and uppercase letters (FullStack → Full Stack)
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    # 3. Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # 4. Fix spaced letters (Bhak are → Bhakare)
    text = re.sub(r'(\b[A-Za-z])\s+(?=[a-z])', r'\1', text)

    return text.strip()