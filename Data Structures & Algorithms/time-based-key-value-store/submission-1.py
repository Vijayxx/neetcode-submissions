class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key,[]).append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        t = self.store[key]
        l = 0
        r = len(t) - 1
        res = ""
        while l <= r:
            m = (l+r)//2

            if t[m][1] <= timestamp:
                res = t[m][0]
                l = m + 1
            elif t[m][1] > timestamp:
                r = m - 1
        return res
        
