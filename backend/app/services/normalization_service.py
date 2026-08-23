import re
import hashlib
from typing import Any


class NormalizationService:
    def normalize_product(self, raw: dict[str, Any]) -> dict[str, Any]:
        """Normalize a raw scraped product into a standardized format, preserving all domain-specific specs."""
        normalized = {}
        normalized['name'] = raw.get('name', 'Unknown')
        normalized['brand'] = raw.get('brand', self._extract_brand(normalized['name']))
        normalized['model_name'] = raw.get('model_name')
        normalized['price'] = self.normalize_price(raw.get('price') or raw.get('current_price'))
        normalized['currency'] = "INR"
        normalized['url'] = raw.get('url')
        normalized['image_url'] = raw.get('image_url') or raw.get('image')
        normalized['availability'] = raw.get('availability', 'In Stock')
        normalized['rating'] = self._extract_rating(raw.get('rating'))
        normalized['source'] = raw.get('source', 'Smartprix')

        # Handle specs in different locations
        specs = raw.get('specifications', {})
        if not specs and 'specs' in raw:
            specs = raw['specs']
        if not isinstance(specs, dict):
            specs = {}

        # Build normalized specs dict preserving all domain keys
        cleaned_specs = {}
        for k, v in specs.items():
            k_lower = k.lower()
            if 'ram' in k_lower or 'memory' in k_lower:
                cleaned_specs[k] = self.normalize_ram(v)
            elif 'storage' in k_lower or 'rom' in k_lower or 'ssd' in k_lower or 'hdd' in k_lower:
                cleaned_specs[k] = self.normalize_storage(v)
            elif 'processor' in k_lower or 'cpu' in k_lower:
                cleaned_specs[k] = self.normalize_cpu(v)
            elif 'gpu' in k_lower or 'graphics' in k_lower:
                cleaned_specs[k] = self.normalize_gpu(v)
            elif 'display' in k_lower or 'screen' in k_lower:
                cleaned_specs[k] = self.normalize_display(v)
            else:
                cleaned_specs[k] = str(v).strip() if v is not None else None

        normalized['specifications'] = cleaned_specs
        normalized['raw_data'] = raw
        normalized['content_hash'] = self.generate_content_hash(normalized)
        return normalized

    def _extract_brand(self, name: str) -> str:
        """Extract brand name from product name."""
        if not name:
            return ""
        known_brands = [
            'Apple', 'Lenovo', 'HP', 'Dell', 'ASUS', 'Acer', 'MSI', 'Samsung', 'Microsoft', 'LG',
            'Sony', 'Keychron', 'Logitech', 'Royal Kludge', 'Redragon', 'OnePlus', 'Xiaomi', 'Nothing',
            'Pedigree', 'Royal Canin', 'Drools', 'Whiskas', 'Purina', 'Himalaya', 'Nespresso', 'Philips',
            'Bose', 'Sennheiser', 'Audio-Technica', 'JBL', 'Canon', 'Nikon', 'GoPro', 'Dji', 'Nike', 'Adidas'
        ]
        name_lower = name.lower()
        for b in known_brands:
            if b.lower() in name_lower:
                return b
        return name.split()[0] if name else ""

    def _extract_rating(self, val: Any) -> float | None:
        """Extract numeric rating from various formats."""
        if val is None:
            return None
        if isinstance(val, (int, float)):
            return float(val)
        m = re.search(r'(\d+(\.\d+)?)', str(val))
        return float(m.group(1)) if m else None

    def normalize_price(self, val: Any) -> float | None:
        """Normalize price from formats like '₹74,990', 'Rs. 74990', 'INR 74,990'."""
        if val is None:
            return None
        if isinstance(val, (int, float)):
            return float(val)
        val_str = str(val).strip()
        if not val_str:
            return None
        val_str = val_str.replace(',', '')
        val_str = re.sub(r'[₹$€]', '', val_str)
        val_str = re.sub(r'(?i)^(rs\.?|inr)\s*', '', val_str)
        val_str = val_str.strip()
        m = re.search(r'(\d+(\.\d+)?)', val_str)
        return float(m.group(1)) if m else None

    def normalize_ram(self, val: Any) -> str | None:
        """Normalize RAM from '16GB DDR5', 'RAM: 16GB', '16GB Memory' -> '16 GB'."""
        if val is None:
            return None
        val_str = str(val).strip()
        if not val_str:
            return None
        m = re.search(r'(\d+)\s*GB', val_str, re.IGNORECASE)
        if m:
            return f"{m.group(1)} GB"
        return val_str

    def normalize_storage(self, val: Any) -> str | None:
        """Normalize storage from '1TB SSD', '512GB SSD' -> '1 TB SSD', '512 GB SSD'."""
        if val is None:
            return None
        val_str = str(val).strip()
        if not val_str:
            return None
        val_upper = val_str.upper()
        m = re.search(r'(\d+)\s*(TB|GB)', val_upper)
        if m:
            size = m.group(1)
            unit = m.group(2)
            storage_type = ""
            if 'SSD' in val_upper or 'NVME' in val_upper:
                storage_type = " SSD"
            elif 'HDD' in val_upper:
                storage_type = " HDD"
            return f"{size} {unit}{storage_type}"
        return val_str

    def normalize_cpu(self, val: Any) -> str | None:
        """Clean up CPU name string."""
        if val is None:
            return None
        val_str = str(val).strip()
        if not val_str:
            return None
        val_str = re.sub(r'(?i)^(processor|cpu)[:\s]*', '', val_str).strip()
        return val_str

    def normalize_gpu(self, val: Any) -> str | None:
        """Clean up GPU name string."""
        if val is None:
            return None
        val_str = str(val).strip()
        if not val_str:
            return None
        val_str = re.sub(r'(?i)^(graphics|gpu)[:\s]*', '', val_str).strip()
        return val_str

    def normalize_display(self, val: Any) -> str | None:
        """Clean up display info string."""
        if val is None:
            return None
        val_str = str(val).strip()
        return val_str if val_str else None

    def generate_content_hash(self, product: dict[str, Any]) -> str:
        """Generate a SHA256 hash for deduplication based on brand+model+name."""
        parts = [
            str(product.get('brand', '')).lower().strip(),
            str(product.get('model_name', '')).lower().strip(),
            str(product.get('name', '')).lower().strip()
        ]
        s = "_".join(parts).encode('utf-8')
        return hashlib.sha256(s).hexdigest()
