import { Terminal } from 'lucide-react';

export default function HealingTimeline({ events }) {
  if (!events || events.length === 0) return null;

  return (
    <div className="bg-slate-950 rounded-xl border border-slate-800 overflow-hidden font-mono text-sm shadow-2xl">
      <div className="bg-slate-900 border-b border-slate-800 p-3 flex items-center space-x-2">
        <div className="flex space-x-1.5">
          <div className="w-3 h-3 rounded-full bg-red-500/80"></div>
          <div className="w-3 h-3 rounded-full bg-amber-500/80"></div>
          <div className="w-3 h-3 rounded-full bg-emerald-500/80"></div>
        </div>
        <div className="flex-1 text-center text-xs text-slate-500 flex items-center justify-center">
          <Terminal className="w-3 h-3 mr-1.5" /> scraper-heal-log.sh
        </div>
      </div>
      <div className="p-4 space-y-1 overflow-x-auto">
        {events.map((event, index) => {
          const lines = event.command.split('\n');
          return (
            <div key={index} className="mb-4 last:mb-0">
              <div className="text-slate-600 text-xs mb-2">[{new Date(event.timestamp).toLocaleTimeString()}] Event: {event.type}</div>
              {lines.map((line, i) => {
                let colorClass = 'text-slate-300';
                if (line.startsWith('> Error')) colorClass = 'text-red-400';
                if (line.startsWith('> Success')) colorClass = 'text-emerald-400';
                if (line.startsWith('> Analyzing') || line.startsWith('> Extractor')) colorClass = 'text-amber-300';
                if (line.includes('c_abc123')) {
                  const parts = line.split('c_abc123');
                  return (
                    <div key={i} className="flex">
                      <span className="text-blue-400 mr-2">{line.startsWith('$') ? '$' : '>'}</span>
                      <span className={colorClass}>
                        {parts[0].replace(/^[>$]\s*/, '')}
                        <span className="bg-amber-500/20 text-amber-300 px-1 rounded mx-0.5 animate-pulse">c_abc123</span>
                        {parts[1]}
                      </span>
                    </div>
                  );
                }
                return (
                  <div key={i} className="flex">
                    <span className="text-blue-400 mr-2">{line.startsWith('$') ? '$' : '>'}</span>
                    <span className={colorClass}>{line.replace(/^[>$]\s*/, '')}</span>
                  </div>
                );
              })}
            </div>
          );
        })}
      </div>
    </div>
  );
}
