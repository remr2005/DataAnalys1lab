import bisect

# Sundaram Sieve
def gen(n):
    arr = []
    for i in range(1,int(((4*n+1)**0.5 - 1)//2+1)):
        for j in range(i,int((2*n-i)//(2*i+1)+1)):
            arr.append(i+j+2*i*j)
    arr_2 = [2*i+1 for i in range(2*n) if i not in arr]
    i = bisect.bisect_left(arr_2, n)
    j = bisect.bisect_left(arr_2, n-1)
    if abs(arr_2[i]-n)>abs(arr_2[j]-n):
        return arr_2[j]
    else:
        return arr_2[i]