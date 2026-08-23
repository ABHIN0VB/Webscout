import { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { Loader2 } from 'lucide-react';
import PipelineStatus from '../components/PipelineStatus';
import { startResearch } from '../services/api';

const PIPELINE_STEPS = [
  { name: 'Understanding query', status: 'pending' },
  { name: 'Collecting web data', status: 'pending' },
  { name: 'Normalizing products', status: 'pending' },
  { name: 'Comparing results', status: 'pending' },
  { name: 'Generating recommendations', status: 'pending' },
];

export default function ResearchPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const query = location.state?.query || '';
  const [steps, setSteps] = useState(PIPELINE_STEPS);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!query) {
      navigate('/');
      return;
    }

    let cancelled = false;

    const runPipeline = async () => {
      // Animate pipeline steps
      const stepDelays = [800, 1500, 1200, 1000, 1000];

      for (let i = 0; i < steps.length; i++) {
        if (cancelled) return;
        
        setSteps(prev => prev.map((s, idx) => ({
          ...s,
          status: idx < i ? 'completed' : idx === i ? 'running' : 'pending'
        })));

        await new Promise(r => setTimeout(r, stepDelays[i]));
      }

      // All steps completed
      setSteps(prev => prev.map(s => ({ ...s, status: 'completed' })));

      // Try real API call
      try {
        const res = await startResearch(query);
        if (!cancelled) {
          const researchId = res.data?.id;
          setTimeout(() => {
            navigate(`/results/${researchId}`, { state: { query } });
          }, 600);
        }
      } catch (err) {
        console.warn('API unavailable, navigating to demo results');
        if (!cancelled) {
          setTimeout(() => {
            navigate('/results/demo', { state: { query, isDemo: true } });
          }, 600);
        }
      }
    };

    runPipeline();
    return () => { cancelled = true; };
  }, [query]);

  return (
    <div className="min-h-[calc(100vh-64px)] flex flex-col items-center justify-center px-4">
      <div className="max-w-xl w-full text-center">
        <div className="mb-8">
          <div className="inline-flex items-center gap-2 bg-blue-500/10 border border-blue-500/20 text-blue-400 text-sm px-4 py-2 rounded-full mb-6">
            <Loader2 className="w-4 h-4 animate-spin" />
            Researching...
          </div>
          <h1 className="text-2xl font-bold text-white mb-3">
            {query}
          </h1>
          <p className="text-slate-400 text-sm">
            WebScout is analyzing your requirements and collecting data
          </p>
        </div>

        <PipelineStatus steps={steps} />

        {error && (
          <div className="mt-6 p-4 bg-red-900/20 border border-red-800 rounded-xl text-red-400 text-sm">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}
