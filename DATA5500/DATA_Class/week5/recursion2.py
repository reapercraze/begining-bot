def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    lst = [ 0, 1]
    for i in range(n):
        lst.append(lst[i+1] + lst[i])
        
    return lst[n]
    
print(fibonacci(20))

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
    
print(fib(20))

