import { X } from 'lucide-react';

export default function ComparisonTable({ products, onRemove }) {
  if (!products || products.length === 0) return null;

  const formatPrice = (price) => {
    if (!price && price !== 0) return 'N/A';
    if (typeof price === 'string' && (price.includes('₹') || price.includes('Rs'))) return price;
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(price);
  };

  // Collect all unique specification keys across all products
  const allSpecKeys = new Set();
  products.forEach(p => {
    const specs = p.specifications || {};
    Object.keys(specs).forEach(k => allSpecKeys.add(k));
  });

  const specKeyList = Array.from(allSpecKeys);

  return (
    <div className="w-full overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900 shadow-xl">
      <table className="w-full text-left border-collapse min-w-[800px]">
        <thead>
          <tr>
            <th className="p-4 bg-slate-900 border-b border-slate-800 border-r w-48 sticky left-0 z-10">
              <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Features</span>
            </th>
            {products.map((p) => (
              <th key={p.id} className="p-4 bg-slate-900 border-b border-slate-800 min-w-[250px] relative">
                {onRemove && (
                  <button 
                    onClick={() => onRemove(p.id)}
                    className="absolute top-3 right-3 p-1.5 rounded-lg bg-slate-800 text-slate-400 hover:text-white hover:bg-slate-700 transition-colors"
                  >
                    <X className="w-4 h-4" />
                  </button>
                )}
                <div className="pr-6">
                  {p.brand && <span className="text-xs text-blue-400 uppercase font-medium">{p.brand}</span>}
                  <h3 className="font-semibold text-base line-clamp-2 mb-1 text-white">{p.name}</h3>
                  <p className="text-xl font-bold text-emerald-400">{formatPrice(p.price)}</p>
                </div>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {/* Match Score */}
          <tr className="bg-slate-900/50">
            <td className="p-4 border-b border-slate-800 border-r font-medium text-slate-400 sticky left-0 z-10 bg-inherit">
              Match Score
            </td>
            {products.map((p) => (
              <td key={`${p.id}-score`} className="p-4 border-b border-slate-800">
                <span className={`text-base font-bold ${
                  (p.matchScore || 0) >= 90 ? 'text-emerald-400' : (p.matchScore || 0) >= 70 ? 'text-amber-400' : 'text-red-400'
                }`}>
                  {p.matchScore || 85}% Match
                </span>
              </td>
            ))}
          </tr>

          {/* Rating */}
          <tr className="bg-slate-900">
            <td className="p-4 border-b border-slate-800 border-r font-medium text-slate-400 sticky left-0 z-10 bg-inherit">
              Rating
            </td>
            {products.map((p) => (
              <td key={`${p.id}-rating`} className="p-4 border-b border-slate-800 text-amber-400 font-semibold">
                ★ {p.rating || 4.5} <span className="text-xs text-slate-500 font-normal">/ 5.0</span>
              </td>
            ))}
          </tr>

          {/* Dynamic Specifications */}
          {specKeyList.map((key, i) => (
            <tr key={key} className={i % 2 === 0 ? 'bg-slate-900/50' : 'bg-slate-900'}>
              <td className="p-4 border-b border-slate-800 border-r font-medium text-slate-400 sticky left-0 z-10 bg-inherit capitalize">
                {key.replace(/_/g, ' ')}
              </td>
              {products.map((p) => {
                const val = p.specifications?.[key] || p[key];
                return (
                  <td key={`${p.id}-${key}`} className="p-4 border-b border-slate-800 text-slate-300 text-sm">
                    {val ? String(val) : <span className="text-slate-600 italic">-</span>}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
