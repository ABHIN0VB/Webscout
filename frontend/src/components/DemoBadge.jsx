import { AlertTriangle } from 'lucide-react';

export default function DemoBadge() {
  return (
    <div className="fixed bottom-4 right-4 z-50 flex items-center space-x-2 bg-amber-500/10 border border-amber-500/30 backdrop-blur-md text-amber-500 px-4 py-2 rounded-full shadow-lg pointer-events-none">
      <AlertTriangle className="w-4 h-4" />
      <span className="text-xs font-bold tracking-widest">DEMO DATA</span>
    </div>
  );
}
