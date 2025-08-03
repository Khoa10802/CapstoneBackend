export default function Footer() {
  const scrollToSection = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  };

  return (
    <footer className="bg-[#002244] text-white py-8">
      <div className="max-w-7xl mx-auto px-8 grid grid-cols-1 md:grid-cols-5 gap-8 text-sm">
        <div>
          <h2 className="font-bold text-base mb-2">SmartContractScanner</h2>
          <p className="text-gray-400">
            AI-powered smart contract analysis. Upload your smart contract and
            detect vulnerabilities instantly.
          </p>
        </div>

        <div>
          <h3 className="font-bold mb-2">Scan</h3>
          <ul>
            <li>
              <button
                onClick={() => scrollToSection("upload")}
                className="hover:underline"
              >
                Upload
              </button>
            </li>
            <li><span className="text-gray-400">History</span></li>
          </ul>
        </div>

        <div>
          <h3 className="font-bold mb-2">Resources</h3>
          <ul className="text-gray-400 space-y-1">
            <li>AI Model</li>
            <li>Guides & Tutorials</li>
            <li>Help Center</li>
          </ul>
        </div>

        <div>
          <h3 className="font-bold mb-2">Company</h3>
          <ul>
            <li>
              <button
                onClick={() => scrollToSection("about")}
                className="hover:underline"
              >
                About Us
              </button>
            </li>
            <li><span className="text-gray-400">Careers</span></li>
          </ul>
        </div>

        <div>
          <h3 className="font-bold mb-2">Try It Today</h3>
          <button
            onClick={() => scrollToSection("upload")}
            className="bg-yellow-400 text-black px-4 py-2 rounded hover:bg-yellow-300"
          >
            Scan Now
          </button>
        </div>
      </div>

      <p className="text-center text-xs text-gray-400 mt-8">
        ©2025 SmartContractScanner Inc.
      </p>
    </footer>
  );
}
