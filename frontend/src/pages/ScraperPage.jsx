import { useState, useEffect } from 'react';
import ScraperHealth from '../components/ScraperHealth';
import HealingTimeline from '../components/HealingTimeline';
import RunHistory from '../components/RunHistory';
import DemoBadge from '../components/DemoBadge';
import { demoScraperStatus, demoHealingEvents, demoRuns } from '../data/demoData';

export default function ScraperPage() {
  const [status, setStatus] = useState(null);
  const [events, setEvents] = useState([]);
  const [runs, setRuns] = useState([]);

  useEffect(() => {
    // In a real app, fetch from API. Using demo data here.
    setStatus(demoScraperStatus);
    setEvents(demoHealingEvents);
    setRuns(demoRuns);
  }, []);

  if (!status) return null;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12 pb-20">
      <DemoBadge />
      
      <div>
        <h1 className="text-3xl font-bold mb-2">Scraper System Health</h1>
        <p className="text-slate-400">Real-time monitoring of data collectors and automatic healing events.</p>
      </div>

      <ScraperHealth {...status} />

      <div>
        <h2 className="text-2xl font-semibold mb-6">Self-Healing Engine</h2>
        <p className="text-slate-400 mb-4 max-w-3xl">
          When website structures change, our AI instantly analyzes the DOM diff, updates the extraction logic, and resumes the run using the exact same Collector ID. Zero manual intervention required.
        </p>
        <div className="grid lg:grid-cols-2 gap-8">
          <HealingTimeline events={events} />
          
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">
            <h3 className="text-lg font-medium mb-4">Schema Adaptation</h3>
            <div className="space-y-4 font-mono text-xs">
              <div className="p-3 rounded bg-red-950/30 border border-red-900/50">
                <div className="text-red-400 mb-1">- document.querySelector('.price-main')</div>
                <div className="text-slate-500">// Selector failed (Node is null)</div>
              </div>
              <div className="flex justify-center">
                <div className="px-3 py-1 rounded-full bg-slate-800 text-slate-400 text-[10px]">AI DOM Analysis</div>
              </div>
              <div className="p-3 rounded bg-emerald-950/30 border border-emerald-900/50">
                <div className="text-emerald-400 mb-1">+ document.querySelector('[data-testid="product-price"]')</div>
                <div className="text-slate-500">// Validated pattern match 99.8%</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div>
        <h2 className="text-2xl font-semibold mb-6">Execution Log</h2>
        <RunHistory runs={runs} />
      </div>
    </div>
  );
}
