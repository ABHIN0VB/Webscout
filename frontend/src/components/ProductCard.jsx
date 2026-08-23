import { Laptop, Star, Tag, CheckCircle2, Sparkles } from 'lucide-react';

export default function ProductCard({ product, rank, onClick, onCompare, isCompared }) {
  const getScoreColor = (score) => {
    if (score >= 90) return 'text-emerald-400 bg-emerald-400/10 border-emerald-400/20';
    if (score >= 70) return 'text-amber-400 bg-amber-400/10 border-amber-400/20';
    return 'text-red-400 bg-red-400/10 border-red-400/20';
  };

  const formatPrice = (price) => {
    if (!price && price !== 0) return 'N/A';
    if (typeof price === 'string' && (price.includes('₹') || price.includes('Rs'))) return price;
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(price);
  };

  // Extract up to 4 key spec items dynamically
  const specs = product.specifications || {};
  const specEntries = Object.entries(specs)
    .filter(([_, val]) => val && val !== 'null' && val !== 'undefined')
    .slice(0, 4);

  return (
    <div className="bg-slate-800/90 backdrop-blur-md rounded-2xl overflow-hidden border border-slate-700/80 hover:border-blue-500/50 hover:bg-slate-800 transition-all group flex flex-col h-full relative shadow-lg">
      {rank && (
        <div className="absolute top-4 left-4 z-10 w-8 h-8 rounded-full bg-slate-900/90 border border-slate-700 flex items-center justify-center font-bold text-sm shadow-lg text-blue-400">
          #{rank}
        </div>
      )}

      <div className="h-44 bg-gradient-to-br from-slate-900 via-slate-850 to-slate-900 flex items-center justify-center border-b border-slate-700/80 relative p-4">
        {product.image_url ? (
          <img src={product.image_url} alt={product.name} className="h-full max-w-full object-contain p-2 group-hover:scale-105 transition-transform duration-500" />
        ) : (
          <div className="w-16 h-16 rounded-2xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400 group-hover:scale-110 transition-transform duration-500">
            <Sparkles className="w-8 h-8" />
          </div>
        )}
        {product.matchScore && (
          <div className={`absolute bottom-3 right-3 px-3 py-1 rounded-full text-xs font-semibold border backdrop-blur-md ${getScoreColor(product.matchScore)}`}>
            {product.matchScore}% Match
          </div>
        )}
      </div>

      <div className="p-5 flex-1 flex flex-col">
        {product.brand && (
          <span className="text-xs font-medium text-blue-400 uppercase tracking-wider mb-1">{product.brand}</span>
        )}
        <h3 className="font-semibold text-base line-clamp-2 mb-3 leading-snug text-white group-hover:text-blue-300 transition-colors flex-1">{product.name}</h3>

        <div className="flex items-center justify-between mb-4">
          <span className="text-xl font-bold text-emerald-400">{formatPrice(product.price)}</span>
          {product.rating && (
            <div className="flex items-center space-x-1 text-xs text-amber-300 bg-amber-400/10 border border-amber-400/20 px-2 py-1 rounded-lg">
              <Star className="w-3.5 h-3.5 fill-current" />
              <span className="font-semibold">{product.rating}</span>
            </div>
          )}
        </div>

        {/* Dynamic Spec Pills */}
        {specEntries.length > 0 && (
          <div className="grid grid-cols-2 gap-2 mb-5">
            {specEntries.map(([key, val]) => (
              <div key={key} className="flex flex-col text-xs text-slate-300 bg-slate-900/60 p-2 rounded-lg border border-slate-700/50">
                <span className="text-[10px] text-slate-500 uppercase font-medium truncate">{key}</span>
                <span className="truncate font-medium text-slate-200">{val}</span>
              </div>
            ))}
          </div>
        )}

        <div className="flex gap-2 mt-auto">
          <button
            onClick={() => onClick(product)}
            className="flex-1 bg-blue-600 hover:bg-blue-500 text-white py-2 rounded-xl text-xs font-semibold transition-all shadow-md shadow-blue-600/20"
          >
            View Details
          </button>
          <label className={`flex items-center justify-center px-3 py-2 rounded-xl text-xs font-medium cursor-pointer transition-all border ${
            isCompared
              ? 'bg-indigo-600/20 border-indigo-500 text-indigo-300 font-semibold'
              : 'bg-slate-900/80 border-slate-700 text-slate-400 hover:text-white hover:border-slate-600'
          }`}>
            <input
              type="checkbox"
              className="hidden"
              checked={isCompared}
              onChange={() => onCompare(product)}
            />
            {isCompared ? '✓ Added' : '+ Compare'}
          </label>
        </div>
      </div>
    </div>
  );
}
