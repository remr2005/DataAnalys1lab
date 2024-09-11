from functools import lru_cache

def FibSums(n):
    sum = 0
    for i in range(1,n+1):
        sum += fib_numb(i)
        yield sum
    
    
@lru_cache()        
def fib_numb(n):
    if n == 0: 
        return 0
    elif n ==1:
        return 1
    else:
        return fib_numb(n-2)+fib_numb(n-1)