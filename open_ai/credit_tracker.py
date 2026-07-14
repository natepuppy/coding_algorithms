# Run with python test.py

# Design a system that tracks user token credits and can efficiently query 
# the number of tokens a user has at any given timestamp. The service should 
# handle credit additions, deductions, and historical balance lookups.

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
            # 1. Grab all credits and subtractions that happend before the timestamp
            # 2. Add the created credits to tokens_created (mapped by id)
            # 3. If it is a subtraction do the following:
            #       a. filter out the ones that expire before this subtraction
            #       b. sort all the remaining tokens_created by the expiration
            #       c. spend the soonest-expiring, non-expired credits first
            # 4. Sum up all the tokens_created remaining that dont expire before timestamp
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
