import { Activity, Database, CheckCircle2, AlertTriangle, ArrowRight } from 'lucide-react';

export default function ScraperHealth({ status, collectorId, lastRun, records }) {
  const isHealthy = status === 'healthy';
  
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 relative overflow-hidden">
      <div className="absolute top-0 right-0 p-8 opacity-5">
        <Activity className="w-48 h-48" />
      </div>
      
      <div className="relative z-10">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h2 className="text-lg font-semibold text-slate-300 mb-1">Scraper Status</h2>
            <div className="flex items-center space-x-2">
              <span className={`w-3 h-3 rounded-full ${isHealthy ? 'bg-emerald-500 animate-pulse' : 'bg-amber-500 animate-pulse'}`} />
              <span className={`font-bold tracking-wider ${isHealthy ? 'text-emerald-400' : 'text-amber-400'}`}>
                {isHealthy ? 'SYSTEM HEALTHY' : 'DEGRADED'}
              </span>
            </div>
          </div>
          <div className="text-right">
            <div className="text-sm text-slate-500 mb-1">Collector ID</div>
            <code className="bg-slate-950 px-3 py-1 rounded-lg text-blue-400 font-mono text-sm border border-slate-800">
              {collectorId}
            </code>
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
            <div className="text-sm text-slate-500 mb-1">Last Run</div>
            <div className="font-medium text-slate-200">{new Date(lastRun).toLocaleTimeString()}</div>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
            <div className="text-sm text-slate-500 mb-1">Records Found</div>
            <div className="font-medium text-emerald-400 flex items-center">
              <Database className="w-4 h-4 mr-1.5" />
              {records}
            </div>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
            <div className="text-sm text-slate-500 mb-1">Success Rate</div>
            <div className="font-medium text-emerald-400">99.8%</div>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
            <div className="text-sm text-slate-500 mb-1">Auto-Heals</div>
            <div className="font-medium text-blue-400">12 (Last 30d)</div>
          </div>
        </div>

        <div>
          <div className="text-sm font-medium text-slate-400 mb-4">Live Pipeline</div>
          <div className="flex flex-col sm:flex-row items-center justify-between gap-2 text-xs sm:text-sm">
            <div className="flex items-center space-x-2 text-emerald-400 bg-emerald-400/10 px-3 py-2 rounded-lg border border-emerald-400/20 w-full sm:w-auto justify-center">
              <CheckCircle2 className="w-4 h-4" /> <span>COLLECT</span>
            </div>
            <ArrowRight className="w-4 h-4 text-slate-600 hidden sm:block" />
            <div className="flex items-center space-x-2 text-emerald-400 bg-emerald-400/10 px-3 py-2 rounded-lg border border-emerald-400/20 w-full sm:w-auto justify-center">
              <CheckCircle2 className="w-4 h-4" /> <span>EXTRACT</span>
            </div>
            <ArrowRight className="w-4 h-4 text-slate-600 hidden sm:block" />
            <div className="flex items-center space-x-2 text-emerald-400 bg-emerald-400/10 px-3 py-2 rounded-lg border border-emerald-400/20 w-full sm:w-auto justify-center">
              <CheckCircle2 className="w-4 h-4" /> <span>VALIDATE</span>
            </div>
            <ArrowRight className="w-4 h-4 text-slate-600 hidden sm:block" />
            <div className="flex items-center space-x-2 text-blue-400 bg-blue-400/10 px-3 py-2 rounded-lg border border-blue-400/20 w-full sm:w-auto justify-center animate-pulse">
              <Activity className="w-4 h-4" /> <span>ANALYZE</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
