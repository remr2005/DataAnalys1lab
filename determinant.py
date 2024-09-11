def calculate_determinant(a):
    for i in range(len(a)):
        if len(a[i])!=len(a):
            print("incorrect data")
            return
    j = 0
    i = 0 
    k=1
    while i < len(a)-1:
        if a[i][j]!=0:
            for d in range(i+1,len(a)):
                a[d] = calculate_sub(a[d],calculate_multiply(a[i],a[d][j]/a[i][j]))
            j+=1
            i+=1
        else:
            for d in range(i+1,len(a)):
                if a[d][j]!=0:
                    buf = a[i].copy()
                    a[i] = a[d]
                    a[d] = buf
                    k*=-1
                    break
                if d == len(a)-1 and a[d][j]==0:
                    return 0
    res = 1
    for i in range(len(a)):
        res*=a[i][i]
    return res*k


def calculate_sub(a,b):
    res = [0]*len(a)
    for i in range(len(a)):
        res[i]= a[i]-b[i]
    return res

def calculate_multiply(a,n):
    res = []
    for i in a:
        res.append(i*n)
    return res