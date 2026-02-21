from services.skills_db import SKILL_SET
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))

def extract_skills(resume_text):
    tokens = word_tokenize(resume_text.lower())

    filtered_tokens = [
        word for word in tokens if word.isalpha() and word not in stop_words
    ]

    extracted = set()
    for token in filtered_tokens:
        if token in SKILL_SET:
            extracted.add(token)

    return list(extracted)