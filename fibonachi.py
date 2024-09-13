from functools import lru_cache

def FibSums(n:int):
    sum = 0
    for i in range(n):
        sum += fib_numb(i)
        yield sum
    
    
@lru_cache()        
def fib_numb(n: int):
    if n == 0: 
        return 0
    elif n ==1:
        return 1
    else:
        return fib_numb(n-2)+fib_numb(n-1)
    
def find_in_fibonachi(n: int):
    j = 0
    fib_gen = FibSums(n)
    while True:
        i = next(fib_gen)
        if len(str(i)) > len(str(n)):
            return j
        j += 1