import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import LandingPage from './pages/LandingPage';
import ResearchPage from './pages/ResearchPage';
import ResultsPage from './pages/ResultsPage';
import ProductPage from './pages/ProductPage';
import ComparePage from './pages/ComparePage';
import ScraperPage from './pages/ScraperPage';
import AnalyticsPage from './pages/AnalyticsPage';

function App() {
  return (
    <div className="min-h-screen flex flex-col relative bg-slate-950">
      <Navbar />
      <main className="flex-1 pt-16">
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/research" element={<ResearchPage />} />
          <Route path="/results/:id" element={<ResultsPage />} />
          <Route path="/product/:id" element={<ProductPage />} />
          <Route path="/compare" element={<ComparePage />} />
          <Route path="/scraper" element={<ScraperPage />} />
          <Route path="/analytics" element={<AnalyticsPage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
