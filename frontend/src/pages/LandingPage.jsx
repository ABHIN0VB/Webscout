import { useNavigate } from 'react-router-dom';
import { Search, Zap, Shield, Globe } from 'lucide-react';
import SearchBar from '../components/SearchBar';

export default function LandingPage() {
  const navigate = useNavigate();

  const handleSearch = (query) => {
    navigate('/research', { state: { query } });
  };

  const prompts = [
    "Best laptop under ₹80k for programming",
    "Best monitor under ₹30k for development",
    "Best mechanical keyboard for coding"
  ];

  return (
    <div className="min-h-[calc(100vh-64px)] flex flex-col relative overflow-hidden">
      <div className="absolute top-0 inset-x-0 h-full bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-blue-900/20 via-slate-950 to-slate-950 -z-10" />
      
      <div className="flex-1 flex flex-col items-center justify-center px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center max-w-4xl mx-auto mb-12">
          <h1 className="text-5xl sm:text-7xl font-extrabold tracking-tight mb-6">
            <span className="bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400 bg-clip-text text-transparent">
              WEBSCOUT
            </span>
          </h1>
          <p className="text-xl sm:text-2xl text-slate-300 mb-4 font-medium">
            Research the web. Even when the web changes.
          </p>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            An AI-powered research agent that automatically collects, analyzes, and compares product data. Powered by self-healing scrapers.
          </p>
        </div>

        <div className="w-full max-w-3xl mx-auto mb-12">
          <SearchBar onSubmit={handleSearch} />
          
          <div className="mt-6 flex flex-wrap items-center justify-center gap-3">
            <span className="text-sm text-slate-500 mr-2">Try:</span>
            {prompts.map((prompt, i) => (
              <button
                key={i}
                onClick={() => handleSearch(prompt)}
                className="text-sm text-slate-300 bg-slate-900/50 hover:bg-slate-800 border border-slate-700/50 hover:border-blue-500/50 px-4 py-2 rounded-full transition-all"
              >
                {prompt}
              </button>
            ))}
          </div>
        </div>

        <div className="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto mt-12">
          <div className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 p-6 rounded-2xl">
            <div className="w-12 h-12 bg-blue-500/10 text-blue-400 rounded-xl flex items-center justify-center mb-4 border border-blue-500/20">
              <Zap className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-semibold text-white mb-2">AI-Powered Analysis</h3>
            <p className="text-slate-400 text-sm">Automatically compares specs, reads reviews, and generates smart recommendations.</p>
          </div>
          <div className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 p-6 rounded-2xl">
            <div className="w-12 h-12 bg-emerald-500/10 text-emerald-400 rounded-xl flex items-center justify-center mb-4 border border-emerald-500/20">
              <Shield className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-semibold text-white mb-2">Self-Healing Data</h3>
            <p className="text-slate-400 text-sm">When websites change, our scrapers automatically fix themselves to keep data flowing.</p>
          </div>
          <div className="bg-slate-900/50 backdrop-blur-sm border border-slate-800 p-6 rounded-2xl">
            <div className="w-12 h-12 bg-purple-500/10 text-purple-400 rounded-xl flex items-center justify-center mb-4 border border-purple-500/20">
              <Globe className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-semibold text-white mb-2">Real-Time Intelligence</h3>
            <p className="text-slate-400 text-sm">Live data collection from multiple sources ensures you always get the latest prices.</p>
          </div>
        </div>
      </div>

      <div className="py-6 text-center border-t border-slate-800/50 mt-auto bg-slate-950">
        <span className="inline-flex items-center space-x-2 text-sm text-slate-500">
          <span>Powered by</span>
          <span className="font-semibold text-slate-300">Bright Data Scraper Studio</span>
        </span>
      </div>
    </div>
  );
}
