from flask import Flask, request, jsonify
from flask_cors import CORS
from services.parser import extract_text_from_pdf
from services.skill_extractor import extract_skills
from services.text_cleaner import clean_resume_text
from services.matcher import match_skills
from services.summarize import generate_summary
from services.ats_scorer import calculate_ats_score
from services.role_mapper import get_role_skills
from services.roadmap_generator import generate_learning_roadmap

app = Flask(__name__)
CORS(app)

@app.route("/api/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files:
        return jsonify({"message": "No resume file uploaded"}), 400

    file = request.files.get("resume")
    job_role = request.form.get("job_role", "").strip().lower()

    # 1️⃣ Extract resume text
    resume_text = extract_text_from_pdf(file)

    # 2️⃣ Clean text
    resume_text = clean_resume_text(resume_text)

    # 3️⃣ Generate professional summary
    summary = generate_summary(resume_text)

    # 4️⃣ Extract resume skills
    skills = extract_skills(resume_text)
    skills = [s.lower() for s in skills]

    # 5️⃣ Get predefined role skills
    jd_skills = get_role_skills(job_role) if job_role else []
    jd_skills = [s.lower() for s in jd_skills]

    # 6️⃣ Skill matching
    matched, missing, score = match_skills(skills, jd_skills)

    # 7️⃣ ATS Score
    ats_score = calculate_ats_score(resume_text, score)

    # 8️⃣ Suggestions generator
    def generate_suggestions(missing_skills, role_context):
        suggestions = []

        skill_tips = {
            "aws": "Learn AWS EC2, S3, and deployment pipelines.",
            "docker": "Learn Docker for containerization and deployment.",
            "react": "Practice React hooks, state management, and components.",
            "sql": "Improve SQL joins, indexing, and optimization.",
            "python": "Strengthen Python OOP and backend development.",
            "flask": "Build REST APIs using Flask and learn deployment.",
            "machine learning": "Study regression, classification, and sklearn."
        }

        for skill in missing_skills:
            if skill in skill_tips:
                suggestions.append(f"For {role_context.title()} roles: {skill_tips[skill]}")
            else:
                suggestions.append(f"For {role_context.title()} roles: Gain practical knowledge in {skill}.")

        return suggestions

    suggestions = generate_suggestions(missing, job_role if job_role else "developer")
    roadmap = generate_learning_roadmap(job_role, missing)
    return jsonify({
        "message": "Resume parsed successfully",
        "job_role": job_role,
        "filename": file.filename,
        "text_length": len(resume_text),
        "skills": skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "suggestions": suggestions,
        "learning_roadmap": roadmap,
        "match_score": score,
        "ats_score": ats_score,
        "summary": summary
    }), 200


if __name__ == "__main__":
    app.run(debug=True)