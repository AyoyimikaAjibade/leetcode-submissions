class LRUCache:

    def __init__(self, capacity: int):
        self.lru_map = {}
        self.cache_map =  {}
        self.capacity = capacity
        self.tick = 0

    def _touch(self, key):
        self.tick += 1
        self.lru_map[key] = self.tick

    def get(self, key: int) -> int:
        if self.cache_map.get(key):
            self._touch(key)
            return self.cache_map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map[key] = value
            self._touch(key)
            return

        if len(self.cache_map) >= self.capacity:
            lru_key = min(self.lru_map, key=self.lru_map.get)
            del self.cache_map[lru_key]
            del self.lru_map[lru_key]

        self.cache_map[key] = value
        self._touch(key)
            
        
