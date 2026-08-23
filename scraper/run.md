# Running the Collector

## Via CLI

Run the collector directly:

```bash
npx -p @brightdata/cli bdata scraper run \
  <COLLECTOR_ID> \
  "https://www.smartprix.com/laptops" \
  --pretty
```

Example:

```bash
npx -p @brightdata/cli bdata scraper run \
  c_abc123def456 \
  "https://www.smartprix.com/laptops" \
  --pretty
```

## Via the API (Programmatic)

WebScout uses the Bright Data HTTP API:

### 1. Trigger the Collector

```bash
curl -X POST "https://api.brightdata.com/dca/trigger?collector=c_abc123def456" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[{"url": "https://www.smartprix.com/laptops"}]'
```

Response:

```json
{"snapshot_id": "s_abc123"}
```

### 2. Retrieve Results

```bash
curl "https://api.brightdata.com/dca/dataset?id=s_abc123" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

Response (when ready): Array of product JSON objects.

## Expected Output

```json
[
  {
    "name": "ASUS Vivobook Pro 15",
    "brand": "ASUS",
    "price": "₹74,990",
    "processor": "AMD Ryzen 7 7735HS",
    "ram": "16 GB DDR5",
    "storage": "1 TB SSD",
    "gpu": "NVIDIA GeForce RTX 3050",
    ...
  },
  ...
]
```

## Troubleshooting

- **Timeout**: Collectors may take 1-5 minutes. The backend polls with exponential backoff.
- **Empty results**: Check that the target URL is accessible and the collector is configured correctly.
- **Authentication error**: Verify your API token in `.env`.
