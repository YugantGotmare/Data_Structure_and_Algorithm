import ctypes

class MeraList():
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)


    def __len__(self):
        return self.n


    def append(self, item):
        if self.n == self.size:
            # RESIZE
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n += 1


    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B


    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','

        return '[' + result[:-1] + ']'


    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "IndexError - Index out of index"


    def pop(self):
        if self.n ==0:
            return 'Empty List'

        print(self.A[self.n-1])
        self.n = self.n - 1



    def clear(self):
        self.n = 0
        self.size = 1


    def __make_array(self, capacity):
        # creates a C type array with size capacity
        return (ctypes.py_object * capacity)()


    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i 

        return 'ValueError - not in list'


    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1


    def __delitem__(self,pos):
        if 0<= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n-1


    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    def find_max(self):
        if self.n == 0:
            return None
        max_value = self.A[0]
        for i in range(1, self.n):
            if self.A[i] > max_value:
                max_value = self.A[i]
        return max_value


    def find_min(self):
        if self.n == 0:
            return None
        min_value = self.A[0]
        for i in range(1, self.n):
            if self.A[i] < min_value:
                min_value = self.A[i]
        return min_value



    def sum_value(self):
        if self.n == 0:
            return None
        total_sum = 0
        for i in range(self.n):
            total_sum += self.A[i]
        return total_sum

    
    def sort(self):
        for i in range(self.n - 1):
            for j in range(0, self.n - i - 1):
                if self.A[j] > self.A[j + 1]:
                    self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]
   



L = MeraList()

L.append(10)
L.append(23)
L.append(3)
L.append(5)

print(L)



# L.sort()
# print(L)
# print(L.sum_value())
# print(L.find_max())
# print(L.find_min())
# print(L)


# print(L.pop())
# del L[1]
# print(L)
# print(L.find(200))

# print(L.clear())
# print(L[22])
# print(L.pop())

# print(L)


