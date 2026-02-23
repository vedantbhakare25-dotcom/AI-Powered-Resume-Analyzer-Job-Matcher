import React, { useState } from "react";
import axios from "axios";

function UploadResume() {
  const [file, setFile] = useState(null);
  const [jobRole, setJobRole] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!file) {
      alert("Please upload a resume");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_role", jobRole);

    try {
      const res = await axios.post(
        "http://127.0.0.1:5000/api/analyze",
        formData,
      );
      setResult(res.data);
    } catch (error) {
      console.error(error);
      alert("Error analyzing resume");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Resume Analyzer</h2>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br />
      <br />

      <input
        type="text"
        placeholder="Enter Job Role (e.g., backend developer)"
        value={jobRole}
        onChange={(e) => setJobRole(e.target.value)}
      />
      <br />
      <br />

      <button onClick={handleSubmit}>Analyze Resume</button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Analysis Result</h3>

          <p>
            <strong>Filename:</strong> {result.filename}
          </p>
          <p>
            <strong>Match Score:</strong> {result.match_score}%
          </p>

          <h4>Extracted Skills:</h4>
          <ul>
            {result.skills?.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>

          <h4 style={{ color: "green" }}>Matched Skills:</h4>
          <ul>
            {result.matched_skills?.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>

          <h4 style={{ color: "red" }}>Missing Skills:</h4>
          <ul>
            {result.missing_skills?.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>

          <h4>Suggestions:</h4>
          <ul>
            {result.suggestions?.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          <p>
            <strong>ATS Score:</strong> {result.ats_score}/100
          </p>
          <p style={{ fontSize: "12px", color: "gray" }}>
            Score based on skill match, resume length, and section presence
            heuristics.
          </p>

          <h4>Estimated ATS Compatibility:</h4>
          <p>{result.summary}</p>
        </div>
      )}
    </div>
  );
}

export default UploadResume;
