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
        formData
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

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <br /><br />

      <input
        type="text"
        placeholder="Enter job skills (comma separated)"
        value={jobRole}
        onChange={(e) => setJobRole(e.target.value)}
      />
      <br /><br />

      <button onClick={handleSubmit}>Analyze Resume</button>
    {result && (
    <div>
        <h3>Response:</h3>
        <p>Message: {result.message}</p>
        <p>Job Role: {result.job_role}</p>
        <p>Filename: {result.filename}</p>
        <p>Text Length: {result.text_length}</p>
        <p>Preview: {result.preview}</p>
    </div>
    )}
    </div>
  );
}

export default UploadResume;