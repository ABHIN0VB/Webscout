export const demoProducts = [
  {
    id: '1', name: 'ASUS TUF Gaming A15', brand: 'ASUS', price: 79990, currency: 'INR',
    rating: 4.5, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'Ryzen 7 7735HS', ram: '16 GB', storage: '1 TB SSD', gpu: 'RTX 4050', display: '15.6" FHD 144Hz', battery: '90 Wh' },
    url: 'https://www.smartprix.com/laptops/asus-tuf-gaming-a15', matchScore: 94,
    score_breakdown: { budget: 100, cpu: 90, ram: 90, storage: 100, gpu: 88, display: 77 },
    reasoning: 'Excellent match: fits ₹80k budget, Ryzen 7 handles Docker & React well, 16GB RAM for development, RTX 4050 for gaming, 1TB SSD provides ample storage.'
  },
  {
    id: '2', name: 'Acer Nitro V 15', brand: 'Acer', price: 72990, currency: 'INR',
    rating: 4.4, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'Ryzen 7 7735HS', ram: '16 GB', storage: '1 TB SSD', gpu: 'RTX 4050', display: '15.6" FHD 144Hz', battery: '57 Wh' },
    url: 'https://www.smartprix.com/laptops/acer-nitro-v-15', matchScore: 92,
    score_breakdown: { budget: 100, cpu: 90, ram: 90, storage: 100, gpu: 88, display: 77 },
    reasoning: 'Great value: same specs as TUF A15 at ₹7,000 less. Ryzen 7 + RTX 4050 combo handles all use cases. Trade-off: smaller battery.'
  },
  {
    id: '3', name: 'Lenovo LOQ 15', brand: 'Lenovo', price: 76990, currency: 'INR',
    rating: 4.7, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'i5-13420H', ram: '16 GB', storage: '512 GB SSD', gpu: 'RTX 4050', display: '15.6" FHD 144Hz', battery: '60 Wh' },
    url: 'https://www.smartprix.com/laptops/lenovo-loq-15', matchScore: 88,
    score_breakdown: { budget: 100, cpu: 75, ram: 90, storage: 80, gpu: 88, display: 77 },
    reasoning: 'Strong contender with RTX 4050 and 144Hz display. i5-13420H is capable for Docker. Trade-off: only 512GB storage.'
  },
  {
    id: '4', name: 'ASUS Vivobook Pro 15', brand: 'ASUS', price: 74990, currency: 'INR',
    rating: 4.6, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'Ryzen 7 7735HS', ram: '16 GB', storage: '1 TB SSD', gpu: 'RTX 3050', display: '15.6" FHD 144Hz', battery: '70 Wh' },
    url: 'https://www.smartprix.com/laptops/asus-vivobook-pro-15', matchScore: 86,
    score_breakdown: { budget: 100, cpu: 90, ram: 90, storage: 100, gpu: 80, display: 77 },
    reasoning: 'Ryzen 7 + 16GB + 1TB SSD is excellent for development. RTX 3050 handles light gaming. Good battery life for portability.'
  },
  {
    id: '5', name: 'HP Victus 15', brand: 'HP', price: 69990, currency: 'INR',
    rating: 4.3, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'i5-12500H', ram: '16 GB', storage: '512 GB SSD', gpu: 'RTX 3050', display: '15.6" FHD 144Hz', battery: '52 Wh' },
    url: 'https://www.smartprix.com/laptops/hp-victus-15', matchScore: 81,
    score_breakdown: { budget: 100, cpu: 75, ram: 90, storage: 80, gpu: 80, display: 77 },
    reasoning: 'Budget-friendly gaming option. i5-12500H + RTX 3050 for light gaming. 512GB storage may feel limited for Docker images.'
  },
  {
    id: '6', name: 'MSI Thin 15', brand: 'MSI', price: 71990, currency: 'INR',
    rating: 4.1, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'i5-12450H', ram: '16 GB', storage: '512 GB SSD', gpu: 'RTX 4050', display: '15.6" FHD 144Hz', battery: '53 Wh' },
    url: 'https://www.smartprix.com/laptops/msi-thin-15', matchScore: 83,
    score_breakdown: { budget: 100, cpu: 75, ram: 90, storage: 80, gpu: 88, display: 77 },
    reasoning: 'RTX 4050 is the standout feature at this price. i5-12450H is adequate for development but not ideal for heavy Docker workloads.'
  },
  {
    id: '7', name: 'Samsung Galaxy Book3', brand: 'Samsung', price: 71990, currency: 'INR',
    rating: 4.4, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'i7-1355U', ram: '16 GB', storage: '512 GB SSD', gpu: 'Integrated', display: '15.6" FHD 60Hz', battery: '54 Wh' },
    url: 'https://www.smartprix.com/laptops/samsung-galaxy-book3', matchScore: 68,
    score_breakdown: { budget: 100, cpu: 90, ram: 90, storage: 80, gpu: 20, display: 65 },
    reasoning: 'Strong CPU and build quality, but integrated GPU is a dealbreaker for gaming requirements. Best suited for pure development work.'
  },
  {
    id: '8', name: 'Lenovo IdeaPad Slim 5', brand: 'Lenovo', price: 62990, currency: 'INR',
    rating: 4.5, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'Ryzen 5 7530U', ram: '16 GB', storage: '512 GB SSD', gpu: 'Integrated', display: '15.6" FHD 60Hz', battery: '57 Wh' },
    url: 'https://www.smartprix.com/laptops/lenovo-ideapad-slim-5', matchScore: 64,
    score_breakdown: { budget: 100, cpu: 75, ram: 90, storage: 80, gpu: 20, display: 65 },
    reasoning: 'Great value for programming-only use. Ryzen 5 + 16GB handles React and Docker. No dedicated GPU means gaming is limited.'
  },
  {
    id: '9', name: 'Dell Inspiron 15', brand: 'Dell', price: 58990, currency: 'INR',
    rating: 4.2, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'i5-1335U', ram: '16 GB', storage: '512 GB SSD', gpu: 'Integrated', display: '15.6" FHD 60Hz', battery: '54 Wh' },
    url: 'https://www.smartprix.com/laptops/dell-inspiron-15', matchScore: 62,
    score_breakdown: { budget: 100, cpu: 75, ram: 90, storage: 80, gpu: 20, display: 65 },
    reasoning: 'Budget-friendly for basic development. i5-1335U is capable for React/Node. Not suitable for gaming or heavy Docker workloads.'
  },
  {
    id: '10', name: 'HP Pavilion 15', brand: 'HP', price: 64990, currency: 'INR',
    rating: 4.3, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'Ryzen 5 7535HS', ram: '16 GB', storage: '512 GB SSD', gpu: 'Integrated', display: '15.6" FHD 60Hz', battery: '41 Wh' },
    url: 'https://www.smartprix.com/laptops/hp-pavilion-15', matchScore: 63,
    score_breakdown: { budget: 100, cpu: 75, ram: 90, storage: 80, gpu: 20, display: 65 },
    reasoning: 'Solid build quality with Ryzen 5. Good for programming but no dedicated GPU. Short battery life is a concern.'
  },
  {
    id: '11', name: 'Lenovo ThinkPad E14', brand: 'Lenovo', price: 68990, currency: 'INR',
    rating: 4.6, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'Ryzen 5 7530U', ram: '16 GB', storage: '512 GB SSD', gpu: 'Integrated', display: '14" FHD 60Hz', battery: '57 Wh' },
    url: 'https://www.smartprix.com/laptops/lenovo-thinkpad-e14', matchScore: 65,
    score_breakdown: { budget: 100, cpu: 75, ram: 90, storage: 80, gpu: 20, display: 65 },
    reasoning: 'Premium keyboard and enterprise build quality. Excellent for pure programming. 14" display is compact. No GPU for gaming.'
  },
  {
    id: '12', name: 'ASUS ROG Strix G15', brand: 'ASUS', price: 89990, currency: 'INR',
    rating: 4.8, image_url: null, availability: 'In Stock', source: 'Smartprix',
    specifications: { processor: 'Ryzen 7 7735HS', ram: '16 GB', storage: '1 TB SSD', gpu: 'RTX 4060', display: '15.6" FHD 165Hz', battery: '90 Wh' },
    url: 'https://www.smartprix.com/laptops/asus-rog-strix-g15', matchScore: 78,
    score_breakdown: { budget: 75, cpu: 90, ram: 90, storage: 100, gpu: 92, display: 80 },
    reasoning: 'Exceeds ₹80k budget by ₹10k but has the best GPU (RTX 4060) and display (165Hz). Top choice if budget can stretch.'
  }
];

