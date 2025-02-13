import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [file1, setFile1] = useState(null);
  const [file2, setFile2] = useState(null);
  const [result, setResult] = useState(null);

  const handleFile1Change = (event) => {
    setFile1(event.target.files[0]);
  };

  const handleFile2Change = (event) => {
    setFile2(event.target.files[0]);
  };

  const handleCompare = async () => {
    if (!file1 || !file2) {
      alert("Please select two images first!");
      return;
    }

    const formData = new FormData();
    formData.append("file1", file1);
    formData.append("file2", file2);

    try {
      const response = await axios.post("http://127.0.0.1:8000/compare/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setResult(response.data);
    } catch (error) {
      console.error("Error comparing images:", error);
      setResult(null);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">🔍 Image Similarity Checker</h1>

      <input type="file" onChange={handleFile1Change} className="mb-2" />
      <input type="file" onChange={handleFile2Change} className="mb-4" />
      <button
        onClick={handleCompare}
        className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-700"
      >
        Compare Images
      </button>

      {result && (
        <div className="mt-4 p-4 bg-white shadow-md rounded-lg">
          <p>📊 pHash Similarity: {Math.round(result.pHash_similarity * 100)}%</p>
          <p>🔍 ORB Similarity: {Math.round(result.ORB_similarity * 100)}%</p>
        </div>
      )}
    </div>
  );
};

export default App;
