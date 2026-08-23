import { Trophy, Check, AlertTriangle, ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function RecommendationCard({ product, score, reasoning, tradeoffs }) {
  const formatPrice = (price) => {
    if (!price && price !== 0) return 'N/A';
    if (typeof price === 'string' && (price.includes('₹') || price.includes('Rs'))) return price;
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(price);
  };

  return (
    <div className="relative rounded-2xl overflow-hidden bg-slate-900 border border-blue-500/30 p-[1px]">
      <div className="absolute inset-0 bg-gradient-to-br from-blue-600/20 to-indigo-600/20 z-0 pointer-events-none" />
      
      <div className="relative z-10 bg-slate-900 rounded-[15px] p-6 sm:p-8 flex flex-col md:flex-row gap-8 items-center">
        <div className="flex-1 space-y-6">
          <div className="inline-flex items-center space-x-2 bg-gradient-to-r from-blue-500/10 to-indigo-500/10 border border-blue-500/20 rounded-full px-4 py-1.5">
            <Trophy className="w-4 h-4 text-blue-400" />
            <span className="text-sm font-semibold text-blue-300 uppercase tracking-wider">Your Best Match</span>
          </div>
          
          <div>
            <h2 className="text-2xl sm:text-3xl font-bold mb-2 text-white">{product.name}</h2>
            <div className="text-3xl font-bold text-emerald-400">{formatPrice(product.price)}</div>
          </div>
          
          <div className="grid sm:grid-cols-2 gap-6">
            <div>
              <h4 className="text-sm font-medium text-slate-400 mb-3 flex items-center">
                <Check className="w-4 h-4 mr-1.5 text-emerald-500" /> Why we recommend it
              </h4>
              <ul className="space-y-2">
                {reasoning?.map((item, i) => (
                  <li key={i} className="text-sm text-slate-300 flex items-start">
                    <span className="mr-2 text-emerald-500 mt-0.5">•</span>
                    {item}
                  </li>
                ))}
              </ul>
            </div>
            
            {tradeoffs && tradeoffs.length > 0 && (
              <div>
                <h4 className="text-sm font-medium text-slate-400 mb-3 flex items-center">
                  <AlertTriangle className="w-4 h-4 mr-1.5 text-amber-500" /> Trade-offs
                </h4>
                <ul className="space-y-2">
                  {tradeoffs.map((item, i) => (
                    <li key={i} className="text-sm text-slate-300 flex items-start">
                      <span className="mr-2 text-amber-500 mt-0.5">•</span>
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
          
          <Link 
            to={`/product/${product.id}`}
            state={{ product }}
            className="inline-flex items-center justify-center px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-medium transition-colors"
          >
            View Full Analysis <ArrowRight className="w-4 h-4 ml-2" />
          </Link>
        </div>
        
        <div className="shrink-0 relative">
          <svg className="w-32 h-32 transform -rotate-90">
            <circle cx="64" cy="64" r="60" stroke="currentColor" strokeWidth="8" fill="transparent" className="text-slate-800" />
            <circle 
              cx="64" cy="64" r="60" 
              stroke="currentColor" 
              strokeWidth="8" 
              fill="transparent" 
              strokeDasharray={377} 
              strokeDashoffset={377 - (377 * score) / 100}
              className="text-blue-500" 
            />
          </svg>
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-3xl font-bold">{score}</span>
            <span className="text-xs text-slate-400 uppercase tracking-widest mt-1">Score</span>
          </div>
        </div>
      </div>
    </div>
  );
}
