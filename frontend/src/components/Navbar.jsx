import { Link, useLocation } from 'react-router-dom';
import { Radar } from 'lucide-react';

export default function Navbar() {
  const location = useLocation();

  const navLinks = [
    { name: 'Research', path: '/' },
    { name: 'Scraper Health', path: '/scraper' },
    { name: 'Analytics', path: '/analytics' }
  ];

  return (
    <nav className="fixed top-0 w-full z-50 bg-slate-900/80 backdrop-blur-xl border-b border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-2">
            <Radar className="h-6 w-6 text-blue-500" />
            <Link to="/" className="text-xl font-bold bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
              WEBSCOUT
            </Link>
          </div>
          <div className="flex space-x-8">
            {navLinks.map((link) => (
              <Link
                key={link.name}
                to={link.path}
                className={`text-sm font-medium transition-colors ${
                  location.pathname === link.path || (location.pathname.startsWith('/results') && link.path === '/')
                    ? 'text-blue-400 border-b-2 border-blue-400 pb-[19px] pt-5'
                    : 'text-slate-300 hover:text-white pt-5 pb-[21px]'
                }`}
              >
                {link.name}
              </Link>
            ))}
          </div>
        </div>
      </div>
    </nav>
  );
}
