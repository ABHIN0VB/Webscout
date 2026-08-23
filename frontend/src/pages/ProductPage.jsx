import { useState, useEffect } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import { ArrowLeft, ExternalLink, Star, Sparkles } from 'lucide-react';
import ScoreBreakdown from '../components/ScoreBreakdown';
import DemoBadge from '../components/DemoBadge';
import { getProduct } from '../services/api';
import { demoProducts } from '../data/demoData';

export default function ProductPage() {
  const { id } = useParams();
  const location = useLocation();
  const navigate = useNavigate();

  const [product, setProduct] = useState(location.state?.product || null);
  const [loading, setLoading] = useState(!location.state?.product);
  const [isDemo, setIsDemo] = useState(!location.state?.product);

  useEffect(() => {
    if (product) return;

    const fetchProduct = async () => {
      try {
        if (id && id !== 'demo') {
          const res = await getProduct(id);
          if (res.data) {
            setProduct(res.data);
            setIsDemo(false);
            setLoading(false);
            return;
          }
        }
      } catch (err) {
        console.warn('Could not fetch product by ID, checking demo catalog', err);
      }

      const fallback = demoProducts.find(p => p.id === id) || demoProducts[0];
      setProduct(fallback);
      setIsDemo(true);
      setLoading(false);
    };

    fetchProduct();
  }, [id, product]);

  const formatPrice = (price) => {
    if (!price && price !== 0) return 'N/A';
    if (typeof price === 'string' && (price.includes('₹') || price.includes('Rs'))) return price;
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(price);
  };

  if (loading || !product) {
    return (
      <div className="max-w-5xl mx-auto px-4 py-24 text-center">
        <div className="animate-pulse text-slate-400 text-lg">Loading product details...</div>
      </div>
    );
  }

  const specs = product.specifications || {};

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {isDemo && <DemoBadge />}

      {/* Back button */}
      <button
        onClick={() => navigate(-1)}
        className="flex items-center gap-2 text-slate-400 hover:text-white mb-6 transition-colors font-medium text-sm"
      >
        <ArrowLeft className="w-4 h-4" /> Back to results
      </button>

      <div className="grid lg:grid-cols-5 gap-8">
        {/* Product Image + Info */}
        <div className="lg:col-span-2">
          <div className="aspect-square bg-gradient-to-br from-slate-900 to-slate-800 rounded-2xl border border-slate-700 flex items-center justify-center mb-6 p-6">
            {product.image_url ? (
              <img src={product.image_url} alt={product.name} className="max-h-full max-w-full object-contain" />
            ) : (
              <div className="w-20 h-20 rounded-2xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
                <Sparkles className="w-10 h-10" />
              </div>
            )}
          </div>

          {/* Match Score */}
          {product.matchScore && (
            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 text-center">
              <div className={`text-4xl font-extrabold ${product.matchScore >= 80 ? 'text-emerald-400' : product.matchScore >= 60 ? 'text-amber-400' : 'text-red-400'}`}>
                {product.matchScore}%
              </div>
              <p className="text-xs text-slate-400 uppercase tracking-wider font-semibold mt-1">Match Score</p>
            </div>
          )}
        </div>

        {/* Details */}
        <div className="lg:col-span-3 space-y-6">
          <div>
            {product.brand && (
              <p className="text-xs text-blue-400 font-semibold uppercase tracking-wider mb-1">{product.brand}</p>
            )}
            <h1 className="text-2xl sm:text-3xl font-bold mb-3 text-white leading-tight">{product.name}</h1>
            <div className="flex items-center gap-4">
              <span className="text-3xl font-extrabold text-emerald-400">{formatPrice(product.price)}</span>
              {product.rating && (
                <span className="flex items-center gap-1.5 text-amber-300 bg-amber-400/10 border border-amber-400/20 px-3 py-1 rounded-full text-sm font-medium">
                  <Star className="w-4 h-4 fill-current" /> {product.rating} / 5.0
                </span>
              )}
            </div>
            {product.availability && (
              <p className="text-xs text-emerald-400 mt-2 font-medium">● {product.availability}</p>
            )}
          </div>

          {/* Specifications Table */}
          <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-lg">
            <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider p-4 border-b border-slate-800">
              Technical Specifications
            </h3>
            <table className="w-full">
              <tbody>
                {Object.entries(specs).length > 0 ? (
                  Object.entries(specs).map(([label, value]) => (
                    <tr key={label} className="border-b border-slate-800/50 last:border-0 hover:bg-slate-850/50 transition-colors">
                      <td className="px-4 py-3 text-xs text-slate-400 w-1/3 capitalize font-medium">{label.replace(/_/g, ' ')}</td>
                      <td className="px-4 py-3 text-xs text-white font-semibold">
                        {value ? String(value) : <span className="text-slate-600 italic">Not listed</span>}
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="2" className="px-4 py-4 text-xs text-slate-500 text-center">
                      Verified standard marketplace listing.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>

          {/* Score Breakdown */}
          {product.score_breakdown && (
            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-lg">
              <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider mb-4">Multi-Factor Score Breakdown</h3>
              <ScoreBreakdown breakdown={product.score_breakdown} />
            </div>
          )}

          {/* AI Reasoning */}
          {product.reasoning && (
            <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5">
              <h3 className="text-xs font-bold text-blue-400 uppercase tracking-wider mb-2">Why This Score</h3>
              <p className="text-slate-300 text-xs leading-relaxed">{product.reasoning}</p>
            </div>
          )}

          {/* Source Link */}
          <div className="flex items-center justify-between bg-slate-900 border border-slate-800 rounded-2xl p-4">
            <div>
              <p className="text-[10px] uppercase font-bold tracking-wider text-slate-500">Data Source</p>
              <p className="text-xs font-semibold text-slate-300">{product.source || 'Smartprix (Bright Data)'}</p>
            </div>
            {product.url && (
              <a
                href={product.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-1.5 text-xs font-semibold text-blue-400 hover:text-blue-300 bg-blue-500/10 px-4 py-2 rounded-xl border border-blue-500/20 transition-all hover:bg-blue-500/20"
              >
                View on Marketplace <ExternalLink className="w-3.5 h-3.5" />
              </a>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
