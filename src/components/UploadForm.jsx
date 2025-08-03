import { useState } from "react";

export default function UploadForm() {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [uploadingFile, setUploadingFile] = useState(null);

  const handleDrop = (e) => {
    e.preventDefault();
    const files = Array.from(e.dataTransfer.files).filter(f => f.name.endsWith('.sol'));
    if (files.length) {
      simulateUpload(files);
    }
  };

  const handleFileChange = (e) => {
    const files = Array.from(e.target.files).filter(f => f.name.endsWith('.sol'));
    if (files.length) {
      simulateUpload(files);
    }
  };

  const simulateUpload = (files) => {
    const file = files[0];
    setUploadingFile(file);
    // Giả lập progress
    setTimeout(() => {
      setSelectedFiles(prev => [...prev, file]);
      setUploadingFile(null);
    }, 1000);
  };

  const handleRemove = (index) => {
    setSelectedFiles(prev => prev.filter((_, i) => i !== index));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectedFiles.length) {
      alert("Scanning files...");
    } else {
      alert("Please upload at least one .sol file");
    }
  };

  return (
    <div className="w-full bg-blue-100 p-6 rounded-lg shadow-md">
      <h2 className="text-xl font-bold text-center mb-4">Upload Your Smart Contracts</h2>

      {/* Drag & Drop box */}
      <div
        className="border-2 border-dashed border-gray-400 rounded-lg p-8 text-center cursor-pointer hover:bg-gray-50"
        onDragOver={(e) => e.preventDefault()}
        onDrop={handleDrop}
      >
        <div className="text-4xl mb-2">☁️</div>
        <p>Drag & drop your <strong>.sol</strong> file or{" "}
          <label className="text-blue-600 underline cursor-pointer">
            Browse
            <input type="file" accept=".sol" onChange={handleFileChange} className="hidden" />
          </label>
        </p>
        <p className="text-sm text-gray-500 mt-2">Solidity smart contracts only (.sol)</p>
      </div>

      {/* Uploading file progress */}
      {uploadingFile && (
        <div className="mt-4">
          <p className="text-sm text-gray-700 mb-1">
            Uploading - 1/1 file
          </p>
          <div className="bg-gray-200 rounded-full h-2 mb-1">
            <div className="bg-blue-500 h-2 rounded-full w-2/3"></div>
          </div>
          <div className="flex justify-between items-center bg-gray-100 px-2 py-1 rounded">
            <span className="text-sm">{uploadingFile.name}</span>
            <span>⏳</span>
          </div>
        </div>
      )}

      {/* Uploaded files list */}
      {selectedFiles.length > 0 && (
        <div className="mt-4 w-full">
          <p className="text-sm text-gray-700 mb-1">
            Uploaded - {selectedFiles.length} file{selectedFiles.length > 1 ? 's' : ''}
          </p>
          <div className="space-y-2">
            {selectedFiles.map((file, idx) => (
              <div
                key={idx}
                className="flex justify-between items-center border border-green-400 px-2 py-1 rounded"
              >
                <span className="text-sm">{file.name}</span>
                <button
                  type="button"
                  className="text-red-500"
                  onClick={() => handleRemove(idx)}
                >
                  ❌
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Start Scan */}
      <button
        onClick={handleSubmit}
        className="w-full bg-indigo-700 text-white py-3 rounded mt-6 hover:bg-indigo-800"
      >
        Start Vulnerability Scan
      </button>
    </div>
  );
}
