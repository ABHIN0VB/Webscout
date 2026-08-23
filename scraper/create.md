# Creating the Bright Data Collector

## Prerequisites

1. A Bright Data account ([brightdata.com](https://brightdata.com))
2. The Bright Data CLI installed

```bash
npx -p @brightdata/cli bdata login
```

## Create the Collector

```bash
npx -p @brightdata/cli bdata scraper create \
  "https://www.smartprix.com/laptops" \
  "Extract publicly available laptop product listings from this website.

For every product return:
- product name
- brand
- model
- current listed price
- currency (INR)
- product URL
- product image URL if publicly available
- availability status
- user rating if publicly listed
- processor / CPU
- RAM (size and type)
- storage (size and type)
- GPU / graphics card
- display information (size, resolution, refresh rate)
- battery capacity if available

Return structured JSON with one object per product.
Do not extract personal information.
Only use publicly available product information."
```

## Expected Output

The CLI will return a **Collector ID** like:

```
c_xxxxxxxxxxxxxxxxxx
```

**Save this ID!** Add it to your `.env`:

```env
BRIGHTDATA_COLLECTOR_ID=c_xxxxxxxxxxxxxxxxxx
```

## Notes

- The Collector ID persists across runs and healing operations
- Do NOT create a new collector unless absolutely necessary
- The same collector is used before and after healing
- The natural-language prompt can be adjusted for different websites