export const demoResearch = {
  id: 'demo-research-1',
  query: 'Best laptops under ₹80,000 for programming, Docker, React and occasional gaming',
  status: 'completed',
  parsed_requirements: {
    category: 'laptop',
    budget: { max_price: 80000, currency: 'INR' },
    use_cases: ['programming', 'Docker', 'React', 'gaming'],
    preferences: { ram_min: '16GB', storage_min: '512GB SSD', dedicated_gpu: true }
  },
  product_count: 42,
  relevant_count: 12,
  top_match_count: 4,
  recommendation: 'Based on your requirements for programming, Docker, React development, and occasional gaming under ₹80,000, the **ASUS TUF Gaming A15** is your best match at 94%. It combines a powerful Ryzen 7 processor for Docker workloads, 16GB RAM for React development, 1TB SSD for project storage, and an RTX 4050 GPU for gaming — all within your budget at ₹79,990.\n\nThe **Acer Nitro V 15** is an excellent alternative at ₹72,990 with nearly identical specs, saving you ₹7,000.\n\nIf budget allows a stretch, the **ASUS ROG Strix G15** at ₹89,990 offers the RTX 4060 for superior gaming performance.',
  results: demoProducts.map((p, i) => ({
    product: p,
    score: p.matchScore,
    rank: i + 1,
    reasoning: p.reasoning,
    score_breakdown: p.score_breakdown
  })),
  created_at: new Date().toISOString(),
  completed_at: new Date().toISOString()
};

