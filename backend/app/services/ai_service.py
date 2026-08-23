import re
import json
import logging
from typing import Any
from app.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

try:
    from google import genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False


class AIService:
    def __init__(self):
        self.settings = get_settings()
        self.model = self.settings.LLM_MODEL or "gemini-2.5-flash"
        self.client = None

        if HAS_GENAI and self.settings.LLM_API_KEY:
            try:
                self.client = genai.Client(api_key=self.settings.LLM_API_KEY)
            except Exception as e:
                logger.warning(f"Could not initialize Google GenAI client: {e}")
                self.client = None

    async def parse_query(self, query: str) -> dict[str, Any]:
        """Parse ANY natural language research prompt into structured constraints."""
        if self.client:
            prompt = (
                "You are an expert product research query parser. "
                "Analyze the user's research query and extract structured requirements.\n\n"
                "Return valid JSON matching this schema:\n"
                "{\n"
                '  "category": "laptop" | "monitor" | "keyboard" | "phone" | "general",\n'
                '  "budget": {"max_price": float or null, "min_price": float or null, "currency": "INR"},\n'
                '  "use_cases": [string],\n'
                '  "preferences": {\n'
                '    "ram_min": string or null,\n'
                '    "storage_min": string or null,\n'
                '    "dedicated_gpu": boolean,\n'
                '    "brand_preference": string or null,\n'
                '    "key_features": [string]\n'
                '  }\n'
                "}\n"
                "Only return valid JSON, no markdown formatting.\n\n"
                f"Query: {query}"
            )
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                text = response.text.strip()
                if text.startswith("```json"):
                    text = text[7:-3].strip()
                elif text.startswith("```"):
                    text = text[3:-3].strip()
                return json.loads(text)
            except Exception as e:
                logger.error(f"Error calling LLM for query parsing: {e}")

        # Comprehensive fallback parser for ANY prompt
        q_lower = query.lower()
        budget_max = None

        # Parse Lakhs (e.g. "1.5 lakh", "2 lac", "1.2 Lakhs")
        lakh_match = re.search(r'([\d\.]+)\s*(?:lakhs?|lacs?|l\b)', q_lower)
        if lakh_match:
            try:
                budget_max = float(lakh_match.group(1)) * 100000.0
            except ValueError:
                pass

        # Parse explicit full numbers first (e.g. "under 40000", "below 50,000", "80000", "₹75000")
        if not budget_max:
            num_match = re.search(r'(?:under|below|less than|within|around|budget|price|worth)?\s*(?:₹|rs\.?|inr)?\s*([\d,]{4,7})', q_lower)
            if num_match:
                raw_num = num_match.group(1).replace(',', '')
                try:
                    val = float(raw_num)
                    if val >= 1000:
                        budget_max = val
                except ValueError:
                    pass

        # Parse "k" budget (e.g. "under 80k", "50k", "30k", but NOT "4k monitor" or "2k display")
        if not budget_max:
            # Exclude resolution phrases (2k, 4k, 8k followed by monitor/display/video/screen)
            clean_q = re.sub(r'\b[248]k\s*(?:monitor|display|video|screen|gaming|oled|panel|resolution)?\b', '', q_lower)
            k_match = re.search(r'([\d\.]+)\s*k\b', clean_q)
            if k_match:
                try:
                    budget_max = float(k_match.group(1)) * 1000.0
                except ValueError:
                    pass

        # Detect category
        category = "general"
        if any(w in q_lower for w in ["pet", "dog", "cat", "puppy", "kitten", "retriever", "food", "kibble", "leash"]):
            category = "pet"
        elif any(w in q_lower for w in ["headphone", "earphone", "audio", "earbuds", "speaker", "soundbar", "mic"]):
            category = "audio"
        elif any(w in q_lower for w in ["camera", "drone", "gopro", "lens", "dslr", "mirrorless", "photography"]):
            category = "camera"
        elif any(w in q_lower for w in ["watch", "smartwatch", "fitness", "garmin", "tracker"]):
            category = "smartwatch"
        elif any(w in q_lower for w in ["coffee", "espresso", "latte", "kitchen", "blender", "air fryer"]):
            category = "kitchen"
        elif any(w in q_lower for w in ["chair", "desk", "furniture", "ergonomic", "table"]):
            category = "furniture"
        elif any(w in q_lower for w in ["monitor", "display", "screen"]):
            category = "monitor"
        elif any(w in q_lower for w in ["keyboard", "keychron", "mechanical"]):
            category = "keyboard"
        elif any(w in q_lower for w in ["phone", "smartphone", "mobile"]):
            category = "phone"
        elif any(w in q_lower for w in ["laptop", "macbook", "notebook", "pc", "computer", "thinkpad", "coding", "programming", "docker", "developer"]):
            category = "laptop"
        else:
            category = "general"

        # Detect use-cases
        use_cases = []
        possible_cases = [
            "programming", "coding", "docker", "react", "gaming", "video editing",
            "machine learning", "deep learning", "ai", "graphic design", "3d rendering",
            "college", "student", "office", "work", "portable", "battery", "lightweight",
            "4k", "oled", "144hz", "wireless"
        ]
        for term in possible_cases:
            if term in q_lower:
                use_cases.append(term)

        # Detect RAM preference
        ram_min = None
        ram_m = re.search(r'(\d+)\s*gb\s*ram', q_lower)
        if ram_m:
            ram_min = f"{ram_m.group(1)}GB"
        elif any(u in ['docker', 'machine learning', 'deep learning', 'video editing'] for u in use_cases):
            ram_min = "32GB" if "deep learning" in use_cases or "machine learning" in use_cases else "16GB"
        elif "programming" in use_cases or "gaming" in use_cases:
            ram_min = "16GB"

        # Detect GPU preference
        needs_gpu = any(u in ["gaming", "video editing", "3d rendering", "machine learning", "deep learning", "ai"] for u in use_cases)
        if "rtx" in q_lower or "gpu" in q_lower or "graphics" in q_lower:
            needs_gpu = True

        # Detect brand preference
        brand = None
        for b in ["apple", "macbook", "mac", "asus", "lenovo", "dell", "hp", "acer", "samsung", "msi", "keychron", "logitech", "lg", "benq"]:
            if b in q_lower:
                brand = "Apple" if b in ["apple", "macbook", "mac"] else b.capitalize()
                break

        return {
            "category": category,
            "budget": {"max_price": budget_max, "min_price": None, "currency": "INR"},
            "use_cases": use_cases or ["general use", "performance"],
            "preferences": {
                "ram_min": ram_min or "16GB",
                "storage_min": "1TB SSD" if "video editing" in use_cases else "512GB SSD",
                "dedicated_gpu": needs_gpu,
                "brand_preference": brand
            }
        }

    async def generate_recommendation(self, products: list[dict], requirements: dict[str, Any]) -> str:
        """Generate final tailored recommendation summary text."""
        if not products:
            return "No matching products found."

        if self.client:
            prompt = (
                f"You are an AI research consultant. Generate an insightful recommendation summary for these top results based on the user requirements: {json.dumps(requirements)}.\n\n"
                f"Products: {json.dumps([{ 'name': p.get('name'), 'price': p.get('price'), 'specs': p.get('specifications') } for p in products[:3]])}\n\n"
                "Format with clear highlights, rationale, and value trade-offs."
            )
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                return response.text
            except Exception as e:
                logger.error(f"Error generating recommendation with LLM: {e}")

        # Intelligent dynamic fallback recommendation
        top = products[0]
        runner_up = products[1] if len(products) > 1 else None
        specs = top.get('specifications', {}) or {}
        price_str = f"₹{int(top.get('price')):,}" if top.get('price') else "competitive market price"
        use_cases = requirements.get("use_cases", [])
        use_case_str = ", ".join(use_cases) if use_cases else "your specified requirements"

        rec = (
            f"Based on your requirements for **{use_case_str}**, our top recommendation is the **{top.get('name', 'selected model')}** at {price_str}.\n\n"
            f"**Key Strengths:**\n"
            f"• **Performance:** Powered by {specs.get('processor') or specs.get('panel') or specs.get('switches') or 'high-tier components'} ensuring top performance.\n"
            f"• **Multitasking:** {specs.get('ram') or specs.get('display') or specs.get('layout') or 'balanced hardware'} allows seamless multitasking without bottlenecks.\n"
            f"• **Reliability:** Scraped and verified from **{top.get('source', 'Smartprix')}** with a {top.get('rating', 4.5)}/5 customer rating.\n"
        )
        if runner_up:
            r_price = f"₹{int(runner_up.get('price')):,}" if runner_up.get('price') else ""
            rec += f"\n**Strong Alternative:** The **{runner_up.get('name')}** {r_price} is a great alternative offering comparable value."

        return rec

    async def generate_ranking_explanation(self, product: dict[str, Any], requirements: dict[str, Any], score: float) -> str:
        """Generate brief explanation for product score."""
        if self.client:
            prompt = (
                f"Briefly explain in 1-2 sentences why this product got a score of {score}/100 "
                f"for these requirements: {json.dumps(requirements)}.\n"
                f"Product: {product.get('name')}, Price: {product.get('price')}, Specs: {json.dumps(product.get('specifications'))}"
            )
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt
                )
                return response.text
            except Exception as e:
                logger.error(f"Error generating ranking explanation with LLM: {e}")

        specs = product.get('specifications', {}) or {}
        key_spec = specs.get('processor') or specs.get('display') or specs.get('switches') or 'solid build'
        return (
            f"Achieves a {round(score)}% match score based on {key_spec}, "
            f"competitive pricing, and strong alignment with your use case."
        )
