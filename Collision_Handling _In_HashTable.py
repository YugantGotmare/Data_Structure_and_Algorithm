# Collision_Handling_In_HashTable

class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                del self.arr[arr_index][index]

# t = HashTable()
# t["march 6"] = 310
# t["march 7"] = 420
# t["march 8"] = 67
# t["march 17"] = 63457

# print(t["march 6"])
# print(t.arr)

# t["march 6"] = 11

# print(t.arr)
# print(t["march 6"])

# del t["march 6"]
# print(t["march 6"])






##################### Practise Questions ######################

arr = []

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Infnore the row")

print(arr)

# What was the average temperature in first week of Jan
print(sum(arr[0:7])/len(arr[0:7]))

# What was the maximum temperature in first 10 days of Jan
print(max(arr[0:10]))

# What was the temperature on Jan 9?
print(arr[8])

# What was the temperature on Jan 4?
print(arr[3])

