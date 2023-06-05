#         1 -> 2 -> 3 -> 4 -> 5 -> None
#         H                   T 

# output: 

#       None <- 1 <- 2 <- 3 <- 4 <- 5
#               T                   H


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


    def reverse(self):
        prev_node = None
        curr_node = self.head

        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node


L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(L)

L.reverse()
print(L)




    