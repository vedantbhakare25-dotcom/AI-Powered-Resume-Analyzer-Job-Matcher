from services.skills_db import SKILL_SET
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))

# 🔥 Normalize common skill variants
NORMALIZATION_MAP = {
    "java script": "javascript",
    "react.js": "react",
    "node.js": "node",
    "machine learning": "machine learning",
    "deep learning": "deep learning"
}

def normalize_text(text):
    text = text.lower()

    # Replace multi-word and dotted variants
    for variant, standard in NORMALIZATION_MAP.items():
        text = text.replace(variant, standard)

    return text

def extract_skills(resume_text):
    # 1️⃣ Normalize problematic patterns first
    resume_text = normalize_text(resume_text)

    # 2️⃣ Tokenize
    tokens = word_tokenize(resume_text)

    # 3️⃣ Remove stopwords & keep alphabets
    filtered_tokens = [
        word for word in tokens if word.isalpha() and word not in stop_words
    ]

    # 4️⃣ Extract skills
    extracted = set()
    for token in filtered_tokens:
        if token in SKILL_SET:
            extracted.add(token)

    return list(extracted)