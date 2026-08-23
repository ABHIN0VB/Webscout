import { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { ArrowLeft, Trophy } from 'lucide-react';
import ComparisonTable from '../components/ComparisonTable';

export default function ComparePage() {
  const location = useLocation();
  const navigate = useNavigate();
  const [products, setProducts] = useState(location.state?.products || []);

  const handleRemove = (id) => {
    setProducts(products.filter(p => p.id !== id));
  };

  if (!products.length) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[50vh]">
        <p className="text-slate-400 mb-4">No products selected for comparison.</p>
        <button onClick={() => navigate(-1)} className="text-blue-400 hover:underline">Go Back</button>
      </div>
    );
  }

  const bestMatch = [...products].sort((a, b) => (b.matchScore || b.score || 0) - (a.matchScore || a.score || 0))[0];
  const winnerScore = bestMatch ? (bestMatch.matchScore || bestMatch.score || 85) : null;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <button 
        onClick={() => navigate(-1)}
        className="flex items-center text-slate-400 hover:text-white mb-6 transition-colors"
      >
        <ArrowLeft className="w-4 h-4 mr-2" /> Back
      </button>

      <h1 className="text-3xl font-bold mb-8">Compare Products</h1>

      {bestMatch && (
        <div className="bg-gradient-to-r from-blue-900/40 to-indigo-900/40 border border-blue-500/30 rounded-2xl p-6 mb-8 flex items-center justify-between">
          <div>
            <div className="flex items-center space-x-2 text-blue-400 font-semibold mb-1">
              <Trophy className="w-5 h-5" />
              <span>Overall Winner</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-bold text-white">{bestMatch.name}</h3>
          </div>
          <div className="text-right">
            <div className="text-sm text-slate-400">Match Score</div>
            <div className="text-3xl font-bold text-emerald-400">{winnerScore}%</div>
          </div>
        </div>
      )}

      <ComparisonTable products={products} onRemove={handleRemove} />
    </div>
  );
}
