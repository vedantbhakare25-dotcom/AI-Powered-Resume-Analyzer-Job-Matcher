from flask import Flask, request, jsonify
from flask_cors import CORS
from services.parser import extract_text_from_pdf
from services.skill_extractor import extract_skills
from services.text_cleaner import clean_resume_text

app = Flask(__name__)
CORS(app)

@app.route("/api/analyze", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files:
        return jsonify({"message": "No resume file uploaded"}), 400

    file = request.files.get("resume")
    job_role = request.form.get("job_role", "")

    # Step 1: Extract raw text
    resume_text = extract_text_from_pdf(file)

    # Step 2: Clean OCR noise
    resume_text = clean_resume_text(resume_text)

    # Step 3: Extract skills
    skills = extract_skills(resume_text)
    
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