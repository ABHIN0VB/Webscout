import httpx
import asyncio
import logging
from datetime import datetime, timezone
from app.config import get_settings

logger = logging.getLogger(__name__)

class BrightDataService:
    BASE_URL = "https://api.brightdata.com"
    
    def __init__(self):
        self.settings = get_settings()
        self.headers = {
            "Authorization": f"Bearer {self.settings.BRIGHTDATA_API_TOKEN}",
            "Content-Type": "application/json"
        }
    
    async def trigger_collector(self, collector_id: str, target_url: str) -> str:
        url = f"{self.BASE_URL}/dca/trigger?collector={collector_id}"
        payload = [{"url": target_url}]
        
        for attempt in range(3):
            try:
                async with httpx.AsyncClient() as client:
                    resp = await client.post(url, json=payload, headers=self.headers, timeout=30.0)
                    resp.raise_for_status()
                    data = resp.json()
                    return data.get("snapshot_id")
            except Exception as e:
                logger.error(f"Attempt {attempt+1} failed to trigger collector: {e}")
                if attempt == 2:
                    raise
                await asyncio.sleep(2 ** attempt)
        return ""
    
    async def get_results(self, snapshot_id: str, timeout: int = 300) -> list[dict]:
        url = f"{self.BASE_URL}/dca/dataset?id={snapshot_id}"
        start_time = datetime.now(timezone.utc)
        
        while (datetime.now(timezone.utc) - start_time).total_seconds() < timeout:
            try:
                async with httpx.AsyncClient() as client:
                    resp = await client.get(url, headers=self.headers, timeout=30.0)
                    if resp.status_code == 200:
                        return resp.json()
            except Exception as e:
                logger.error(f"Error polling dataset: {e}")
            await asyncio.sleep(10)
        
        raise TimeoutError("Polling collector results timed out")
    
    async def get_collector_status(self, collector_id: str) -> dict:
        url = f"{self.BASE_URL}/dca/collector/{collector_id}"
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(url, headers=self.headers, timeout=10.0)
                if resp.status_code == 200:
                    return resp.json()
        except Exception:
            pass
        return {"status": "unknown"}
    
    async def run_collector(self, collector_id: str = None, target_url: str = None) -> list[dict]:
        cid = collector_id or self.settings.BRIGHTDATA_COLLECTOR_ID
        url = target_url or self.settings.BRIGHTDATA_TARGET_URL
        if not cid:
            return []
            
        snapshot_id = await self.trigger_collector(cid, url)
        if not snapshot_id:
            raise Exception("Failed to get snapshot_id")
            
        return await self.get_results(snapshot_id)
