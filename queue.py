from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer)==0:
            print("empty Queue")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.size())
print(pq.dequeue())
print(pq.dequeue())


#################  Queue Practise 1 ########################

# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

# Pass following list as an argument to place order thread,

# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders.


# import threading
# import time

# from collections import deque

# class Queue:
#     def __init__(self):
#         self.buffer = deque()

#     def enqueue(self, val):
#         self.buffer.appendleft(val)

#     def dequeue(self):
#         if len(self.buffer)==0:
#             print("Queue is empty")
#             return

#         return self.buffer.pop()

#     def is_empty(self):
#         return len(self.buffer) == 0

#     def size(self):
#         return len(self.buffer)

# food_order_queue = Queue()

# def place_orders(orders):
#     for order in orders:
#         print("Placing order for:",order)
#         food_order_queue.enqueue(order)
#         time.sleep(0.5)

# def serve_orders():
#     time.sleep(1)
#     while True:
#         order = food_order_queue.dequeue()
#         print("Now serving: ",order)
#         time.sleep(2)

# if __name__ == '__main__':
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     t1 = threading.Thread(target=place_orders, args=(orders,))
#     t2 = threading.Thread(target=serve_orders)

#     t1.start()
#     t2.start()



#################  Queue Practise 2 ########################

# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

# You also need to add front() function in queue class that can return the front element in the queue.

# from collections import deque

# class Queue:
#     def __init__(self):
#         self.buffer = deque()

#     def enqueue(self, val):
#         self.buffer.appendleft(val)

#     def dequeue(self):
#         if len(self.buffer)==0:
#             print("Queue is empty")
#             return

#         return self.buffer.pop()

#     def is_empty(self):
#         return len(self.buffer) == 0

#     def size(self):
#         return len(self.buffer)

#     def fornt(self):
#         return self.buffer[-1]

# def produce_binary_numbers(n):
#     number_queue = Queue()
#     number_queue.enqueue("1")

#     for i in range(n):
#         front = number_queue.fornt()
#         print("   ", front)
#         number_queue.enqueue(front + "0")
#         number_queue.enqueue(front + "1")

#         number_queue.dequeue()

# if __name__ == '__main__':
#     produce_binary_numbers(10)