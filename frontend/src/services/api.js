import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '',
});

export const startResearch = (query) => api.post('/api/research', { query });
export const getResearch = (id) => api.get(`/api/research/${id}`);
export const getProducts = (filters) => api.get('/api/products', { params: filters });
export const getProduct = (id) => api.get(`/api/products/${id}`);
export const compareProducts = (product_ids) => api.post('/api/compare', { product_ids });
export const getScraperStatus = () => api.get('/api/scraper/status');
export const getScraperRuns = () => api.get('/api/scraper/runs');
export const getHealingEvents = () => api.get('/api/scraper/healing-events');
export const getAnalytics = () => api.get('/api/analytics');

export default api;
