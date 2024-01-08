class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        H = self.get_hash(key)
        self.arr[H] = value

    def __getitem__(self, key):
        H = self.get_hash(key)
        return self.arr[H]

    def __delitem__(self, key):
        H = self.get_hash(key)
        self.arr[H] = None


H = HashTable()
H["Rahul"] = 1
H["Bahul"] = 10
H["Sahul"] = 19
H["Zahul"] = 18
H["Yahul"] = 17

print(H["Sahul"])
del H["Bahul"]
print(H.arr)

