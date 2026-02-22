import re

def clean_resume_text(text):
    # 1. Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # 2. Fix broken words like "Bhak are" → "Bhakare"
    text = re.sub(r'(\w)\s+(\w)', r'\1\2', text)

    # 3. Remove weird line breaks
    text = text.replace("\n", " ")

    # 4. Strip leading/trailing spaces
    return text.strip()