import { useState } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip as RechartsTooltip, ResponsiveContainer,
  AreaChart, Area, PieChart, Pie, Cell, Legend
} from 'recharts';
import { Activity, CheckCircle2, XCircle, Wrench, Database, Clock } from 'lucide-react';
import DemoBadge from '../components/DemoBadge';
import { demoAnalytics } from '../data/demoData';

const COLORS = ['#10b981', '#ef4444', '#3b82f6'];

export default function AnalyticsPage() {
  const [stats] = useState(demoAnalytics);

  const barData = stats.run_history || [
    { date: 'Aug 17', success: 12, failed: 1 },
    { date: 'Aug 18', success: 14, failed: 0 },
    { date: 'Aug 19', success: 13, failed: 2 },
    { date: 'Aug 20', success: 15, failed: 1 },
    { date: 'Aug 21', success: 14, failed: 2 },
    { date: 'Aug 22', success: 12, failed: 1 },
    { date: 'Aug 23', success: 8, failed: 1 },
  ];

  const healingData = stats.healing_history || [];

  const pieData = [
    { name: 'Successful', value: stats.successful || stats.successful_runs || 88 },
    { name: 'Failed', value: stats.failed || stats.failed_runs || 8 },
    { name: 'Healed', value: stats.healed || stats.healed_runs || 8 }
  ];

  const statCards = [
    { label: 'Total Runs', value: stats.totalRuns || stats.total_runs, icon: Activity, color: 'text-white' },
    { label: 'Successful', value: stats.successful || stats.successful_runs, icon: CheckCircle2, color: 'text-emerald-400' },
    { label: 'Failed', value: stats.failed || stats.failed_runs, icon: XCircle, color: 'text-red-400' },
    { label: 'Auto-Healed', value: stats.healed || stats.healed_runs, icon: Wrench, color: 'text-blue-400' },
    { label: 'Total Records', value: (stats.records || stats.total_records || 0).toLocaleString(), icon: Database, color: 'text-purple-400' },
    { label: 'Avg Recovery', value: stats.recoveryTime || `${stats.avg_recovery_time_seconds}s`, icon: Clock, color: 'text-amber-400' },
  ];

  const reliabilityPercent = stats.successful || stats.successful_runs
    ? Math.round(((stats.successful || stats.successful_runs) / (stats.totalRuns || stats.total_runs)) * 100)
    : 92;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 pb-20">
      <DemoBadge />

      <div>
        <h1 className="text-3xl font-bold mb-2">Analytics</h1>
        <p className="text-slate-400">Scraper performance, data collection metrics, and self-healing statistics.</p>
      </div>

      {/* Stat Cards */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        {statCards.map((stat, i) => {
          const Icon = stat.icon;
          return (
            <div key={i} className="bg-slate-900 border border-slate-800 p-4 rounded-xl">
              <div className="flex items-center gap-2 mb-2">
                <Icon className={`w-4 h-4 ${stat.color}`} />
                <span className="text-xs text-slate-500">{stat.label}</span>
              </div>
              <div className={`text-2xl font-bold ${stat.color}`}>{stat.value}</div>
            </div>
          );
        })}
      </div>

      {/* Reliability Banner */}
      <div className="bg-gradient-to-r from-emerald-900/30 to-blue-900/30 border border-emerald-800/50 rounded-xl p-6">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold text-white mb-1">Scraper Reliability</h3>
            <p className="text-sm text-slate-400">
              {reliabilityPercent}% of all runs completed successfully. Failed runs were auto-healed by Bright Data Scraper Studio.
            </p>
          </div>
          <div className="text-4xl font-bold text-emerald-400">{reliabilityPercent}%</div>
        </div>
      </div>

      {/* Charts Row */}
      <div className="grid lg:grid-cols-2 gap-8">
        {/* Run Status History */}
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl">
          <h3 className="text-lg font-semibold mb-6">Runs Over Time</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={barData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                <XAxis dataKey="date" stroke="#94a3b8" fontSize={12} tickLine={false} axisLine={false} />
                <YAxis stroke="#94a3b8" fontSize={12} tickLine={false} axisLine={false} />
                <RechartsTooltip
                  contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px' }}
                  itemStyle={{ color: '#e2e8f0' }}
                />
                <Bar dataKey="success" stackId="a" fill="#10b981" name="Successful" radius={[0, 0, 4, 4]} />
                <Bar dataKey="failed" stackId="a" fill="#ef4444" name="Failed" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Status Distribution */}
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl">
          <h3 className="text-lg font-semibold mb-6">Run Status Distribution</h3>
          <div className="h-64 flex items-center justify-center">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={90}
                  paddingAngle={4}
                  dataKey="value"
                >
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Legend
                  formatter={(value) => <span className="text-slate-300 text-sm">{value}</span>}
                />
                <RechartsTooltip
                  contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px' }}
                  itemStyle={{ color: '#e2e8f0' }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Healing Events Over Time */}
      {healingData.length > 0 && (
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl">
          <h3 className="text-lg font-semibold mb-6">Self-Healing Recovery</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={healingData}>
                <defs>
                  <linearGradient id="colorHealed" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3} />
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                <XAxis dataKey="date" stroke="#94a3b8" fontSize={12} tickLine={false} axisLine={false} />
                <YAxis stroke="#94a3b8" fontSize={12} tickLine={false} axisLine={false} />
                <RechartsTooltip
                  contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px' }}
                  itemStyle={{ color: '#e2e8f0' }}
                />
                <Area type="monotone" dataKey="records_recovered" stroke="#3b82f6" fillOpacity={1} fill="url(#colorHealed)" name="Records Recovered" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
      )}
    </div>
  );
}
