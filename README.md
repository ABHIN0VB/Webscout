# 🛰️ WebScout — AI Web Research Agent

> **Built for the *WeMakeDevs: Into the Scrape-Verse Hackathon* sponsored by Bright Data**  
> *Autonomous web intelligence agent with deterministic multi-factor ranking and self-healing web scrapers.*

---

## 🌟 Overview

**WebScout** is an autonomous AI product research agent designed to transform unstructured, ever-changing web data into confident purchase decisions. 

Unlike traditional search engines that dump unorganized listings, WebScout:
1. **Parses complex, natural-language requirements** (use-cases, hard budget ceilings, spec preferences).
2. **Collects live, structured product data** from the web using **Bright Data Scraper Studio**.
3. **Cleans, normalizes, and deduplicates** messy marketplace formats.
4. **Deterministically scores and ranks candidates (0–100%)** across budget fit, CPU benchmark tiers, RAM multitasking, fast storage, and graphics.
5. **Surfaces transparent recommendation rationales**, trade-offs, and interactive side-by-side spec comparisons.

---

## ⚡ Key Highlights & Architecture

```
                    ┌────────────────────────┐
                    │ Natural Language Query │
                    └───────────┬────────────┘
                                │
                                ▼
               ┌─────────────────────────────────┐
               │   Gemini 2.5 Flash / AI Parser  │
               │ (Category, Budget, Preferences) │
               └────────────────┬────────────────┘
                                │
                                ▼
               ┌─────────────────────────────────┐
               │    Bright Data Scraper Studio   │
               │   (Remote Crawler / Collector)  │
               └────────────────┬────────────────┘
                                │
                                ▼
               ┌─────────────────────────────────┐
               │  Normalization & Deduplication  │
               │ (SHA-256 Hashes, Strict Budget) │
               └────────────────┬────────────────┘
                                │
                                ▼
               ┌─────────────────────────────────┐
               │  Deterministic Scoring Engine   │
               │ (Budget 25%, CPU 20%, RAM 15%…) │
               └────────────────┬────────────────┘
                                │
                                ▼
               ┌─────────────────────────────────┐
               │    Interactive React Dashboard  │
               │ (Winner Card, Spec Matrix, Logs)│
               └─────────────────────────────────┘
```

---

## 🛡️ Bright Data Scraper Studio & Self-Healing Integration

WebScout uses **Bright Data Scraper Studio** as its core web-data infrastructure:

- **Target Source**: `https://www.smartprix.com/laptops`
- **Collector ID**: Created and managed through the Bright Data CLI (`bdata`) and DCA API.
- **Self-Healing Resilience (`bdata scraper heal`)**: When target website DOM elements change, Bright Data's AI adapts the selector schema without changing the Collector ID, ensuring zero downtime for downstream applications.

---

## 🚀 Features

- 🧠 **Universal Natural Language Parsing**: Handles queries like *"Best lightweight laptop for computer science student under 50k"* or *"High-end 4K video editing laptop with 32GB RAM under 2.5 Lakh"*.
- ⚖️ **Deterministic Mathematical Scoring**: No black-box guesses. Scores are calculated transparently with visible percentage breakdowns.
- 🎯 **Strict Budget Ceiling Guardrails**: Automatically filters out overpriced listings to guarantee recommendations match the user's real budget.
- 📊 **Multi-Product Comparison**: Compare 2–4 products side-by-side with an auto-generated spec matrix.
- 📈 **Scraper Health & Analytics**: Real-time dashboard showing collector health, recovery timelines, and success rates.
- 🌐 **Dual-Engine Execution**: Seamlessly runs with live Bright Data collectors or resilient local simulation.

---

## 📦 Tech Stack

- **Frontend**: React 18, Vite 5, Tailwind CSS, Lucide React, Recharts, React Router v6
- **Backend**: FastAPI, Pydantic v2, SQLAlchemy (Async), aiosqlite / PostgreSQL
- **AI & LLM**: Google Gemini 2.5 Flash (`google-genai`)
- **Web Infrastructure**: Bright Data Scraper Studio, Bright Data CLI (`@brightdata/cli`)

---

## 🛠️ Quick Start & Installation

### 1. Prerequisites
- Python 3.11+
- Node.js 18+ and npm
- Bright Data Account & Google AI Studio Key (Optional for live scraping)

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/webscout.git
cd webscout
```

### 3. Environment Configuration
Copy the example environment file and configure your keys:
```bash
cp .env.example .env
```

Edit `.env`:
```ini
# Bright Data Configuration
BRIGHTDATA_API_TOKEN=your_brightdata_token_here
BRIGHTDATA_COLLECTOR_ID=your_collector_id_here
BRIGHTDATA_TARGET_URL=https://www.smartprix.com/laptops

# Database (Local SQLite auto-configured)
DATABASE_URL=sqlite+aiosqlite:///./webscout.db

# LLM (Google Gemini)
LLM_API_KEY=your_gemini_api_key_here
LLM_MODEL=gemini-2.5-flash

# Mode (false = Live Bright Data, true = Local Seed)
DEMO_MODE=false
```

---

### 4. Running the Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 5. Running the Frontend
```bash
cd frontend
npm install
npm run dev
```

Open **`http://localhost:5173`** in your browser!

---

## 🧪 Running Automated Tests

Run the complete test suite across normalization, deduplication, scoring, and API endpoints:

```bash
python -m pytest tests/ -v
```

All 25 tests pass out of the box with 100% test coverage on core ranking logic.

---

## 🏆 Hackathon Submission Checklist

- [x] Bright Data Scraper Studio Collector integration
- [x] Real-world downstream product (WebScout Research Agent)
- [x] Self-Healing Scraper documentation and monitoring (`/scraper`)
- [x] Deterministic multi-factor ranking engine
- [x] Full automated test suite (25/25 tests passing)
- [x] Responsive, polished React UI with dark theme & glassmorphism

---

## 📄 License
MIT License. Built for the WeMakeDevs Into the Scrape-Verse Hackathon.
