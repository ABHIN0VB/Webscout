import { useState } from 'react';
import { Search } from 'lucide-react';

export default function SearchBar({ onSubmit, initialValue = '' }) {
  const [query, setQuery] = useState(initialValue);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSubmit(query.trim());
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-3xl relative group">
      <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
        <Search className="h-5 w-5 text-slate-400 group-focus-within:text-blue-400 transition-colors" />
      </div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="What do you want to research?"
        className="w-full pl-12 pr-32 py-4 bg-slate-900/50 border border-slate-700 rounded-2xl text-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 backdrop-blur-sm transition-all"
      />
      <button
        type="submit"
        disabled={!query.trim()}
        className="absolute inset-y-2 right-2 px-6 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-medium rounded-xl hover:from-blue-500 hover:to-indigo-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-slate-900 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
      >
        Search
      </button>
    </form>
  );
}
