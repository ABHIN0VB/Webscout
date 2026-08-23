# 🛰️ WebScout — AI-Powered Autonomous Web Research Agent

[![Bright Data Scraper Studio](https://img.shields.io/badge/Bright%20Data-Scraper%20Studio-orange?style=for-the-badge&logo=datadog)](https://brightdata.com)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-blue?style=for-the-badge&logo=google)](https://ai.google.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18.3-61DAFB?style=for-the-badge&logo=react)](https://react.dev)
[![Tests](https://img.shields.io/badge/Tests-25%2F25%20Passing%20(100%25)-brightgreen?style=for-the-badge)](https://github.com/ABHIN0VB/Webscout)

> **Built for the *WeMakeDevs: Into the Scrape-Verse Hackathon* sponsored by Bright Data.**  
> *Transforming messy web pages into confident buying decisions through resilient scraping and deterministic AI.*

---

## 🎯 The Problem

Every day, buyers waste hours browsing dozens of e-commerce tabs, comparing confusing specifications, and dealing with outdated prices. Traditional search engines only match keywords and dump thousands of unsorted links—leading to **decision fatigue and buyer remorse**.

Meanwhile, standard web scrapers **break constantly** whenever websites tweak their HTML structure or CSS class names.

---

## 💡 The Solution: WebScout

**WebScout** is an end-to-end autonomous research consultant that combines:
1. **Bright Data Scraper Studio**: Crawls real marketplace websites and automatically self-heals when site layouts change.
2. **Deterministic Mathematical Scoring**: Evaluates candidate products against your exact budget, CPU/GPU tiers, and RAM needs with 100% mathematical transparency (no LLM hallucinations in ranking).
3. **Generative AI Insights (Gemini 2.5 Flash)**: Explains the exact strengths, weaknesses, and trade-offs of the top recommendation.

---

## ⚡ How It Works (The 5-Step Pipeline)

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                                 USER PROMPT                                 │
 │  "Best lightweight budget laptop for computer science student under 50k"    │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────┐   ┌──────────────────────────┐   ┌────────────────────────┐
 │ 1. Intent Extraction    │   │ 2. Web Collection        │   │ 3. Normalization       │
 │ Gemini parses budget,   │──▶│ Bright Data Collector    │──▶│ Cleans INR currencies, │
 │ category, & RAM specs   │   │ crawls Smartprix live    │   │ SHA-256 deduplication  │
 └─────────────────────────┘   └──────────────────────────┘   └────────────────────────┘
                                                                           │
                                                                           ▼
 ┌─────────────────────────┐                                  ┌────────────────────────┐
 │ 5. Executive Summary    │                                  │ 4. Deterministic Rank  │
 │ Gemini writes rationale │◀─────────────────────────────────│ Weighted math scoring  │
 │ & trade-off breakdown   │                                  │ (Budget, CPU, RAM...)  │
 └─────────────────────────┘                                  └────────────────────────┘
```

---

## 🛡️ Bright Data Scraper Studio & Self-Healing Resilience

WebScout treats web scraping as mission-critical infrastructure rather than a fragile script:

### 1. Collector Lifecycle
- **Target URL**: `https://www.smartprix.com/laptops`
- **Collector ID**: Created once via Bright Data CLI and remains **constant** across all runs.
- **API Trigger**: Dispatches asynchronous requests to Bright Data's distributed browser cloud (`POST /dca/trigger`).

### 2. Zero-Downtime Self-Healing (`bdata scraper heal`)
When a target website updates its DOM structure or class names:
- Traditional scrapers crash and return `null` values.
- **Bright Data Scraper Studio AI** inspects the DOM diff, re-maps the extraction selectors, and recovers data **under the exact same Collector ID**.
- WebScout's built-in **Scraper Health Dashboard** (`/scraper`) visually demonstrates this recovery timeline with zero disruption to downstream ranking.

---

## ⚖️ Deterministic Scoring vs Black-Box AI

Unlike generic search apps that ask an LLM to "guess the best laptop", WebScout uses a **strict, multi-factor mathematical scoring engine**:

$$\text{Final Score} = 0.25(\text{Budget}) + 0.20(\text{CPU}) + 0.15(\text{RAM}) + 0.15(\text{Storage}) + 0.15(\text{GPU}) + 0.10(\text{Display})$$

| Factor | Weight | Scoring Logic |
| :--- | :---: | :--- |
| **Budget Fit** | **25%** | 100% if under budget; exponential penalty if exceeding budget ceiling |
| **CPU Performance** | **20%** | Benchmark tier ranking (e.g. Core Ultra / i9 > Ryzen 7 / i7 > Ryzen 5 / i5 > i3) |
| **RAM Multitasking** | **15%** | Evaluates capacity (32GB / 16GB dual-channel vs 8GB base) |
| **Storage Speed** | **15%** | Rewards high-speed NVMe PCIe SSDs over slower drives |
| **GPU / Graphics** | **15%** | Evaluates dedicated Ray Tracing GPUs (RTX 4080/4060) for 3D/gaming needs |
| **Display Quality** | **10%** | High refresh rates (144Hz–240Hz), 4K resolutions, and OLED panels |

---

## 🚀 Key Features

- 🧠 **Universal Multi-Category Intelligence**: Handles Laptops, 4K Monitors, Mechanical Keyboards, Smartphones, Audio, Cameras, Furniture, and Pet Supplies.
- 🎯 **Strict Budget Guardrails**: Eliminates out-of-budget noise so a ₹50,000 search never shows ₹2.5 Lakh machines.
- 📊 **Interactive Comparison Matrix**: Side-by-side spec comparison table for up to 4 selected products.
- 📈 **Real-Time Scraper Analytics**: Visual health cards, recovery time trackers, and historical run reliability charts.
- 🛡️ **Dual-Engine Resilience**: Supports both live Bright Data collectors and seeded marketplace data for offline demonstrations.

---

## 📦 Tech Stack

- **Backend**: FastAPI (Python 3.11+), Async SQLAlchemy, Pydantic v2, aiosqlite / PostgreSQL
- **Frontend**: React 18, Vite 5, Tailwind CSS, Lucide React, Recharts
- **AI & Reasoning**: Google Gemini 2.5 Flash (`google-genai`)
- **Web Infrastructure**: Bright Data Scraper Studio, Bright Data CLI (`@brightdata/cli`)

---

## 🛠️ Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/ABHIN0VB/Webscout.git
cd Webscout
```

### 2. Configure Environment (`.env`)
```bash
cp .env.example .env
```

```ini
# Bright Data Scraper Studio
BRIGHTDATA_API_TOKEN=your_token_here
BRIGHTDATA_COLLECTOR_ID=your_collector_id_here
BRIGHTDATA_TARGET_URL=https://www.smartprix.com/laptops

# Database (Auto-configured SQLite)
DATABASE_URL=sqlite+aiosqlite:///./webscout.db

# Google Gemini (AI Studio)
LLM_API_KEY=your_gemini_api_key_here
LLM_MODEL=gemini-2.5-flash

DEMO_MODE=false
```

### 3. Run Backend (Terminal 1)
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. Run Frontend (Terminal 2)
```bash
cd frontend
npm install
npm run dev
```

Open **`http://localhost:5173`** in your browser!

---

## 🧪 Automated Testing

WebScout includes a comprehensive automated test suite with **100% passing tests**:

```bash
python -m pytest tests/ -v
```

```
======================== 25 passed, 1 warning in 4.00s ========================
```

---

## 🏆 Hackathon Evaluation Summary

| Hackathon Reward Criteria | How WebScout Delivers |
| :--- | :--- |
| **1. Potential Impact** | Solves e-commerce decision fatigue by delivering clear recommendations in seconds. |
| **2. Creativity & Innovation** | Combines deterministic math scoring with generative AI trade-off analysis. |
| **3. Technical Excellence** | Full async FastAPI backend, SHA-256 deduplication, strict budget filtering, 25/25 unit tests. |
| **4. Bright Data Scraper Studio** | Integrates remote DCA trigger API, custom collector schemas, and web data normalization. |
| **5. Reliability & Self-Healing** | Demonstrates `bdata scraper heal` resilience with persistent Collector ID and live telemetry. |
| **6. Presentation** | Glassmorphic React dashboard, spec comparison matrix, and interactive charts. |

---

## 📄 License
MIT License. Created for the **WeMakeDevs: Into the Scrape-Verse Hackathon**.
