// HistorySidebar.jsx
export default function HistorySidebar({ isOpen, onClose }) {
  return (
    <div
      className={`fixed top-0 right-0 h-full w-80 bg-white shadow-lg z-50 transform transition-transform duration-300 ease-in-out
      ${isOpen ? "translate-x-0" : "translate-x-full"}`}
    >
      <div className="flex justify-between items-center p-4 border-b">
        <h2 className="text-lg font-bold">Scan History</h2>
        <button onClick={onClose} className="text-gray-600 hover:text-black text-xl">&times;</button>
      </div>

      <div className="p-4 space-y-4 overflow-y-auto h-full">
        {/* Example Card */}
        <div className="border rounded p-4 bg-gray-50 shadow">
          <h3 className="font-semibold">NewSmartContract.sol</h3>
          <p className="text-sm text-gray-600">Scanned: 06-03-2025</p>
          <p className="text-sm text-gray-600">Duration: 4.2s</p>
          <ul className="text-sm mt-2 list-disc list-inside">
            <li><span className="text-red-500 font-bold">High:</span> Reentrancy</li>
            <li><span className="text-yellow-500 font-bold">Medium:</span> Integer Overflow</li>
            <li><span className="text-green-600 font-bold">Low:</span> Unchecked Call Return</li>
          </ul>
          <div className="flex gap-2 mt-3 text-sm">
            <button className="bg-blue-600 text-white px-2 py-1 rounded hover:bg-blue-700">Re-scan</button>
            <button className="bg-gray-200 px-2 py-1 rounded hover:bg-gray-300">Report</button>
            <button className="bg-gray-200 px-2 py-1 rounded hover:bg-gray-300">Source</button>
          </div>
        </div>
      </div>
    </div>
  );
}
