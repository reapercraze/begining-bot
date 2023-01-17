import random
import time

lst = [random.randint(1, 10000) for i in range(10000)]


start = time.time()
for i in range(1, 10001):
    for l in lst:
        if i == l: 
            break
end = time.time()
print("time in sec:", end - start)

arr = [3, 1, 4, 1, 6, 2, 9, 5, 7]
print(arr)
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
            
            