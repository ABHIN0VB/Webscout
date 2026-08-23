export default function ScoreBreakdown({ breakdown }) {
  const getBarColor = (score) => {
    if (score >= 90) return 'bg-emerald-500';
    if (score >= 70) return 'bg-amber-500';
    return 'bg-red-500';
  };

  const getLabelColor = (score) => {
    if (score >= 90) return 'text-emerald-400';
    if (score >= 70) return 'text-amber-400';
    return 'text-red-400';
  };

  return (
    <div className="space-y-4">
      {Object.entries(breakdown).map(([category, score]) => (
        <div key={category} className="space-y-2">
          <div className="flex justify-between items-center text-sm">
            <span className="font-medium text-slate-300 capitalize">{category.replace(/([A-Z])/g, ' $1').trim()}</span>
            <span className={`font-bold ${getLabelColor(score)}`}>{score}/100</span>
          </div>
          <div className="h-2 w-full bg-slate-800 rounded-full overflow-hidden">
            <div 
              className={`h-full rounded-full ${getBarColor(score)} transition-all duration-1000 ease-out`} 
              style={{ width: `${score}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}