export const demoScraperStatus = {
  status: 'healthy',
  collectorId: 'c_m3x7k9p2q1w4',
  collector_id: 'c_m3x7k9p2q1w4',
  lastRun: new Date().toISOString(),
  last_run: new Date().toISOString(),
  records: 42,
  target_url: 'https://www.smartprix.com/laptops'
};

export const demoRuns = [
  { id: '1', time: new Date().toISOString(), started_at: new Date().toISOString(), status: 'completed', records: 42, duration: '47s', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '2', time: new Date(Date.now() - 3600000).toISOString(), started_at: new Date(Date.now() - 3600000).toISOString(), status: 'completed', records: 41, duration: '52s', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '3', time: new Date(Date.now() - 7200000).toISOString(), started_at: new Date(Date.now() - 7200000).toISOString(), status: 'failed', records: 0, duration: '8s', error: 'Extraction failed: required fields missing', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '4', time: new Date(Date.now() - 7100000).toISOString(), started_at: new Date(Date.now() - 7100000).toISOString(), status: 'healed', records: 41, duration: '38s', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '5', time: new Date(Date.now() - 10800000).toISOString(), started_at: new Date(Date.now() - 10800000).toISOString(), status: 'completed', records: 40, duration: '45s', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '6', time: new Date(Date.now() - 14400000).toISOString(), started_at: new Date(Date.now() - 14400000).toISOString(), status: 'completed', records: 42, duration: '43s', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '7', time: new Date(Date.now() - 18000000).toISOString(), started_at: new Date(Date.now() - 18000000).toISOString(), status: 'completed', records: 39, duration: '50s', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '8', time: new Date(Date.now() - 86400000).toISOString(), started_at: new Date(Date.now() - 86400000).toISOString(), status: 'failed', records: 0, duration: '5s', error: 'Connection timeout', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '9', time: new Date(Date.now() - 86300000).toISOString(), started_at: new Date(Date.now() - 86300000).toISOString(), status: 'healed', records: 38, duration: '41s', collector_id: 'c_m3x7k9p2q1w4' },
  { id: '10', time: new Date(Date.now() - 90000000).toISOString(), started_at: new Date(Date.now() - 90000000).toISOString(), status: 'completed', records: 42, duration: '44s', collector_id: 'c_m3x7k9p2q1w4' },
];

