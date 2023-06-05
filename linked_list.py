class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n 


    def insert_head(self,value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

        self.n = self.n + 1 


    def __str__(self):
        curr = self.head

        result = ''

        while curr != None:
            result = result + str(curr.data) + ' -> '
            curr = curr.next 

        return result[:-3]


    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.n = self.n + 1

    
    def insert_after(self,after,value):
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return "Item Not Found"


    def clear(self):
        self.head = None
        self.n = 0


    def delete_head(self):
        if self.head == None:
            return "Empty LL"

        self.head = self.head.next
        self.n = self.n - 1
    
    def pop(self):
        
        if self.head == None:
            return "Empty LL"

        curr = self.head

        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n = self.n - 1


    def remove(self,value):
        
        if self.head == None:
            return "Empty LL"

        if self.head.data == value:
            return self.delete_head()

        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            return "Item Not Found"
        else:
            curr.next = curr.next.next 


    def search(self,item):

        curr = self.head 
        pos = 0

        while curr != None:
            if curr.data == item:
                return pos 
            curr = curr.next
            pos = pos + 1

        return "Item not found"



    def __getitem__(self,index):

        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return "Index not found"


L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(L)
# L.clear()
# L.delete_head()
# L.insert_after(3, 300)
# L.insert_after(1, 200)
# L.append(5)
# L.pop()
# L.remove(2)
# print(L.search(3))
print(L[5])
# print(L)






















# a =Node(1)
# b =Node(2)
# c =Node(3)

# a.next = b
# b.next = c
 
# print(a.next)

# print(int(0x0000019B5D6E1160))