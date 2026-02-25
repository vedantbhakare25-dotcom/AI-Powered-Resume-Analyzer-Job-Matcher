import re

def generate_summary(text):
    text = text.replace("\n", " ")

    # Extract Name (first 3 words usually)
    words = text.split()
    name = " ".join(words[:2]) if len(words) > 2 else "Candidate"

    # Extract skills section roughly
    skills_match = re.search(r"skilled in (.+?)[.;]", text.lower())
    skills = skills_match.group(1) if skills_match else "Various technologies"

    # Extract experience line
    exp_match = re.search(r"experience: (.+?)[.;]", text.lower())
    experience = exp_match.group(1) if exp_match else "Relevant project experience"

    return {
        "name": name.title(),
        "skills": skills.title(),
        "experience": experience.title(),
    }