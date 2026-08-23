"""Deterministic product ranking service.

All scoring is deterministic — no LLM calls.
LLM is only used in AIService for explanation text.

Weights: budget=25%, cpu=20%, ram=15%, storage=15%, gpu=15%, display=10%
"""
import re
from typing import Any


class RankingService:
    """Score and rank products against user requirements."""

    WEIGHTS = {
        "budget": 0.25,
        "cpu": 0.20,
        "ram": 0.15,
        "storage": 0.15,
        "gpu": 0.15,
        "display": 0.10,
    }

    def rank_products(self, products: list[dict], requirements: dict) -> list[dict]:
        """Rank products against structured requirements. Returns products with scores."""
        budget_max = None
        budget_info = requirements.get("budget", {})
        if isinstance(budget_info, dict):
            budget_max = budget_info.get("max_price")

        use_cases = requirements.get("use_cases", [])
        prefs = requirements.get("preferences", {})

        ram_min = prefs.get("ram_min")
        storage_min = prefs.get("storage_min")
        needs_dedicated_gpu = prefs.get("dedicated_gpu", False)

        # If gaming is in use cases, default to needing dedicated GPU
        if not needs_dedicated_gpu and any("gam" in uc.lower() for uc in use_cases):
            needs_dedicated_gpu = True

        brand_pref = prefs.get("brand_preference")

        ranked = []
        for p in products:
            price = p.get("price")
            specs = p.get("specifications", {}) or {}
            prod_brand = p.get("brand", "")

            breakdown = {
                "budget": self.score_budget_fit(price, budget_max),
                "cpu": self.score_cpu(specs.get("processor") or specs.get("panel") or specs.get("switches"), use_cases),
                "ram": self.score_ram(specs.get("ram") or specs.get("layout"), ram_min),
                "storage": self.score_storage(specs.get("storage") or specs.get("connectivity"), storage_min),
                "gpu": self.score_gpu(specs.get("gpu") or specs.get("camera"), needs_dedicated_gpu),
                "display": self._score_display(specs.get("display") or specs.get("resolution")),
            }

            total = self.calculate_overall_score(breakdown)

            # Strict budget constraint penalty
            if budget_max and price and price > budget_max:
                overshoot_pct = (price - budget_max) / budget_max
                if overshoot_pct > 0.35:  # Significantly over budget (e.g. > 35% over budget)
                    total = max(10.0, total * 0.25)
                elif overshoot_pct > 0.15:  # Moderately over budget
                    total = max(25.0, total * 0.65)
                elif overshoot_pct > 0.05:  # Slightly over budget
                    total = total * 0.88

            # Boost if user specifically requested this brand
            if brand_pref and prod_brand and brand_pref.lower() in prod_brand.lower():
                total = min(99.0, total + 12.0)

            ranked.append({
                **p,
                "score": round(total, 1),
                "score_breakdown": {k: round(v, 1) for k, v in breakdown.items()},
            })

        ranked.sort(key=lambda x: x["score"], reverse=True)

        for i, item in enumerate(ranked):
            item["rank"] = i + 1

        return ranked

    def score_budget_fit(self, price: float | None, budget: float | None) -> float:
        """Score how well the price fits the budget. 100 = under budget."""
        if budget is None:
            return 100.0
        if price is None:
            return 50.0
        if price <= budget:
            return 100.0
        # Linear penalty for exceeding budget
        overshoot = (price - budget) / budget
        return max(0.0, 100.0 - overshoot * 200)

    def score_ram(self, ram_str: str | None, min_ram: str | None) -> float:
        """Score RAM against minimum requirement."""
        ram_gb = self._extract_gb(ram_str)

        if min_ram is None:
            if ram_gb is None:
                return 50.0
            if ram_gb >= 32:
                return 100.0
            if ram_gb >= 16:
                return 85.0
            if ram_gb >= 8:
                return 65.0
            return 40.0

        min_gb = self._extract_gb(str(min_ram))
        if min_gb is None:
            min_gb = 8

        if ram_gb is None:
            return 50.0
        if ram_gb >= min_gb * 2:
            return 100.0
        if ram_gb >= min_gb:
            return 90.0
        if ram_gb >= min_gb * 0.5:
            return 60.0
        return 30.0

    def score_storage(self, storage_str: str | None, min_storage: str | None) -> float:
        """Score storage against minimum requirement."""
        storage_gb = self._extract_storage_gb(storage_str)

        if min_storage is None:
            if storage_gb is None:
                return 50.0
            if storage_gb >= 1024:
                return 100.0
            if storage_gb >= 512:
                return 80.0
            if storage_gb >= 256:
                return 60.0
            return 40.0

        min_gb = self._extract_storage_gb(str(min_storage))
        if min_gb is None:
            min_gb = 512

        if storage_gb is None:
            return 50.0
        if storage_gb >= min_gb * 2:
            return 100.0
        if storage_gb >= min_gb:
            return 90.0
        if storage_gb >= min_gb * 0.5:
            return 60.0
        return 30.0

    def score_gpu(self, gpu_str: str | None, needs_dedicated: bool) -> float:
        """Score GPU. Dedicated GPUs score higher when gaming/GPU work is needed."""
        if gpu_str is None:
            return 10.0 if needs_dedicated else 50.0

        gpu_upper = gpu_str.upper()
        is_dedicated = any(kw in gpu_upper for kw in [
            "RTX", "GTX", "RADEON RX", "ARC A", "MX"
        ])

        if needs_dedicated:
            if not is_dedicated:
                return 20.0
            if "RTX 4090" in gpu_upper:
                return 100.0
            if "RTX 4080" in gpu_upper:
                return 98.0
            if "RTX 4070" in gpu_upper:
                return 95.0
            if "RTX 4060" in gpu_upper:
                return 92.0
            if "RTX 4050" in gpu_upper:
                return 88.0
            if "RTX 3060" in gpu_upper:
                return 85.0
            if "RTX 3050" in gpu_upper:
                return 80.0
            if "GTX 1650" in gpu_upper:
                return 65.0
            return 75.0
        else:
            if is_dedicated:
                return 80.0
            return 65.0

    def score_cpu(self, cpu_str: str | None, use_cases: list[str]) -> float:
        """Score CPU tier. Higher-end CPUs score better."""
        if cpu_str is None:
            return 50.0

        cpu_upper = cpu_str.upper()
        tier = self._get_cpu_tier(cpu_upper)

        has_heavy_use = any(
            uc.lower() in ["docker", "gaming", "video editing", "3d rendering", "machine learning", "compilation"]
            for uc in use_cases
        )

        base_scores = {
            "ultra": 100.0,
            "high": 90.0,
            "mid": 75.0,
            "low": 50.0,
            "entry": 35.0,
        }

        score = base_scores.get(tier, 60.0)

        if has_heavy_use and tier in ("low", "entry"):
            score -= 10
        elif has_heavy_use and tier in ("high", "ultra"):
            score += 5

        return min(100.0, max(0.0, score))

    def _score_display(self, display_str: str | None) -> float:
        """Score display quality."""
        if display_str is None:
            return 50.0
        d = display_str.upper()
        score = 60.0
        if "4K" in d or "3840" in d or "2880" in d:
            score += 25
        elif "2K" in d or "2560" in d or "QHD" in d:
            score += 15
        elif "1920" in d or "FHD" in d or "FULL HD" in d:
            score += 5
        if "165HZ" in d or "165 HZ" in d:
            score += 15
        elif "144HZ" in d or "144 HZ" in d:
            score += 12
        elif "120HZ" in d or "120 HZ" in d:
            score += 8
        return min(100.0, score)

    def _get_cpu_tier(self, cpu_upper: str) -> str:
        """Classify CPU into performance tier."""
        if any(x in cpu_upper for x in ["I9", "RYZEN 9", "M3 MAX", "M3 PRO", "M4"]):
            return "ultra"
        if any(x in cpu_upper for x in ["I7", "RYZEN 7", "M3", "M2 PRO"]):
            return "high"
        if any(x in cpu_upper for x in ["I5", "RYZEN 5", "M2", "M1"]):
            return "mid"
        if any(x in cpu_upper for x in ["I3", "RYZEN 3"]):
            return "low"
        if any(x in cpu_upper for x in ["CELERON", "PENTIUM", "ATHLON"]):
            return "entry"
        return "mid"

    def _extract_gb(self, val: str | None) -> int | None:
        """Extract GB value from string like '16 GB', '16GB', '16'."""
        if val is None:
            return None
        m = re.search(r'(\d+)\s*GB', str(val), re.IGNORECASE)
        if m:
            return int(m.group(1))
        m = re.search(r'^(\d+)$', str(val).strip())
        if m:
            return int(m.group(1))
        return None

    def _extract_storage_gb(self, val: str | None) -> int | None:
        """Extract storage in GB from string like '1 TB SSD', '512GB'."""
        if val is None:
            return None
        val_str = str(val).upper()
        m = re.search(r'(\d+)\s*TB', val_str)
        if m:
            return int(m.group(1)) * 1024
        m = re.search(r'(\d+)\s*GB', val_str)
        if m:
            return int(m.group(1))
        return None

    def calculate_overall_score(self, breakdown: dict[str, float]) -> float:
        """Weighted average of all scores."""
        total = 0.0
        for key, weight in self.WEIGHTS.items():
            total += breakdown.get(key, 50.0) * weight
        return total
