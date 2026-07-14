# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            time, value = values[mid]

            if time <= timestamp:
                # This could be our answer
                result = value

                # But there might be a newer timestamp
                left = mid + 1
            else:
                # Timestamp too large
                right = mid - 1

        return result