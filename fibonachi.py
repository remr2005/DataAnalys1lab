from functools import lru_cache

def FibSums(n:int):
    sum = 0
    for i in range(n):
        sum += fib_numb(i)
        yield sum
    
def FibSums(n: int):
    sum = 0
    fr = 0
    sc = 1
    for i in range(n):
        if i == 0:
            yield 0
        else:
            sum += fr
            yield sum
        fr, sc = sc, fr + sc
    
    
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