export const demoHealingEvents = [
  {
    id: '1',
    timestamp: new Date(Date.now() - 7200000).toISOString(),
    started_at: new Date(Date.now() - 7200000).toISOString(),
    type: 'extraction_failure',
    collector_id: 'c_m3x7k9p2q1w4',
    description: 'Product price and title extraction broke after the site\'s HTML structure changed.',
    status: 'completed',
    command: `$ bdata scraper run c_m3x7k9p2q1w4 "https://www.smartprix.com/laptops" --pretty

Starting collector c_m3x7k9p2q1w4...
Fetching target page...
Extracting products...

✗ Required fields missing: price, name
✗ 0 of 42 products extracted

──────────────────────────────────────

$ bdata scraper heal c_m3x7k9p2q1w4 \\
  "Product price and title extraction broke after the site's HTML structure changed."

Analyzing target DOM...
Detecting structural changes...
Rebuilding extraction selectors...
Validating new extraction logic...
Updating collector c_m3x7k9p2q1w4...

✓ Collector healed successfully

──────────────────────────────────────

$ bdata scraper run c_m3x7k9p2q1w4 "https://www.smartprix.com/laptops" --pretty

Starting collector c_m3x7k9p2q1w4...
Fetching target page...
Extracting products...

✓ 42 products extracted successfully

SAME COLLECTOR ID: c_m3x7k9p2q1w4`
  },
  {
    id: '2',
    timestamp: new Date(Date.now() - 86400000).toISOString(),
    started_at: new Date(Date.now() - 86400000).toISOString(),
    type: 'timeout_failure',
    collector_id: 'c_m3x7k9p2q1w4',
    description: 'Page load timeout due to lazy loading changes.',
    status: 'completed',
    command: `$ bdata scraper run c_m3x7k9p2q1w4 "https://www.smartprix.com/laptops" --pretty

Starting collector c_m3x7k9p2q1w4...
Fetching target page...

✗ Timeout: page did not load within 30s

──────────────────────────────────────

$ bdata scraper heal c_m3x7k9p2q1w4 \\
  "Page loading timeout, possibly due to new lazy-loading implementation."

Analyzing page load behavior...
Adjusting wait strategies...
Updating collector c_m3x7k9p2q1w4...

✓ Collector healed successfully

──────────────────────────────────────

$ bdata scraper run c_m3x7k9p2q1w4 "https://www.smartprix.com/laptops" --pretty

✓ 38 products extracted successfully

SAME COLLECTOR ID: c_m3x7k9p2q1w4`
  }
];

export const demoAnalytics = {
  total_runs: 96,
  totalRuns: 96,
  successful_runs: 88,
  successful: 88,
  failed_runs: 8,
  failed: 8,
  healed_runs: 8,
  healed: 8,
  total_records: 3780,
  records: 3780,
  records_recovered: 316,
  avg_recovery_time_seconds: 34.2,
  recoveryTime: '34.2s',
  run_history: [
    { date: 'Aug 17', success: 12, failed: 1 },
    { date: 'Aug 18', success: 14, failed: 0 },
    { date: 'Aug 19', success: 13, failed: 2 },
    { date: 'Aug 20', success: 15, failed: 1 },
    { date: 'Aug 21', success: 14, failed: 2 },
    { date: 'Aug 22', success: 12, failed: 1 },
    { date: 'Aug 23', success: 8, failed: 1 },
  ],
  healing_history: [
    { date: 'Aug 17', healed: 1, records_recovered: 38 },
    { date: 'Aug 19', healed: 2, records_recovered: 82 },
    { date: 'Aug 20', healed: 1, records_recovered: 41 },
    { date: 'Aug 21', healed: 2, records_recovered: 79 },
    { date: 'Aug 22', healed: 1, records_recovered: 42 },
    { date: 'Aug 23', healed: 1, records_recovered: 34 },
  ]
};
