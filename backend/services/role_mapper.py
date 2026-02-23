def get_role_skills(role_text):
    role_text = role_text.lower()

    role_skill_map = {
        "frontend": ["html", "css", "javascript", "react"],
        "frontend developer": ["html", "css", "javascript", "react"],
        "backend": ["python", "flask", "sql", "api"],
        "backend developer": ["python", "flask", "sql", "api"],
        "full stack": ["html", "css", "javascript", "react", "python", "flask", "sql"],
        "full stack developer": ["html", "css", "javascript", "react", "python", "flask", "sql"],
        "python": ["python", "flask", "sql"],
        "python developer": ["python", "flask", "sql"],
        "data scientist": ["python", "machine learning", "pandas", "numpy", "sql"],
        "ai engineer": ["python", "machine learning", "deep learning", "tensorflow"],
    }

    for key in role_skill_map:
        if key in role_text:
            return role_skill_map[key]

    return []