import { CheckCircle2, Circle, Loader2, XCircle } from 'lucide-react';

export default function PipelineStatus({ steps }) {
  return (
    <div className="w-full max-w-xl mx-auto">
      <div className="relative">
        {steps.map((step, index) => {
          const isLast = index === steps.length - 1;
          
          return (
            <div key={step.name} className="flex items-start mb-8 last:mb-0 relative">
              {!isLast && (
                <div className={`absolute left-3 top-8 bottom-[-24px] w-0.5 ${
                  step.status === 'completed' ? 'bg-emerald-500' : 'bg-slate-800'
                }`} />
              )}
              
              <div className="relative z-10 flex items-center justify-center w-6 h-6 mt-0.5 mr-4 rounded-full bg-slate-950">
                {step.status === 'completed' && <CheckCircle2 className="w-6 h-6 text-emerald-500" />}
                {step.status === 'running' && <Loader2 className="w-6 h-6 text-blue-500 animate-spin" />}
                {step.status === 'pending' && <Circle className="w-6 h-6 text-slate-600" />}
                {step.status === 'failed' && <XCircle className="w-6 h-6 text-red-500" />}
              </div>
              
              <div>
                <p className={`font-medium ${
                  step.status === 'completed' ? 'text-emerald-400' :
                  step.status === 'running' ? 'text-blue-400' :
                  step.status === 'failed' ? 'text-red-400' : 'text-slate-400'
                }`}>
                  {step.name}
                </p>
                {step.description && (
                  <p className="text-sm text-slate-500 mt-1">{step.description}</p>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
