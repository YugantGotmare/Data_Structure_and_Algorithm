class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(100)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

H = HashTable()
H["Rahul"] = 1
H["Bahul"] = 10
H["Sahul"] = 19
H["Zahul"] = 18
H["Yahul"] = 17
H["Gahul"] = 20

print(H["Gahul"])
# del H["Bahul"]
print(H.arr)

