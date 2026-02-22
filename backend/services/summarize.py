import re

def generate_summary(text):
    # Split into sentences using punctuation
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Filter meaningful sentences (length > 40 chars)
    meaningful = [s.strip() for s in sentences if len(s.strip()) > 40]

    # Return top 3 meaningful sentences
    summary = meaningful[:3]

    return " ".join(summary)
