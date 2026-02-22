def calculate_ats_score(resume_text, match_score):
    score = 0

    # 1️⃣ Skill Match Weight (50%)
    score += match_score * 0.5

    # 2️⃣ Resume Length Quality (20%)
    word_count = len(resume_text.split())
    if 200 <= word_count <= 800:
        score += 20
    elif word_count > 100:
        score += 10
    else:
        score += 5

    # 3️⃣ Section Presence (30%)
    sections = ["skills", "projects", "experience", "education"]
    found_sections = sum(1 for sec in sections if sec.lower() in resume_text.lower())
    section_score = (found_sections / len(sections)) * 30
    score += section_score

    return int(score)