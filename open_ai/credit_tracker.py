# Run with python test.py

# Design a system that tracks user token credits and can efficiently query 
# the number of tokens a user has at any given timestamp. The service should 
# handle credit additions, deductions, and historical balance lookups.



import heapq
class CreditTracker:
    """
    Incremental / online. Assumes operation timestamps are non-decreasing.
    Each credit is pushed and popped from the heap exactly once, so every
    operation is amortized O(log N).
    """
    def __init__(self) -> None:
        self._heap = []   # [expiresAt, remaining], min-heap by soonest expiry
        self._live = 0    # total non-expired, unspent credits
        self._now = 0     # latest timestamp processed
    
    def _advance(self, timestamp: int) -> None:
        if timestamp < self._now:
            raise ValueError("Timestamps must be non-decreasing")
        
        self._now = timestamp

        while self._heap and self._heap[0][0] <= timestamp:   # expire
            self._live -= heapq.heappop(self._heap)[1]
    
    def createCredit(self, id: str, amount: int, timestamp: int, expiresAt: int) -> None:
        if amount <= 0 or expiresAt <= timestamp:
            raise ValueError("Invalid input")
        
        self._advance(timestamp)
        heapq.heappush(self._heap, [expiresAt, amount])
        self._live += amount
    
    def subtract(self, amount: int, timestamp: int) -> None:
        if amount <= 0:
            raise ValueError("Invalid input")
        
        self._advance(timestamp)

        if amount > self._live:
            raise ValueError("Insufficient funds")
        
        self._live -= amount

        while amount > 0:                        # spend soonest-expiring first
            top = self._heap[0]
            take = min(top[1], amount)
            top[1] -= take
            amount -= take
            if top[1] == 0:
                heapq.heappop(self._heap)
    
    def getBalance(self, timestamp: int) -> int:
        self._advance(timestamp)
        return self._live








CREATE, SUBTRACT = 0, 1

class CreditTrackerInterview:
    def __init__(self) -> None:
        # (timestamp, EVENT_TYPE, data)
        self.events = []

    def createCredit(self, id: str, amount: int, timestamp: int, expiresAt: int) -> None:
        if amount <= 0:
            raise ValueError("Invalid input")
        
        self.events.append((timestamp, CREATE, (id, amount, expiresAt)))

        return True
        
    def subtract(self, amount: int, timestamp: int) -> None:
        if amount <= 0:
            raise ValueError("Invalid input")
        
        self.events.append((timestamp, SUBTRACT, amount))

        return True
        
    def getBalance(self, timestamp: int) -> int:
        events = sorted(self.events, key=lambda x: (x[0], x[1]))

        tokens_created = {}

        for event_timestamp, event_type, obj in events:
            # 1. Sort events by when they happened
            # 2. Loop through everything that happened before the timestamp
            # 3. Add the created credits to tokens_created (mapped by id)
            # 4. If it is a subtraction do the following:
            #       a. filter out the ones that expire before this subtraction
            #       b. sort all the remaining tokens_created by the expiration
            #       c. spend the soonest-expiring, non-expired credits first
            # 5. Sum up all the tokens_created remaining that dont expire before timestamp
            if timestamp < event_timestamp:
                break

            if event_type == CREATE:
                id, amount, expires_at = obj
                tokens_created[id] = [expires_at, amount]
            else:
                amount_to_subtract = obj

                records_able_to_spend = []
                # spend soonest-expiring, non-expired credits first
                for id, (expires_at, amount) in tokens_created.items():
                    if event_timestamp < expires_at:
                        records_able_to_spend.append([expires_at, amount, id])

                records_able_to_spend.sort(key=lambda x: x[0])

                for expires_at, amount, id in records_able_to_spend:
                    if amount_to_subtract == 0:
                        break

                    if amount > amount_to_subtract:
                        amount -= amount_to_subtract
                        tokens_created[id][1] = amount
                        amount_to_subtract = 0
                    else:
                        tokens_created[id][1] = 0
                        amount_to_subtract -= amount
                
                if amount_to_subtract > 0:
                    raise ValueError("Insufficient Funds")
        
        total = 0
        for id, (expires_at, amount) in tokens_created.items():
            if timestamp < expires_at:
                total += amount
        
        return total


if __name__ == "__main__":
    ct = CreditTrackerInterview()
    ct.createCredit("1", 3, 3, 6)
    ct.createCredit("2", 2, 2, 6)
    ct.createCredit("3", 1, 1, 6)

    assert ct.getBalance(5) == 6

    ct.subtract(2, 5)

    assert ct.getBalance(5) == 4
