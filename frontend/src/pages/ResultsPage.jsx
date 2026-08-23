import { useState, useEffect } from 'react';
import { useLocation, useParams, useNavigate } from 'react-router-dom';
import { Filter, ArrowUpDown, CheckCircle2 } from 'lucide-react';
import RecommendationCard from '../components/RecommendationCard';
import ProductCard from '../components/ProductCard';
import DemoBadge from '../components/DemoBadge';
import { getResearch } from '../services/api';
import { demoProducts, demoResearch } from '../data/demoData';

export default function ResultsPage() {
  const { id } = useParams();
  const location = useLocation();
  const navigate = useNavigate();
  const [research, setResearch] = useState(null);
  const [products, setProducts] = useState([]);
  const [isDemo, setIsDemo] = useState(location.state?.isDemo || false);
  const [selectedForCompare, setSelectedForCompare] = useState([]);
  const [sortBy, setSortBy] = useState('match');
  const query = location.state?.query || research?.query || 'Research Results';

  useEffect(() => {
    if (isDemo || id === 'demo' || !id) {
      setIsDemo(true);
      setResearch(demoResearch);
      setProducts(demoProducts);
      return;
    }

    const fetchResults = async () => {
      try {
        const res = await getResearch(id);
        const data = res.data;
        if (!data || !data.results || data.results.length === 0) {
          setIsDemo(true);
          setResearch(demoResearch);
          setProducts(demoProducts);
          return;
        }
        setResearch(data);
        setProducts(data.results.map(r => ({
          ...r.product,
          matchScore: r.score,
          score_breakdown: r.score_breakdown,
          reasoning: r.reasoning
        })));
      } catch (err) {
        console.warn('API unavailable, using demo data', err);
        setIsDemo(true);
        setResearch(demoResearch);
        setProducts(demoProducts);
      }
    };
    fetchResults();
  }, [id, isDemo]);

  const handleCompare = (product) => {
    setSelectedForCompare(prev => {
      if (prev.find(p => p.id === product.id)) {
        return prev.filter(p => p.id !== product.id);
      }
      if (prev.length < 4) return [...prev, product];
      return prev;
    });
  };

  const sortedProducts = [...products].sort((a, b) => {
    if (sortBy === 'match') return (b.matchScore || 0) - (a.matchScore || 0);
    if (sortBy === 'price-low') return (a.price || 0) - (b.price || 0);
    if (sortBy === 'price-high') return (b.price || 0) - (a.price || 0);
    if (sortBy === 'rating') return (b.rating || 0) - (a.rating || 0);
    return 0;
  });

  if (!products.length) {
    return (
      <div className="max-w-7xl mx-auto px-4 py-20 text-center">
        <div className="animate-pulse text-slate-400">Loading results...</div>
      </div>
    );
  }

  const topMatch = sortedProducts[0];
  const others = sortedProducts.slice(1);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative pb-24">
      {isDemo && <DemoBadge />}

      {/* Query Header */}
      <div className="mb-6">
        <p className="text-sm text-blue-400 font-medium mb-1">Researching</p>
        <h1 className="text-2xl sm:text-3xl font-bold mb-3">{query}</h1>
      </div>

      {/* Pipeline Success */}
      <div className="flex flex-wrap gap-3 mb-6">
        {['Understanding query', 'Collecting web data', 'Normalizing products', 'Comparing results', 'Generating recommendations'].map(step => (
          <div key={step} className="flex items-center gap-1.5 text-xs text-emerald-400">
            <CheckCircle2 className="w-3.5 h-3.5" />
            <span>{step}</span>
          </div>
        ))}
      </div>

      {/* Stats Bar */}
      <div className="flex flex-wrap gap-6 mb-8 p-4 bg-slate-900/50 border border-slate-800 rounded-xl">
        <div>
          <p className="text-2xl font-bold text-white">{research?.product_count || products.length}</p>
          <p className="text-xs text-slate-400">products found</p>
        </div>
        <div className="border-l border-slate-700 pl-6">
          <p className="text-2xl font-bold text-blue-400">{research?.relevant_count || products.length}</p>
          <p className="text-xs text-slate-400">relevant</p>
        </div>
        <div className="border-l border-slate-700 pl-6">
          <p className="text-2xl font-bold text-emerald-400">{research?.top_match_count || products.filter(p => (p.matchScore || 0) > 80).length}</p>
          <p className="text-xs text-slate-400">top matches</p>
        </div>
        <div className="ml-auto flex items-center gap-2">
          <ArrowUpDown className="w-4 h-4 text-slate-400" />
          <select
            value={sortBy}
            onChange={e => setSortBy(e.target.value)}
            className="bg-slate-800 border border-slate-700 text-sm text-slate-300 rounded-lg px-3 py-1.5 focus:outline-none focus:border-blue-500"
          >
            <option value="match">Best Match</option>
            <option value="price-low">Price: Low → High</option>
            <option value="price-high">Price: High → Low</option>
            <option value="rating">Highest Rated</option>
          </select>
        </div>
      </div>

      {/* Top Recommendation */}
      <div className="mb-12">
        <RecommendationCard
          product={topMatch}
          score={topMatch.matchScore}
          reasoning={topMatch.reasoning
            ? topMatch.reasoning.split('. ').filter(s => s.trim()).map(s => s.replace(/\.$/, ''))
            : ['Best performance-to-price ratio', 'Meets all your specified requirements']
          }
          tradeoffs={
            !topMatch.specifications?.battery || topMatch.specifications?.battery === 'N/A'
              ? ['Battery information was not listed by the source']
              : []
          }
        />
      </div>

      {/* AI Summary */}
      {research?.recommendation && (
        <div className="mb-10 p-5 bg-slate-900/60 border border-slate-800 rounded-xl">
          <h3 className="text-sm font-semibold text-blue-400 uppercase tracking-wider mb-3">AI Analysis</h3>
          <p className="text-slate-300 text-sm leading-relaxed whitespace-pre-line">{research.recommendation}</p>
        </div>
      )}

      {/* Product Grid */}
      <div>
        <h2 className="text-xl font-semibold mb-6">All Matches</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {others.map((product, i) => (
            <ProductCard
              key={product.id}
              product={product}
              rank={i + 2}
              onClick={() => navigate(`/product/${product.id}`, { state: { product } })}
              onCompare={handleCompare}
              isCompared={!!selectedForCompare.find(p => p.id === product.id)}
            />
          ))}
        </div>
      </div>

      {/* Source Attribution */}
      <div className="mt-8 text-center">
        <p className="text-xs text-slate-500">
          Data sourced from <span className="text-slate-400 font-medium">Smartprix</span> via Bright Data Scraper Studio
        </p>
      </div>

      {/* Floating Compare Bar */}
      {selectedForCompare.length >= 2 && (
        <div className="fixed bottom-8 left-1/2 -translate-x-1/2 z-50 bg-slate-900/95 border border-blue-500/50 p-4 rounded-2xl shadow-2xl shadow-blue-500/10 flex items-center space-x-6 backdrop-blur-xl">
          <div className="text-slate-300">
            <span className="font-bold text-white">{selectedForCompare.length}</span> products selected
          </div>
          <button
            onClick={() => navigate('/compare', { state: { products: selectedForCompare } })}
            className="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white px-6 py-2 rounded-xl font-medium transition-all"
          >
            Compare Now
          </button>
        </div>
      )}
    </div>
  );
}
