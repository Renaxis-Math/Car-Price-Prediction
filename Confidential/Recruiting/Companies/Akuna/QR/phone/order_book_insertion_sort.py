import bisect

class OrderBook:
    def __init__(self):
        self.store = []  # resize-able container

    def addNum(self, num: int) -> None:
        left, right = 0, len(self.store)
        while left < right:
            mid = (left + right) // 2
            if self.store[mid] < num:
                left = mid + 1
            else:
                right = mid

        self.store.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.store)
        return self.store[n // 2] if n & 1 else \
        (self.store[n // 2 - 1] + self.store[n // 2]) * 0.5