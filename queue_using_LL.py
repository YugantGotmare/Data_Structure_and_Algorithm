class Node:

    def __init__(self,value):
        self.data = value 
        self.next = None 


class Queue:

    def __init__(self):
        self.front = None 
        self.rear = None 

    def enqueue(self,value):

        new_node = Node(value)

        if self.front == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):

        if self.front == None:
            return "Queue empty"
        else:
            self.front = self.front.next


    def is_empty(self):
        return self.front == None

    def size(self):

        temp = self.front
        counter = 0

        while temp is not None:
            counter += 1
            temp = temp.next

        return counter

    def front_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.front.data

    def rear_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.rear.data


    def traverse(self):

        temp = self.front

        while temp is not None:
            print(temp.data,end=' ')
            temp = temp.next 


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.traverse())
# q.dequeue()
# print(q.traverse())
# print(q.traverse())
# q.dequeue()
# print(q.traverse())
print(q.is_empty())
print(q.front_item())
print(q.rear_item())