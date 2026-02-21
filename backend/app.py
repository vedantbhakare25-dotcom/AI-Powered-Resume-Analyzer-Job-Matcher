from flask import Flask, request, jsonify
from flask_cors import CORS
from services.parser import extract_text_from_pdf
from services.skill_extractor import extract_skills

app = Flask(__name__)
CORS(app)

@app.route("/api/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files:
        return jsonify({"message": "No resume file uploaded"}), 400

    file = request.files.get("resume")
    job_role = request.form.get("job_role", "")

    # Step 1: Extract resume text
    resume_text = extract_text_from_pdf(file)

    # Step 2: NLP Skill Extraction
    skills = extract_skills(resume_text)

    # Step 3: Return response with skills
    return jsonify({
        "message": "Resume parsed successfully",
        "job_role": job_role,
        "filename": file.filename,
        "text_length": len(resume_text),
        "skills": skills,   # ⭐ NEW FIELD
        "preview": resume_text[:300]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)