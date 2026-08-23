import { CheckCircle2, XCircle, Clock } from 'lucide-react';

export default function RunHistory({ runs }) {
  if (!runs || runs.length === 0) return null;

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden">
      <div className="px-6 py-4 border-b border-slate-800 bg-slate-900/50">
        <h3 className="font-semibold text-slate-300">Recent Scraper Runs</h3>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead>
            <tr className="bg-slate-950 text-slate-500 text-xs uppercase tracking-wider">
              <th className="px-6 py-3 font-medium">Time</th>
              <th className="px-6 py-3 font-medium">Status</th>
              <th className="px-6 py-3 font-medium">Records</th>
              <th className="px-6 py-3 font-medium">Duration</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/50">
            {runs.map((run) => (
              <tr key={run.id} className="hover:bg-slate-800/50 transition-colors">
                <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-300">
                  {new Date(run.time).toLocaleString()}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className={`inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-full text-xs font-medium border ${
                    run.status === 'success' 
                      ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' 
                      : 'bg-red-500/10 text-red-400 border-red-500/20'
                  }`}>
                    {run.status === 'success' ? <CheckCircle2 className="w-3.5 h-3.5" /> : <XCircle className="w-3.5 h-3.5" />}
                    <span className="capitalize">{run.status}</span>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-300 font-mono">
                  {run.records}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-500 flex items-center">
                  <Clock className="w-4 h-4 mr-1.5" /> {run.duration}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
