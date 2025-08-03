// Header.jsx
import React from 'react';

export default function Header({ onShowHistory }) {
  return (
    <header className="w-full sticky top-0 z-50 bg-[#003366] text-white px-8 py-4 shadow-md flex justify-between items-center">
      {/* Logo */}
      <div className="flex items-center font-bold text-xl">
        <span className="text-yellow-400 mr-2">🔒</span>
        SmartContractScanner
      </div>

      {/* Navigation */}
      <div className="flex items-center space-x-6">
        <nav className="flex space-x-6">
          <a href="#upload" className="hover:underline">Upload & Scan</a>
          <button onClick={onShowHistory} className="hover:underline">History</button>
          <a href="#about" className="hover:underline">About</a>
        </nav>

        <button className="bg-yellow-400 text-black px-4 py-2 rounded hover:bg-yellow-300">
          Login
        </button>
      </div>
    </header>
  );
}
