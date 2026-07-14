import asyncio
from collections import deque, defaultdict

# Assuming the requests all come in order
class RateLimiter:
    def __init__(self, requests, ms):
        self.requests = requests
        self.ms = ms
        self.locks = defaultdict(asyncio.Lock)
        self.history = defaultdict(deque)
    
    def _cleanup(self, userId, timestamp):
        history = self.history[userId]
        while history and history[0] <= timestamp - self.ms:
            history.popleft()

    async def allow_request(self, userId: str, timestamp: int):
        lock = self.locks[userId]

        async with lock:
            self._cleanup(userId, timestamp)

            if len(self.history[userId]) >= self.requests:
                return False
            
            self.history[userId].append(timestamp)

            return True

