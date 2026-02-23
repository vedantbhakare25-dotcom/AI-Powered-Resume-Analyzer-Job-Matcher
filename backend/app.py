from flask import Flask, request, jsonify
from flask_cors import CORS
from services.parser import extract_text_from_pdf
from services.skill_extractor import extract_skills
from services.text_cleaner import clean_resume_text
from services.matcher import match_skills
from services.summarize import generate_summary
from services.ats_scorer import calculate_ats_score
from services.role_mapper import get_role_skills

app = Flask(__name__)
CORS(app)

@app.route("/api/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files:
        return jsonify({"message": "No resume file uploaded"}), 400

    file = request.files.get("resume")
    job_role = request.form.get("job_role", "")
    job_description = request.form.get("job_description", "")

    # 1️⃣ Extract resume text
    resume_text = extract_text_from_pdf(file)

    # 2️⃣ Clean text
    resume_text = clean_resume_text(resume_text)

    # 3️⃣ Generate professional summary
    summary = generate_summary(resume_text)

    # 4️⃣ Extract resume skills
    skills = extract_skills(resume_text)

    # 5️⃣ Determine JD skills properly
    if job_description.strip():
        jd_skills = extract_skills(job_description)

    elif job_role.strip():
        # If role matches predefined roles
        mapped = get_role_skills(job_role)
        if mapped:
            jd_skills = mapped
        else:
            # If user typed comma-separated manual skills
            jd_skills = [skill.strip().lower() for skill in job_role.split(",") if skill.strip()]
    else:
        jd_skills = []

    # 6️⃣ Skill matching
    matched, missing, score = match_skills(skills, jd_skills)

    # 7️⃣ ATS Score
    ats_score = calculate_ats_score(resume_text, score)

    # 8️⃣ Suggestions generator
    def generate_suggestions(missing_skills, role_context):
        suggestions = []

        role_context = role_context.lower()

        skill_tips = {
            "aws": "Learn AWS EC2, S3, and deployment pipelines.",
            "docker": "Learn Docker for containerization and microservices deployment.",
            "react": "Practice React hooks, state management, and component architecture.",
            "sql": "Improve SQL joins, indexing, and database optimization.",
            "python": "Strengthen Python OOP, async programming, and API design.",
            "flask": "Build scalable REST APIs with Flask and learn production deployment.",
            "machine learning": "Study regression, classification, and model evaluation using sklearn."
        }

        for skill in missing_skills:
            skill_lower = skill.lower()

            if skill_lower in skill_tips:
                suggestions.append(
                    f"For {role_context.title()} roles: {skill_tips[skill_lower]}"
                )
            else:
                suggestions.append(
                    f"For {role_context.title()} roles: Gain practical knowledge in {skill}."
                )

        return suggestions

    role_context = job_role if job_role else job_description
    suggestions = generate_suggestions(missing, role_context)

    return jsonify({
        "message": "Resume parsed successfully",
        "job_role": job_role,
        "filename": file.filename,
        "text_length": len(resume_text),
        "skills": skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "suggestions": suggestions,
        "match_score": score,
        "ats_score": ats_score,
        "summary": summary
    }), 200


if __name__ == "__main__":
    app.run(debug=True)