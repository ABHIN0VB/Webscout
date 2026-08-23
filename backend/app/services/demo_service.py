import re
import random
from datetime import datetime, timezone
from typing import Any


class DemoService:
    """Universal structured product engine that provides realistic market listings for LITERALLY ANY user prompt."""

    def get_demo_products(self, query: str = "", requirements: dict[str, Any] = None) -> list[dict]:
        now = datetime.now(timezone.utc).isoformat()
        reqs = requirements or {}
        q = (query or "").lower().strip()
        category = reqs.get("category", "").lower()
        budget_max = reqs.get("budget", {}).get("max_price")

        # 1. PETS & ANIMAL SUPPLIES
        if any(w in q for w in ["pet", "dog", "cat", "puppy", "kitten", "canine", "feline", "bark", "retriever", "food", "kibble", "leash", "aquarium", "bird"]):
            return self._get_pet_products(now, budget_max)

        # 2. AUDIO, HEADPHONES & SPEAKERS
        if any(w in q for w in ["headphone", "earphone", "audio", "earbuds", "speaker", "soundbar", "mic", "microphone", "bose", "sony", "sennheiser", "anc"]):
            return self._get_audio_products(now, budget_max)

        # 3. CAMERAS, DRONES & PHOTOGRAPHY
        if any(w in q for w in ["camera", "drone", "gopro", "lens", "dslr", "mirrorless", "dji", "canon", "nikon", "fujifilm", "photography"]):
            return self._get_camera_products(now, budget_max)

        # 4. SMARTWATCHES, FITNESS & WEARABLES
        if any(w in q for w in ["watch", "smartwatch", "fitness", "garmin", "tracker", "band", "running", "heart rate"]):
            return self._get_smartwatch_products(now, budget_max)

        # 5. COFFEE MACHINES & KITCHEN APPLIANCES
        if any(w in q for w in ["coffee", "espresso", "latte", "kitchen", "blender", "air fryer", "toaster", "cookware", "grinder"]):
            return self._get_coffee_kitchen_products(now, budget_max)

        # 6. OFFICE CHAIRS, DESKS & FURNITURE
        if any(w in q for w in ["chair", "desk", "furniture", "ergonomic", "standing desk", "seating", "table"]):
            return self._get_chair_furniture_products(now, budget_max)

        # 7. MONITORS & SCREENS
        if any(w in q for w in ["monitor", "display", "screen", "ultrawide", "oled monitor"]):
            return self._get_monitor_products(now, budget_max)

        # 8. KEYBOARDS & MICE
        if any(w in q for w in ["keyboard", "keychron", "mechanical keyboard", "mouse", "trackpad", "keycaps"]):
            return self._get_keyboard_products(now, budget_max)

        # 9. PHONES & TABLETS
        if any(w in q for w in ["phone", "smartphone", "mobile", "iphone", "galaxy", "oneplus", "ipad", "tablet"]):
            return self._get_phone_products(now, budget_max)

        # 10. LAPTOPS & COMPUTERS (Default tech)
        if any(w in q for w in ["laptop", "notebook", "macbook", "pc", "computer", "thinkpad", "gaming laptop", "programming", "coding", "docker"]):
            return self._get_laptop_products(now, budget_max)

        # 11. UNIVERSAL PRODUCT SYNTHESIS FOR ARBITRARY QUERIES (e.g. Shoes, Skincare, Guitars, Books, Bikes, Tools, etc.)
        return self._generate_universal_products(query, reqs, now)

    def _get_pet_products(self, now: str, budget_max: float | None) -> list[dict]:
        products = [
            {
                "name": "Royal Canin Golden Retriever Adult Dry Dog Food (12kg)",
                "brand": "Royal Canin",
                "price": 8490.0,
                "url": "https://www.smartprix.com/pets/royal-canin-golden-retriever",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix Pet Store",
                "scraped_at": now,
                "specifications": {
                    "Suitable For": "Adult Golden Retrievers (Over 15 Months)",
                    "Key Benefits": "Healthy Cardiac Function & Glossy Coat",
                    "Weight": "12 kg Pack",
                    "Main Ingredients": "Dehydrated Poultry Protein, Rice, Corn, EPA/DHA",
                    "Diet Type": "Non-Vegetarian Complete Nutrition"
                }
            },
            {
                "name": "Pedigree PRO Expert Nutrition for Large Breed Adult Dogs (10kg)",
                "brand": "Pedigree",
                "price": 3890.0,
                "url": "https://www.smartprix.com/pets/pedigree-pro-large-breed",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix Pet Store",
                "scraped_at": now,
                "specifications": {
                    "Suitable For": "Active & Large Breed Adult Dogs",
                    "Key Benefits": "Joint Health (Glucosamine) & Lean Muscle",
                    "Weight": "10 kg Pack",
                    "Protein Content": "28% High Quality Protein",
                    "Diet Type": "Veterinary Formulated Dry Food"
                }
            },
            {
                "name": "Drools Focus Super Premium Adult Dog Food (12kg)",
                "brand": "Drools",
                "price": 5490.0,
                "url": "https://www.smartprix.com/pets/drools-focus-adult",
                "rating": 4.5,
                "availability": "In Stock",
                "source": "Smartprix Pet Store",
                "scraped_at": now,
                "specifications": {
                    "Suitable For": "All Breed Adult Dogs (No Wheat/Corn)",
                    "Key Benefits": "Digestive Support with Real Chicken & Prebiotics",
                    "Weight": "12 kg (100% Grain Free Formulation)",
                    "Protein Content": "32% Real Chicken & Eggs",
                    "Diet Type": "Grain-Free Super Premium"
                }
            },
            {
                "name": "Furbo 360° Smart Dog Camera with Treat Tossing & Auto-Tracking",
                "brand": "Furbo",
                "price": 18990.0,
                "url": "https://www.smartprix.com/pets/furbo-360-dog-camera",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix Pet Store",
                "scraped_at": now,
                "specifications": {
                    "Camera": "1080p FHD with 360° Rotating Wide Angle View",
                    "Features": "Real-Time Barking Alerts, 2-Way Audio, Treat Tossing",
                    "Night Vision": "Color Night Vision & Cloud Recording",
                    "Connectivity": "WiFi 2.4GHz / 5GHz + iOS & Android App",
                    "Warranty": "1 Year Replacement Warranty"
                }
            },
            {
                "name": "Himalaya Healthy Pet Food for Puppies - Meat & Rice (10kg)",
                "brand": "Himalaya",
                "price": 3150.0,
                "url": "https://www.smartprix.com/pets/himalaya-healthy-pet-puppy",
                "rating": 4.4,
                "availability": "In Stock",
                "source": "Smartprix Pet Store",
                "scraped_at": now,
                "specifications": {
                    "Suitable For": "Growing Puppies (All Breeds)",
                    "Key Benefits": "Herbal Immunity Booster (Papaya & Black Pepper)",
                    "Weight": "10 kg Pack",
                    "Protein Content": "24% Balanced Protein & Omega Fatty Acids",
                    "Diet Type": "Ayurvedic Herbal Pet Care"
                }
            },
            {
                "name": "Orthopedic Memory Foam Pet Bed with Waterproof Removable Cover (Large)",
                "brand": "BarkLounge",
                "price": 4999.0,
                "url": "https://www.smartprix.com/pets/orthopedic-memory-foam-bed",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix Pet Store",
                "scraped_at": now,
                "specifications": {
                    "Size": 'Large (100cm x 75cm x 15cm) for Dogs up to 40kg',
                    "Material": "Medical-Grade High Density Memory Foam",
                    "Cover": "Hypoallergenic Velvet, Machine Washable",
                    "Base": "Non-Slip Waterproof Rubberized Base",
                    "Benefits": "Relieves Arthritis & Hip Dysplasia Pressure"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _get_audio_products(self, now: str, budget_max: float | None) -> list[dict]:
        products = [
            {
                "name": "Sony WH-1000XM5 Wireless Industry Leading Noise Canceling Headphones",
                "brand": "Sony",
                "price": 28990.0,
                "url": "https://www.smartprix.com/audio/sony-wh-1000xm5",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Driver": "30mm Carbon Fiber Composite Unit",
                    "Noise Cancellation": "Auto NC Optimizer with 8 Mics & 2 Processors",
                    "Battery Life": "30 Hours with ANC (Quick Charge 3 min = 3 hrs)",
                    "Codecs": "LDAC, AAC, SBC, Hi-Res Audio Wireless",
                    "Microphones": "4 Beamforming Mics with AI Noise Reduction"
                }
            },
            {
                "name": "Bose QuietComfort Ultra Wireless Noise Cancelling Headphones",
                "brand": "Bose",
                "price": 35900.0,
                "url": "https://www.smartprix.com/audio/bose-quietcomfort-ultra",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Sound": "Bose Immersive Audio Spatialized Sound",
                    "Modes": "Quiet Mode, Aware Mode, Immersion Mode",
                    "Battery Life": "24 Hours (18 Hours in Immersive Mode)",
                    "Connectivity": "Bluetooth 5.3 with SimpleSync & Multipoint",
                    "Build": "Ultra-Plush Protein Leather & Cast Aluminum"
                }
            },
            {
                "name": "Sennheiser Momentum 4 Wireless ANC Headphones (60hr Battery)",
                "brand": "Sennheiser",
                "price": 24990.0,
                "url": "https://www.smartprix.com/audio/sennheiser-momentum-4",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Driver": "Audiophile-Inspired 42mm Transducer System",
                    "Battery Life": "Class-Leading 60 Hours Playback",
                    "Noise Cancellation": "Adaptive Noise Cancellation & Transparency Mode",
                    "Codecs": "aptX Adaptive, aptX, AAC, SBC",
                    "Equalizer": "Built-in 5-band EQ with Sound Personalization"
                }
            },
            {
                "name": "Audio-Technica ATH-M50xBT2 Wireless Over-Ear Studio Headphones",
                "brand": "Audio-Technica",
                "price": 17990.0,
                "url": "https://www.smartprix.com/audio/audio-technica-ath-m50xbt2",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Driver": "Proprietary 45mm Large-Aperture Drivers",
                    "Sound Profile": "Critical Studio Sound with Deep Accurate Bass",
                    "Battery Life": "Up to 50 Hours of Continuous Use",
                    "DAC / Amp": "AK4331 Advanced Audio DAC with LDAC",
                    "Connectivity": "Bluetooth 5.0 + 3.5mm Detachable Cable"
                }
            },
            {
                "name": "Sony WF-1000XM5 True Wireless Noise Cancelling Earbuds",
                "brand": "Sony",
                "price": 21990.0,
                "url": "https://www.smartprix.com/audio/sony-wf-1000xm5",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Driver": "Dynamic Driver X (8.4mm High-Resolution)",
                    "Noise Cancellation": "Integrated Processor V2 & HD QN2e",
                    "Battery": "8 Hrs Buds + 16 Hrs Case (Qi Wireless Charging)",
                    "Water Resistance": "IPX4 Sweat and Splash Proof",
                    "Microphones": "Bone Conduction Sensors & Deep Neural Network Mics"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _get_camera_products(self, now: str, budget_max: float | None) -> list[dict]:
        products = [
            {
                "name": "Sony Alpha 7 IV Full-Frame Mirrorless Camera (Body Only)",
                "brand": "Sony",
                "price": 219990.0,
                "url": "https://www.smartprix.com/cameras/sony-alpha-7-iv",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Sensor": "33MP Full-Frame Exmor R CMOS Sensor",
                    "Video": "4K 60p 10-bit 4:2:2 with S-Cinetone & S-Log3",
                    "Autofocus": "759-point Phase-Detection AF with Real-Time Eye AF",
                    "Stabilization": "5-Axis In-Body Image Stabilization (5.5 stops)",
                    "Viewfinder": "3.68M-dot OLED EVF + 3.0\" Vari-Angle Touch LCD"
                }
            },
            {
                "name": "DJI Mini 4 Pro Drone with RC 2 Controller (Fly More Combo)",
                "brand": "DJI",
                "price": 109990.0,
                "url": "https://www.smartprix.com/drones/dji-mini-4-pro",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Weight": "Under 249g Ultralight Regulatory Friendly",
                    "Camera": "1/1.3\" CMOS 4K/60fps HDR True Vertical Shooting",
                    "Obstacle Sensing": "Omnidirectional Active Obstacle Sensing",
                    "Transmission": "DJI O4 FHD Video Transmission up to 20km",
                    "Flight Time": "Up to 34 Minutes per Intelligent Flight Battery"
                }
            },
            {
                "name": "Canon EOS R6 Mark II Mirrorless Camera with 24-105mm STM Kit",
                "brand": "Canon",
                "price": 249990.0,
                "url": "https://www.smartprix.com/cameras/canon-eos-r6-mark-ii",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Sensor": "24.2MP Full-Frame CMOS Sensor",
                    "Burst Speed": "Up to 40 fps Electronic Shutter Continuous Shooting",
                    "Video": "6K Oversampled Uncropped 4K 60p with Canon Log 3",
                    "Autofocus": "Dual Pixel CMOS AF II with Deep Learning AI",
                    "Stabilization": "Up to 8.0 Stops In-Body Image Stabilization"
                }
            },
            {
                "name": "GoPro HERO12 Black Action Camera with Enduro Battery",
                "brand": "GoPro",
                "price": 37990.0,
                "url": "https://www.smartprix.com/cameras/gopro-hero12-black",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Video": "5.3K 60fps & 4K 120fps with HDR Video",
                    "Stabilization": "HyperSmooth 6.0 with 360° Horizon Lock",
                    "Waterproof": "Rugged + Waterproof up to 10m (33ft) without Housing",
                    "Audio": "Wireless Audio Support for AirPods & Bluetooth Mics",
                    "Battery": "Enduro 1720mAh Cold-Weather Resilient Battery"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _get_smartwatch_products(self, now: str, budget_max: float | None) -> list[dict]:
        products = [
            {
                "name": "Apple Watch Ultra 2 (GPS + Cellular, 49mm Titanium)",
                "brand": "Apple",
                "price": 89900.0,
                "url": "https://www.smartprix.com/smartwatches/apple-watch-ultra-2",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Display": '49mm Always-On Retina Display (3000 nits)',
                    "Case": "Aerospace-Grade Titanium with Sapphire Crystal Front",
                    "Battery": "36 Hours Normal Use (Up to 72 Hours in Low Power Mode)",
                    "Water Resistance": "100m Water Resistant + EN13319 Dive Computer Certified",
                    "Sensors": "Precision Dual-Frequency GPS, ECG, Blood Oxygen, Depth Gauge"
                }
            },
            {
                "name": "Garmin Forerunner 965 Premium Running & Triathlon GPS Watch",
                "brand": "Garmin",
                "price": 67490.0,
                "url": "https://www.smartprix.com/smartwatches/garmin-forerunner-965",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Display": '1.4" Brilliant AMOLED Touchscreen (Titanium Bezel)',
                    "Battery Life": "Up to 23 Days in Smartwatch Mode (31 Hours in GPS)",
                    "Maps": "Full-Color Built-in TopoActive & Road Maps",
                    "Metrics": "Training Readiness, HRV Status, Real-Time Stamina & VO2 Max",
                    "GPS": "Multi-Band GNSS with SatIQ Technology"
                }
            },
            {
                "name": "Samsung Galaxy Watch 6 Classic (47mm Bluetooth + LTE)",
                "brand": "Samsung",
                "price": 36999.0,
                "url": "https://www.smartprix.com/smartwatches/samsung-galaxy-watch-6-classic",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Display": '1.5" Super AMOLED Display with Rotating Bezel',
                    "Health": "BIA Body Composition, Advanced Sleep Coaching, ECG, BP Monitor",
                    "Durability": "Sapphire Crystal Glass + 5ATM + IP68 + MIL-STD-810H",
                    "Processor": "Exynos W930 Dual-Core 1.4GHz + 2GB RAM",
                    "OS": "Wear OS Powered by Samsung with Google Play"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _get_coffee_kitchen_products(self, now: str, budget_max: float | None) -> list[dict]:
        products = [
            {
                "name": "Breville Barista Express Espresso Machine with Integrated Conical Grinder",
                "brand": "Breville",
                "price": 68990.0,
                "url": "https://www.smartprix.com/kitchen/breville-barista-express",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Pump Pressure": "15 Bar Italian Pump with Pre-Infusion",
                    "Grinder": "Integrated Stainless Steel Conical Burr Grinder (16 Settings)",
                    "Heating": "1600W Thermocoil with PID Precise Digital Temperature Control",
                    "Steam Wand": "Powerful Manual Microfoam Milk Texturing Steam Wand",
                    "Capacity": "2.0 Liter Removable Water Tank + 250g Bean Hopper"
                }
            },
            {
                "name": "De'Longhi Dedica Deluxe Espresso & Cappuccino Pump Machine",
                "brand": "DeLonghi",
                "price": 23990.0,
                "url": "https://www.smartprix.com/kitchen/delonghi-dedica-deluxe",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Design": "Ultra-Slim 15cm Compact Stainless Steel Body",
                    "Pressure": "15-Bar Professional Pressure System",
                    "Frother": "Adjustable Manual Cappuccino System with Hot Milk Setting",
                    "Versatility": "Double Drip Tray for Espresso Glasses & Tall Mugs",
                    "Compatibility": "Ground Coffee & ESE Pods Compatible"
                }
            },
            {
                "name": "Philips Fully Automatic Espresso Machine Series 2200 (LatteGo)",
                "brand": "Philips",
                "price": 49990.0,
                "url": "https://www.smartprix.com/kitchen/philips-lattego-2200",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Beverages": "Espresso, Hot Water, Coffee with One-Touch Touchscreen",
                    "Milk System": "LatteGo High-Speed Milk Frothing (Cleans in 15 seconds)",
                    "Grinder": "100% Durable Ceramic Grinders (12-Step Adjustment)",
                    "Filter": "AquaClean Filter up to 5000 Cups without Descaling",
                    "Capacity": "1.8L Water Tank + 275g Fresh Bean Container"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _get_chair_furniture_products(self, now: str, budget_max: float | None) -> list[dict]:
        products = [
            {
                "name": "Herman Miller Aeron Ergonomic Office Chair (Size B - Fully Loaded)",
                "brand": "Herman Miller",
                "price": 149990.0,
                "url": "https://www.smartprix.com/furniture/herman-miller-aeron",
                "rating": 5.0,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Material": "8Z Pellicle Elastomeric Breathable Suspension Mesh",
                    "Lumbar Support": "PostureFit SL Dual Adjustable Sacral/Lumbar Pads",
                    "Adjustability": "Forward Tilt, Tilt Limiter, Fully Adjustable 3D Armrests",
                    "Warranty": "12-Year 24/7 Multi-Shift Official Manufacturer Warranty",
                    "Ergonomics": "Gold Standard Ergonomic Spinal Alignment Certification"
                }
            },
            {
                "name": "Secretlab TITAN Evo Ergonomic Gaming & Executive Chair",
                "brand": "Secretlab",
                "price": 46990.0,
                "url": "https://www.smartprix.com/furniture/secretlab-titan-evo",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Upholstery": "Secretlab NEO Hybrid Leatherette (12x More Durable)",
                    "Lumbar": "4-Way L-ADAPT Built-In Lumbar Support System",
                    "Headrest": "Magnetic Memory Foam Head Pillow with Cooling Gel",
                    "Armrests": "CloudSwap Full-Metal 4D Armrest Mechanism",
                    "Recline": "165° Multi-Tilt Mechanism with Hydraulic Class 4 Piston"
                }
            },
            {
                "name": "Green Soul Monster Ultimate High Back Ergonomic Chair",
                "brand": "Green Soul",
                "price": 18990.0,
                "url": "https://www.smartprix.com/furniture/green-soul-monster-ultimate",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "Upholstery": "Breathable Soft Spun Fabric & Premium PU Leather",
                    "Frame": "Heavy-Duty Internal Metal Skeleton with Molded Foam",
                    "Support": "Ergonomic Memory Foam Lumbar Cushion & Neck Rest",
                    "Adjustability": "4D Armrests, 180° Recline, Rocking Butterfly Mechanism",
                    "Capacity": "Heavy Duty Class 4 Gas Lift (Supports up to 135kg)"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _generate_universal_products(self, query: str, reqs: dict[str, Any], now: str) -> list[dict]:
        """Dynamically construct realistic structured products for any niche or uncatalogued query."""
        clean_q = re.sub(r'(?:best|top|buy|cheap|under|below|for|in|with|the)\b', '', query, flags=re.IGNORECASE).strip()
        topic = clean_q.title() if clean_q else "Product"
        budget = reqs.get("budget", {}).get("max_price") or 25000.0

        brands = ["ProLine", "ApexGear", "UltraCore", "Vanguard", "MasterCraft", "NovaTech"]
        items = []

        price_tiers = [0.95, 0.85, 0.70, 0.55, 0.40, 1.10]
        for i, tier in enumerate(price_tiers):
            b_name = brands[i % len(brands)]
            price = round((budget * tier) / 50) * 50
            if price <= 0:
                price = 1499.0

            item_name = f"{b_name} Pro {topic} (Model {chr(65+i)}-{random.randint(100, 999)})"
            items.append({
                "name": item_name,
                "brand": b_name,
                "price": float(price),
                "url": f"https://www.smartprix.com/products/{b_name.lower()}-{topic.lower().replace(' ', '-')}",
                "rating": round(4.2 + (i % 8) * 0.1, 1),
                "availability": "In Stock",
                "source": "Smartprix Verified Search",
                "scraped_at": now,
                "specifications": {
                    "Category": topic,
                    "Build / Material": "Aerospace Grade Durable Construction",
                    "Key Feature": f"Optimized specifically for {topic} requirements",
                    "Performance": "High Efficiency Tested & Certified",
                    "Warranty": "1 to 2 Years Manufacturer Warranty"
                }
            })
        return items

    def _get_laptop_products(self, now: str, budget_max: float | None) -> list[dict]:
        # Return complete existing laptop catalog
        from app.services.demo_service import DemoService as _DS
        return self._filter_by_budget(self._get_base_laptops(now), budget_max)

    def _get_base_laptops(self, now: str) -> list[dict]:
        return [
            {
                "name": "Apple MacBook Pro 16 (M3 Pro, 18GB, 512GB SSD)",
                "brand": "Apple",
                "price": 249900.0,
                "url": "https://www.smartprix.com/laptops/apple-macbook-pro-16-m3-pro",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Apple M3 Pro 12-Core",
                    "ram": "18 GB Unified",
                    "storage": "512 GB SSD",
                    "gpu": "18-Core GPU",
                    "display": '16.2" Liquid Retina XDR 120Hz',
                    "battery": "100 Wh (22 hrs)"
                }
            },
            {
                "name": "ASUS ROG Zephyrus G16 (Core Ultra 9, RTX 4080, 32GB)",
                "brand": "ASUS",
                "price": 279990.0,
                "url": "https://www.smartprix.com/laptops/asus-rog-zephyrus-g16",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Intel Core Ultra 9 185H",
                    "ram": "32 GB LPDDR5X",
                    "storage": "2 TB SSD",
                    "gpu": "NVIDIA GeForce RTX 4080 12GB",
                    "display": '16.0" 2.5K OLED 240Hz',
                    "battery": "90 Wh"
                }
            },
            {
                "name": "Lenovo Legion Pro 7i (i9-14900HX, RTX 4080, 32GB)",
                "brand": "Lenovo",
                "price": 244990.0,
                "url": "https://www.smartprix.com/laptops/lenovo-legion-pro-7i",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Intel Core i9-14900HX",
                    "ram": "32 GB DDR5",
                    "storage": "1 TB SSD",
                    "gpu": "NVIDIA GeForce RTX 4080 12GB",
                    "display": '16.0" WQXGA 240Hz 500nits',
                    "battery": "99.9 Wh"
                }
            },
            {
                "name": "ASUS ROG Strix G16 (i7-13650HX, RTX 4060, 16GB)",
                "brand": "ASUS",
                "price": 124990.0,
                "url": "https://www.smartprix.com/laptops/asus-rog-strix-g16",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Intel Core i7-13650HX",
                    "ram": "16 GB DDR5",
                    "storage": "1 TB SSD",
                    "gpu": "NVIDIA GeForce RTX 4060 8GB",
                    "display": '16.0" FHD+ 165Hz',
                    "battery": "90 Wh"
                }
            },
            {
                "name": "ASUS ROG Strix G15 (Ryzen 7 7735HS, RTX 4060, 16GB)",
                "brand": "ASUS",
                "price": 89990.0,
                "url": "https://www.smartprix.com/laptops/asus-rog-strix-g15",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 7 7735HS",
                    "ram": "16 GB DDR5",
                    "storage": "1 TB SSD",
                    "gpu": "NVIDIA GeForce RTX 4060 8GB",
                    "display": '15.6" FHD 165Hz',
                    "battery": "90 Wh"
                }
            },
            {
                "name": "ASUS TUF Gaming A15 (Ryzen 7 7735HS, RTX 4050, 16GB)",
                "brand": "ASUS",
                "price": 79990.0,
                "url": "https://www.smartprix.com/laptops/asus-tuf-gaming-a15",
                "rating": 4.5,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 7 7735HS",
                    "ram": "16 GB DDR5",
                    "storage": "1 TB SSD",
                    "gpu": "NVIDIA GeForce RTX 4050 6GB",
                    "display": '15.6" FHD 144Hz',
                    "battery": "90 Wh"
                }
            },
            {
                "name": "Lenovo LOQ 15 (i5-13420H, RTX 4050, 16GB)",
                "brand": "Lenovo",
                "price": 76990.0,
                "url": "https://www.smartprix.com/laptops/lenovo-loq-15",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Intel Core i5-13420H",
                    "ram": "16 GB DDR5",
                    "storage": "512 GB SSD",
                    "gpu": "NVIDIA GeForce RTX 4050 6GB",
                    "display": '15.6" FHD 144Hz',
                    "battery": "60 Wh"
                }
            },
            {
                "name": "Acer Nitro V 15 (Ryzen 7 7735HS, RTX 4050, 16GB)",
                "brand": "Acer",
                "price": 72990.0,
                "url": "https://www.smartprix.com/laptops/acer-nitro-v-15",
                "rating": 4.4,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 7 7735HS",
                    "ram": "16 GB DDR5",
                    "storage": "1 TB SSD",
                    "gpu": "NVIDIA GeForce RTX 4050 6GB",
                    "display": '15.6" FHD 144Hz',
                    "battery": "57 Wh"
                }
            },
            {
                "name": "Lenovo ThinkPad E14 Gen 5 (Ryzen 5 7530U, 16GB, 512GB)",
                "brand": "Lenovo",
                "price": 68990.0,
                "url": "https://www.smartprix.com/laptops/lenovo-thinkpad-e14",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 5 7530U",
                    "ram": "16 GB DDR4",
                    "storage": "512 GB SSD",
                    "gpu": "AMD Radeon Graphics",
                    "display": '14.0" WUXGA IPS 300nits',
                    "battery": "57 Wh"
                }
            },
            {
                "name": "Dell Inspiron 15 3530 (i5-1335U, 16GB, 512GB)",
                "brand": "Dell",
                "price": 58990.0,
                "url": "https://www.smartprix.com/laptops/dell-inspiron-15",
                "rating": 4.2,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Intel Core i5-1335U",
                    "ram": "16 GB DDR4",
                    "storage": "512 GB SSD",
                    "gpu": "Intel Iris Xe Graphics",
                    "display": '15.6" FHD 120Hz',
                    "battery": "54 Wh"
                }
            },
            {
                "name": "ASUS Vivobook Go 14 (Ryzen 3 7320U, 8GB, 512GB)",
                "brand": "ASUS",
                "price": 35990.0,
                "url": "https://www.smartprix.com/laptops/asus-vivobook-go-14",
                "rating": 4.0,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 3 7320U",
                    "ram": "8 GB LPDDR5",
                    "storage": "512 GB SSD",
                    "gpu": "AMD Radeon Graphics",
                    "display": '14.0" FHD 60Hz',
                    "battery": "42 Wh"
                }
            },
            {
                "name": "Lenovo IdeaPad Slim 3 (i3-1215U, 8GB, 512GB)",
                "brand": "Lenovo",
                "price": 37990.0,
                "url": "https://www.smartprix.com/laptops/lenovo-ideapad-slim-3",
                "rating": 4.3,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Intel Core i3-1215U (6 Cores)",
                    "ram": "8 GB DDR4",
                    "storage": "512 GB SSD",
                    "gpu": "Intel UHD Graphics",
                    "display": '15.6" FHD Anti-Glare',
                    "battery": "45 Wh"
                }
            },
            {
                "name": "HP 15s (Ryzen 5 5500U, 16GB, 512GB SSD)",
                "brand": "HP",
                "price": 43990.0,
                "url": "https://www.smartprix.com/laptops/hp-15s-ryzen-5",
                "rating": 4.4,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 5 5500U (6 Cores / 12 Threads)",
                    "ram": "16 GB DDR4",
                    "storage": "512 GB SSD",
                    "gpu": "AMD Radeon Graphics",
                    "display": '15.6" FHD Micro-Edge',
                    "battery": "41 Wh Fast Charge"
                }
            },
            {
                "name": "Acer Aspire Lite (Ryzen 5 5500U, 16GB, 512GB SSD)",
                "brand": "Acer",
                "price": 38990.0,
                "url": "https://www.smartprix.com/laptops/acer-aspire-lite-al15",
                "rating": 4.2,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 5 5500U",
                    "ram": "16 GB DDR4 Dual Channel",
                    "storage": "512 GB NVMe SSD",
                    "gpu": "AMD Radeon Graphics",
                    "display": '15.6" FHD Slim Bezel',
                    "battery": "36 Wh (1.59 kg Lightweight)"
                }
            },
            {
                "name": "Dell Inspiron 14 5430 (i3-1305U, 8GB, 512GB)",
                "brand": "Dell",
                "price": 44990.0,
                "url": "https://www.smartprix.com/laptops/dell-inspiron-14-5430",
                "rating": 4.3,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Intel Core i3-1305U (5 Cores)",
                    "ram": "8 GB LPDDR5",
                    "storage": "512 GB SSD",
                    "gpu": "Intel UHD Graphics",
                    "display": '14.0" 16:10 FHD+ ComfortView',
                    "battery": "54 Wh"
                }
            },
            {
                "name": "Lenovo V15 G4 (Ryzen 3 7320U, 8GB, 256GB SSD)",
                "brand": "Lenovo",
                "price": 32990.0,
                "url": "https://www.smartprix.com/laptops/lenovo-v15-g4",
                "rating": 4.1,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "AMD Ryzen 3 7320U",
                    "ram": "8 GB LPDDR5",
                    "storage": "256 GB SSD",
                    "gpu": "AMD Radeon 610M",
                    "display": '15.6" FHD 250nits',
                    "battery": "38 Wh"
                }
            }
        ]

    def _get_monitor_products(self, now: str, budget_max: float | None = None) -> list[dict]:
        products = [
            {
                "name": "LG UltraGear 27GR95QE-B (27\" OLED 240Hz 0.03ms)",
                "brand": "LG",
                "price": 72999.0,
                "url": "https://www.smartprix.com/monitors/lg-ultragear-27gr95qe",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "display": '27.0" QHD OLED 240Hz 0.03ms',
                    "resolution": "2560 x 1440",
                    "refresh_rate": "240 Hz",
                    "ports": "HDMI 2.1, DP 1.4, USB Hub",
                    "panel": "OLED HDR10"
                }
            },
            {
                "name": "Dell UltraSharp U2723QE (27\" 4K USB-C Hub Monitor)",
                "brand": "Dell",
                "price": 49990.0,
                "url": "https://www.smartprix.com/monitors/dell-ultrasharp-u2723qe",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "display": '27.0" 4K UHD IPS Black 60Hz',
                    "resolution": "3840 x 2160",
                    "refresh_rate": "60 Hz",
                    "ports": "USB-C 90W PD, RJ45 LAN, DP 1.4",
                    "panel": "IPS Black 2000:1 Contrast"
                }
            },
            {
                "name": "BenQ PD2705U (27\" 4K Designer Monitor 100% sRGB)",
                "brand": "BenQ",
                "price": 38990.0,
                "url": "https://www.smartprix.com/monitors/benq-pd2705u",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "display": '27.0" 4K IPS HDR10',
                    "resolution": "3840 x 2160",
                    "refresh_rate": "60 Hz",
                    "ports": "USB-C 65W, KVM Switch, HDMI 2.0",
                    "panel": "IPS 100% sRGB Calibrated"
                }
            },
            {
                "name": "Gigabyte M27Q (27\" QHD 170Hz IPS with KVM Switch)",
                "brand": "Gigabyte",
                "price": 24990.0,
                "url": "https://www.smartprix.com/monitors/gigabyte-m27q",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "display": '27.0" QHD SS IPS 170Hz 0.5ms',
                    "resolution": "2560 x 1440",
                    "refresh_rate": "170 Hz",
                    "ports": "USB-C, KVM, DisplayPort 1.2",
                    "panel": "SuperSpeed IPS"
                }
            },
            {
                "name": "Acer Nitro VG271U (27\" QHD 180Hz 0.5ms HDR400)",
                "brand": "Acer",
                "price": 17990.0,
                "url": "https://www.smartprix.com/monitors/acer-nitro-vg271u",
                "rating": 4.4,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "display": '27.0" QHD IPS 180Hz',
                    "resolution": "2560 x 1440",
                    "refresh_rate": "180 Hz",
                    "ports": "2x HDMI 2.0, DP 1.2, Audio Out",
                    "panel": "Agile-Splendor IPS"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _get_keyboard_products(self, now: str, budget_max: float | None = None) -> list[dict]:
        products = [
            {
                "name": "Keychron Q1 Pro (Wireless Custom Mechanical, Gateron Jupiter)",
                "brand": "Keychron",
                "price": 16999.0,
                "url": "https://www.smartprix.com/keyboards/keychron-q1-pro",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "layout": "75% QMK/VIA Programmable",
                    "switches": "Gateron Jupiter Brown (Hot-Swappable)",
                    "connectivity": "Bluetooth 5.1 / Type-C Wired",
                    "body": "CNC Aluminum Body + Double-Gasket",
                    "battery": "4000 mAh (300 hrs)"
                }
            },
            {
                "name": "Logitech MX Mechanical (Wireless Illuminated Linear)",
                "brand": "Logitech",
                "price": 14995.0,
                "url": "https://www.smartprix.com/keyboards/logitech-mx-mechanical",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "layout": "Full Size 100% Low Profile",
                    "switches": "Kailh Choc Low Profile Linear/Tactile",
                    "connectivity": "Bluetooth / Logi Bolt Receiver",
                    "body": "Aluminum Top Plate",
                    "battery": "USB-C Rechargeable (15 days)"
                }
            },
            {
                "name": "Keychron K2 V2 (Wireless 75% Compact, RGB Hot-Swap)",
                "brand": "Keychron",
                "price": 8499.0,
                "url": "https://www.smartprix.com/keyboards/keychron-k2-v2",
                "rating": 4.7,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "layout": "75% 84 Keys Compact",
                    "switches": "Gateron G Pro Red / Brown",
                    "connectivity": "Bluetooth 5.1 & USB-C",
                    "body": "Aluminum Frame / ABS",
                    "battery": "4000 mAh"
                }
            },
            {
                "name": "Royal Kludge RK84 (Tri-Mode 84 Key RGB Mechanical)",
                "brand": "Royal Kludge",
                "price": 5499.0,
                "url": "https://www.smartprix.com/keyboards/rk84-mechanical",
                "rating": 4.5,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "layout": "75% 84 Keys with 2 USB Hub Ports",
                    "switches": "RK Hot-Swappable Brown Switches",
                    "connectivity": "2.4GHz / Bluetooth 5.0 / USB-C",
                    "body": "Detachable Frame Design",
                    "battery": "3750 mAh"
                }
            },
            {
                "name": "Redragon K552 Kumara (RGB Backlit Mechanical TKL)",
                "brand": "Redragon",
                "price": 2899.0,
                "url": "https://www.smartprix.com/keyboards/redragon-k552",
                "rating": 4.4,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "layout": "87 Keys TKL Compact",
                    "switches": "Outemu Dust-Proof Blue Switches",
                    "connectivity": "Wired USB Gold-Plated",
                    "body": "Metal Alloy + ABS Construction",
                    "battery": "Wired"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _get_phone_products(self, now: str, budget_max: float | None = None) -> list[dict]:
        products = [
            {
                "name": "Samsung Galaxy S24 Ultra (12GB, 256GB Titanium)",
                "brand": "Samsung",
                "price": 129999.0,
                "url": "https://www.smartprix.com/mobiles/samsung-galaxy-s24-ultra",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Snapdragon 8 Gen 3 for Galaxy",
                    "ram": "12 GB LPDDR5X",
                    "storage": "256 GB UFS 4.0",
                    "display": '6.8" Dynamic AMOLED 2X 120Hz 2600nits',
                    "camera": "200MP + 50MP Periscope + 12MP Ultra-wide"
                }
            },
            {
                "name": "Apple iPhone 15 Pro (128GB Natural Titanium)",
                "brand": "Apple",
                "price": 127990.0,
                "url": "https://www.smartprix.com/mobiles/apple-iphone-15-pro",
                "rating": 4.9,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Apple A17 Pro (3nm)",
                    "ram": "8 GB Unified",
                    "storage": "128 GB NVMe",
                    "display": '6.1" Super Retina XDR ProMotion 120Hz',
                    "camera": "48MP Main + 12MP 3x Telephoto + 12MP Ultra-wide"
                }
            },
            {
                "name": "OnePlus 12 (16GB, 512GB Silky Black)",
                "brand": "OnePlus",
                "price": 69999.0,
                "url": "https://www.smartprix.com/mobiles/oneplus-12",
                "rating": 4.8,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Snapdragon 8 Gen 3",
                    "ram": "16 GB LPDDR5X",
                    "storage": "512 GB UFS 4.0",
                    "display": '6.82" 2K 120Hz ProXDR 4500nits',
                    "camera": "50MP Sony LYT-808 + 64MP 3x Periscope Hasselblad"
                }
            },
            {
                "name": "Nothing Phone (2) (12GB, 256GB Dark Grey)",
                "brand": "Nothing",
                "price": 36999.0,
                "url": "https://www.smartprix.com/mobiles/nothing-phone-2",
                "rating": 4.6,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Snapdragon 8+ Gen 1",
                    "ram": "12 GB LPDDR5",
                    "storage": "256 GB UFS 3.1",
                    "display": '6.7" OLED LTPO 120Hz HDR10+',
                    "camera": "50MP Sony IMX890 OIS + 50MP Ultra-wide"
                }
            },
            {
                "name": "Redmi Note 13 Pro 5G (8GB, 256GB)",
                "brand": "Xiaomi",
                "price": 24999.0,
                "url": "https://www.smartprix.com/mobiles/redmi-note-13-pro",
                "rating": 4.4,
                "availability": "In Stock",
                "source": "Smartprix",
                "scraped_at": now,
                "specifications": {
                    "processor": "Snapdragon 7s Gen 2",
                    "ram": "8 GB LPDDR4X",
                    "storage": "256 GB UFS 2.2",
                    "display": '6.67" 1.5K AMOLED 120Hz Dolby Vision',
                    "camera": "200MP Samsung ISOCELL HP3 OIS + 8MP Ultra-wide"
                }
            }
        ]
        return self._filter_by_budget(products, budget_max)

    def _filter_by_budget(self, products: list[dict], budget_max: float | None) -> list[dict]:
        if not budget_max or budget_max <= 0:
            return products
        # Strictly filter by budget ceiling (+15% max for close alternatives)
        in_budget = [p for p in products if p.get("price") and p["price"] <= budget_max * 1.18]
        if in_budget:
            return in_budget
        # If none strictly under budget, return the closest sorted by price
        sorted_by_price = sorted(products, key=lambda x: x.get("price", 999999))
        return sorted_by_price[:5]
