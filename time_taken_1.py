import time

start = time.time()
i = 1
while i<101:
    print(i)
    i+=1   ### 0.2


# for i in range(1,101):
#     print(i) ### 0.3
print(time.time()-start)