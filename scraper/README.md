# Bright Data Scraper Studio Integration

## Overview

WebScout uses **Bright Data Scraper Studio** as its web data extraction infrastructure. We do NOT build or maintain our own scraper. Bright Data handles:

- Web page fetching
- Data extraction
- Anti-bot handling
- Self-healing when sites change

## Why Scraper Studio?

1. **No maintenance burden** — Bright Data maintains the extraction logic
2. **Self-healing** — When target sites change their HTML, `bdata scraper heal` repairs the collector automatically
3. **Same Collector ID** — The application code never needs to change when a scraper is healed
4. **Structured output** — The collector returns clean JSON, not raw HTML

## Target Website

**Smartprix** (`https://www.smartprix.com/laptops`)

### Why Smartprix?

- **Niche/Regional site**: Indian tech comparison portal, not a global marketplace
- **No pre-built Bright Data scraper**: Requires a custom Scraper Studio collector
- **Rich public data**: Product names, prices, specs (CPU, RAM, GPU, storage, display), ratings
- **Publicly accessible**: No login required to view product listings
- **Structured listings**: Consistent product card format with specifications

### Why NOT Amazon/Flipkart?

- They already have pre-built Bright Data scrapers
- The hackathon rewards building for the "long tail"
- Using a niche site demonstrates custom Scraper Studio value

## Data Contract

The collector should return JSON objects with this structure:

```json
{
  "name": "ASUS Vivobook Pro 15",
  "brand": "ASUS",
  "model": "Vivobook Pro 15",
  "price": "₹74,990",
  "currency": "INR",
  "url": "https://www.smartprix.com/...",
  "image_url": "https://...",
  "availability": "In Stock",
  "rating": "4.4",
  "processor": "AMD Ryzen 7 7735HS",
  "ram": "16 GB DDR5",
  "storage": "1 TB SSD",
  "gpu": "NVIDIA GeForce RTX 3050",
  "display": "15.6 inch, 1920x1080, 144Hz",
  "battery": "70 Wh"
}
```

Missing fields are handled gracefully by the normalization service.
