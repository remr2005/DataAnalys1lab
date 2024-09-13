import bisect
import random
import math
from time import time

# Не работает на болших числах))))
# Sundaram Sieve
def gen(n):
    i = 0
    print(time())
    while (True):
        if miller_rabin_test(n+i):
            if slow_is_prime(n+i):
                print(time())
                return n+i
            else:
                print("error in miller test")
        elif miller_rabin_test(n-i):
            if slow_is_prime(n-i):
                print(time())
                return n-i
            else:
                print("error in miller test")
        i+=1
    
def slow_is_prime(n):
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return False
    return True


def miller_rabin_test(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Основной цикл теста
    for _ in range(int(math.log2(n))):
        f = False
        a = random.randint(2, n - 2)
        x = pow(a, d, n) 
        
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                f = True
                break
            elif x == 1:
                return False
        
        if not f:
            return False
    
    return True
