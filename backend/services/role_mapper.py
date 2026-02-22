def get_role_skills(role_text):
    role_text = role_text.lower()

    role_skill_map = {
        "frontend developer": ["html", "css", "javascript", "react"],
        "backend developer": ["python", "flask", "sql", "api"],
        "full stack developer": ["html", "css", "javascript", "react", "python", "flask", "sql"],
        "python developer": ["python", "flask", "sql"],
        "data scientist": ["python", "machine learning", "pandas", "numpy", "sql"],
        "ai engineer": ["python", "machine learning", "deep learning", "tensorflow"],
    }

    return role_skill_map.get(role_text.lower(), [])