export default function AboutSection() {
  return (
    <section id="about" className="w-full bg-white text-gray-800 px-6 py-12">
      <div className="max-w-4xl mx-auto space-y-10">
        {/* Giới thiệu dự án */}
        <div>
          <h2 className="text-3xl font-bold text-center text-[#003366] mb-4">
            About Our Project
          </h2>
          <p className="text-lg text-center">
            This project was initiated as part of our Capstone course at RMIT University,
            with the goal of addressing the real-world issue of smart contract vulnerabilities.
            We’ve developed a complete web platform that allows users to easily upload their
            Solidity smart contracts and receive AI-powered vulnerability analysis — helping developers
            and auditors ensure security before deployment.
          </p>
        </div>

        {/* Giới thiệu nhóm */}
        <div>
          <h3 className="text-2xl font-semibold text-[#003366] mb-4">Our Team</h3>
          <ul className="grid md:grid-cols-2 gap-4">
            <li className="bg-blue-50 p-4 rounded shadow">
              <p className="font-bold">Du Tuan Vu</p>
              <p> Frontend Developer</p>
              <p className="text-sm text-gray-600">Responsible for UI design, user flow, and React components.</p>
            </li>
            <li className="bg-blue-50 p-4 rounded shadow">
              <p className="font-bold">Pham Dang Khoa</p>
              <p>Machine Learning Engineer</p>
              <p className="text-sm text-gray-600">Developed the AI model for vulnerability detection.</p>
            </li>
            <li className="bg-blue-50 p-4 rounded shadow">
              <p className="font-bold">Hoang Duc Phuong, Dinh Gia Bao </p>
              <p>Backend Developer</p>
              <p className="text-sm text-gray-600">Built API services and handled backend integration.</p>
            </li>
            <li className="bg-blue-50 p-4 rounded shadow">
              <p className="font-bold">Nguyen Minh Phu</p>
              <p>Dataset Specialist & Project Leader</p>
              <p className="text-sm text-gray-600">Labeled vulnerability data and created project documentation.</p>
            </li>
          </ul>
        </div>

        {/* Timeline */}
        <div>
          <h3 className="text-2xl font-semibold text-[#003366] mb-2">Project Timeline</h3>
          <ul className="list-disc pl-5 space-y-1 text-gray-700">
            <li><strong>Start Date:</strong> Feb 2025</li>
            <li><strong>Expected Completion:</strong> September 2025</li>
            <li>Phase 1: Dataset preparation  — ✅ Completed</li>
            <li>Phase 2: UI development, backend integration & model training — 🔄 In progress</li>
          </ul>
        </div>
      </div>
    </section>
  );
}
