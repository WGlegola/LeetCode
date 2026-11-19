class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.usage = []

    def get(self, key: int) -> int:
        if key in self.store:
            self.usage.remove(key)
            self.usage.insert(0, key)
            return self.store[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            self.usage.remove(key)
            self.usage.insert(0, key)
        else:
            if len(self.usage) == self.cap:
                self.usage.insert(0, key)
                self.store.pop(self.usage.pop())
                self.store[key] = value
            else:
                self.usage.insert(0, key)
                self.store[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
