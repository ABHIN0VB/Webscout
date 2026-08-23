# Self-Healing the Collector

## When to Heal

Self-healing is needed when:

- The target website changes its HTML structure
- Product fields are missing from extraction results
- The collector returns empty or malformed data
- CSS selectors or page layout has changed

## How to Heal

Use the **same Collector ID** — never create a new collector:

```bash
npx -p @brightdata/cli bdata scraper heal \
  <COLLECTOR_ID> \
  "Product title and price extraction broke after the site's HTML structure changed."
```

### Example

```bash
# 1. Run the collector — observe failure
npx -p @brightdata/cli bdata scraper run c_abc123def456 \
  "https://www.smartprix.com/laptops" --pretty

# Output: Empty results or missing fields

# 2. Heal the collector
npx -p @brightdata/cli bdata scraper heal c_abc123def456 \
  "Product price and title extraction broke after the site's HTML structure changed. \
   Product cards are no longer extracting the name, price, and specification fields."

# Output: Bright Data AI analyzes the target, rebuilds extraction logic

# 3. Re-run the SAME collector
npx -p @brightdata/cli bdata scraper run c_abc123def456 \
  "https://www.smartprix.com/laptops" --pretty

# Output: Products successfully recovered
```

## Key Points

1. **SAME Collector ID** — The collector ID does not change during healing
2. **No application code changes** — WebScout keeps working with the same collector
3. **Bright Data handles the AI repair** — We do not implement custom healing logic
4. **The downstream pipeline is unaffected** — Same JSON schema in, same analysis out

## What We Do NOT Do

- ❌ Build custom scraper repair
- ❌ AI-based selector fixing
- ❌ Create a new collector to "replace" the broken one
- ❌ Fake the healing process in the UI

## What We DO

- ✅ Detect extraction failures (missing fields, empty results)
- ✅ Log the failure event
- ✅ Call `bdata scraper heal` with a description of what broke
- ✅ Re-run the same collector
- ✅ Validate recovered data
- ✅ Show the healing event in the UI
