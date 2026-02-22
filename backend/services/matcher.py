def match_skills(resume_skills, jd_skills):
    """
    resume_skills -> list
    jd_skills -> list (from JD or role mapper)
    """

    resume_set = set([s.lower() for s in resume_skills])
    jd_set = set([s.lower() for s in jd_skills])

    matched = list(resume_set.intersection(jd_set))
    missing = list(jd_set - resume_set)

    score = int((len(matched) / len(jd_set)) * 100) if jd_set else 0

    return matched, missing, score