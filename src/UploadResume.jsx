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
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 p-6 flex items-center justify-center">
      <div className="bg-white/20 backdrop-blur-lg shadow-2xl rounded-2xl p-8 w-full max-w-3xl border border-white/30">
        {/* Title */}
        <h1 className="text-3xl font-bold text-white text-center mb-6">
          AI Resume Analyzer
        </h1>
        {/* Upload Form */}
        <div className="mb-6">
          <div className="mb-6">
            <label className="block text-lg font-semibold mb-2">
              Upload Resume
            </label>

            <div className="flex items-center gap-4">
              <label className="cursor-pointer bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2 rounded-xl shadow-lg hover:scale-105 transition">
                Choose File
                <input
                  type="file"
                  className="hidden"
                  onChange={(e) => setFile(e.target.files[0])}
                />
              </label>

              {file && (
                <span className="text-sm text-gray-700 font-medium">
                  {file.name}
                </span>
              )}
            </div>
          </div>
          <button
            onClick={handleSubmit}
            className="w-full bg-black text-white py-3 rounded-lg font-semibold hover:bg-gray-900 transition"
          >
            Analyze Resume
          </button>
        </div>

        {/* Results */}
        {result && (
          <div className="mt-8 bg-white/90 rounded-xl p-6 shadow-xl">
            <h2 className="text-2xl font-bold mb-4 text-gray-800">
              Analysis Result
            </h2>

            <p className="mb-2">
              <strong>Filename:</strong> {result.filename}
            </p>

            {/* Match Score Progress Bar */}
            <div className="mb-6">
              <p className="font-semibold text-gray-700">
                Match Score: {result.match_score}%
              </p>
              <div className="w-full bg-gray-200 rounded-full h-4 mt-2">
                <div
                  className="bg-green-500 h-4 rounded-full transition-all"
                  style={{ width: `${result.match_score}%` }}
                ></div>
              </div>
            </div>

            {/* Extracted Skills */}
            <h3 className="text-lg font-semibold text-gray-800 mb-2">
              Extracted Skills
            </h3>
            <div className="flex flex-wrap gap-2 mb-4">
              {result.skills.map((skill, i) => (
                <span
                  key={i}
                  className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm"
                >
                  {skill}
                </span>
              ))}
            </div>

            {/* Matched Skills */}
            <h3 className="text-lg font-semibold text-green-700 mb-2">
              Matched Skills
            </h3>
            <div className="flex flex-wrap gap-2 mb-4">
              {result.matched_skills.map((skill, i) => (
                <span
                  key={i}
                  className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm"
                >
                  {skill}
                </span>
              ))}
            </div>

            {/* Missing Skills */}
            <h3 className="text-lg font-semibold text-red-700 mb-2">
              Missing Skills
            </h3>
            <div className="flex flex-wrap gap-2 mb-4">
              {result.missing_skills.map((skill, i) => (
                <span
                  key={i}
                  className="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm"
                >
                  {skill}
                </span>
              ))}
            </div>

            {/* Suggestions */}
            <h3 className="text-lg font-semibold text-gray-800 mb-2">
              Suggestions
            </h3>
            <ul className="list-disc pl-5 text-gray-700 mb-4">
              {result.suggestions.map((s, i) => (
                <li key={i}>{s}</li>
              ))}
            </ul>

            {/* ATS Score */}
            <p className="text-lg font-bold text-purple-700">
              ATS Score: {result.ats_score}/100
            </p>

            {/* Summary */}
            <h4 className="text-xl font-bold mt-6 mb-2">Candidate Snapshot</h4>

            <div className="bg-white shadow-xl rounded-2xl p-6 border">
              <p className="text-lg font-semibold text-blue-600">
                {result.profile?.name}
              </p>

              <div className="mt-3 space-y-2 text-gray-700">
                <p>
                  <strong>Skills:</strong> {result.profile?.skills}
                </p>
                <p>
                  <strong>Experience:</strong> {result.profile?.experience}
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default UploadResume;
