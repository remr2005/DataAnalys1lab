from functools import lru_cache

def FibSums(n):
    sum = [0]
    for i in range(n+1):
        sum.append(0)
        sum[i+1]+=sum[i] + fib_numb(i)
        yield sum[i+1]
    
    
@lru_cache()        
def fib_numb(n):
    if n == 0: 
        return 0
    elif n ==1:
        return 1
    else:
        return fib_numb(n-2)+fib_numb(n-1)