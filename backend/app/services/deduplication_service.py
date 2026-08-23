class DeduplicationService:
    def deduplicate(self, products: list[dict]) -> list[dict]:
        seen_urls = set()
        seen_hashes = set()
        unique = []
        
        for p in products:
            url = p.get('url')
            if url:
                if url in seen_urls: continue
                seen_urls.add(url)
                
            chash = p.get('content_hash')
            if chash:
                if chash in seen_hashes: continue
                seen_hashes.add(chash)
                
            unique.append(p)
            
        return unique
