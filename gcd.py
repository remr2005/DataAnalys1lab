from functools import lru_cache

# the correct decision
def gcd_eight(a):
    try:
        a = a<<0
    except Exception as e:
        print(f"incorrect input, error:{e}")
        return
    if not (99999 >= a >= 10000 or -99999 >= a >= -10000):
        print("incorrect input")
        return
    s = 1
    while(a&1==0):
        a = a>> 1
        s = s << 1
    return s

# i thought that was right decision, but i am anyway use -,
# so this is incorrect
# Binary algorithm for finding GCD(Greatest Common Divisor)
@lru_cache()
def binary_alg(m: int,n:int):
    if m == 0 or m == n:
        return n
    elif n == 0:
        return m
    elif is_even(m) and is_even(n):
        return binary_alg(m>>1,n>>1)<<1
    elif is_even(m):
        return  binary_alg(m>>1,n)
    elif is_even(n):
        return binary_alg(m,n>>1)
    elif n > m:
        return binary_alg(m,(n-m)>>1)
    else:
        return binary_alg((m-n)>>1,n)
    
# The binary view of 1 is 00...001, so when you using & operation, 
# the even number look like ......0, 0 & 1 equal 0, but odd number
# look like .......1, so 1 & 1 equal 1
def is_even(n: int):
    return True if n & 1 == 0 else False