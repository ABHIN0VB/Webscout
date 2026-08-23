# WebScout Development Rules

This project uses **Bright Data Scraper Studio** as its web data infrastructure.

## Core Principles

1. **Bright Data is the source of truth for web extraction.** Never replace Bright Data with a custom scraper or any alternative scraping engine.

2. **Never create a new collector when an existing collector can be reused.** The primary collector ID is stored in `BRIGHTDATA_COLLECTOR_ID`.

3. **When extraction fails:**
   - Inspect the collector output
   - Identify what changed
   - Use the official `bdata scraper heal` command
   - Re-run the SAME collector
   - Validate the resulting JSON
   - Continue the downstream pipeline

4. **Never expose credentials.** All API keys and tokens are environment variables loaded from `.env`. Never commit `.env`. Never hardcode credentials. Never log credentials.

5. **Only scrape publicly available information.** Never scrape login-protected, private, paywalled, or personal information. Never scrape government websites.

6. **Do not claim simulated data is live.** When `DEMO_MODE=true`, all demo data must be clearly labeled as demo data.

7. **Keep Bright Data logic isolated.** All Bright Data-specific code lives in `backend/app/services/brightdata_service.py`. The rest of the application should not depend on Bright Data internals.

## Architecture

```
User Query → AI Parser → Bright Data Collector → Normalization → Dedup → Ranking → Results
```

## Key Files

- `backend/app/services/brightdata_service.py` — Bright Data API integration
- `backend/app/services/research_service.py` — Research pipeline orchestrator
- `backend/app/services/ai_service.py` — LLM integration (Gemini)
- `backend/app/services/normalization_service.py` — Data normalization
- `backend/app/services/deduplication_service.py` — Product deduplication
- `backend/app/services/ranking_service.py` — Product scoring and ranking

## Target Website

The default target is **Smartprix** (`smartprix.com/laptops`), a niche Indian tech comparison portal. This is NOT a Bright Data pre-built scraper target. The Collector is created via Scraper Studio.

## Self-Healing Workflow

```bash
# Detect failure
bdata scraper run <COLLECTOR_ID> <URL> --pretty

# Heal (same collector)
bdata scraper heal <COLLECTOR_ID> "<description of what broke>"

# Verify (same collector)
bdata scraper run <COLLECTOR_ID> <URL> --pretty
```
