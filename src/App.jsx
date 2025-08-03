import { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import UploadForm from './components/UploadForm';
import AboutSection from './components/AboutSection';
import HistorySidebar from './components/HistorySidebar';
import backgroundImage from './assets/background.png';

export default function App() {
  const [showHistory, setShowHistory] = useState(false);

  return (
    <div className="flex flex-col w-full relative">
      {/* Sticky Header */}
      <Header onShowHistory={() => setShowHistory(true)} />

      {/* History Sidebar Slide-in */}
      {showHistory && (
        <HistorySidebar isOpen={showHistory} onClose={() => setShowHistory(false)} />
        )}

      {/* Main Upload Area with background image */}
      <main
        className="flex flex-col w-full px-4 pt-24 min-h-screen bg-fixed bg-cover bg-center"
        style={{
          backgroundImage: `linear-gradient(to bottom right, rgba(0,51,102,0.9), rgba(0,38,77,0.9)), url(${backgroundImage})`,
        }}
      >
        <section
          id="upload"
          className="w-full max-w-md mx-auto mb-16 scroll-mt-24"
        >
          <div className="bg-white/10 backdrop-blur-lg rounded-xl p-8 shadow-lg">
            <UploadForm />
          </div>
        </section>
      </main>

      {/* About Section */}
      <section
        id="about"
        className="w-full min-h-screen bg-white px-8 py-20 scroll-mt-20"
      >
        <AboutSection />
      </section>

      {/* Footer */}
      <Footer />
    </div>
  );
}
