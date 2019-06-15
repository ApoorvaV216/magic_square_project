import math
from sys import stdout
LOG_10 = 2.302585092994
def odd(s):
    if s % 2 == 0:
        s += 1
    q = [[0 for j in range(s)] for i in range(s)]
    p = 1
    i = s // 2
    j = 0
    while p <= (s * s):
        q[i][j] = p
        ti = i + 1
        if ti >= s: ti = 0
        tj = j - 1
        if tj < 0: tj = s - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1
    return q, s
def even(s):
    if s % 2 == 1:
        s += 1
    while s % 4 == 0:
        s += 2
    q = [[0 for j in range(s)] for i in range(s)]
    z = s // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = odd(z)
    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d
 
    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, s):
            if i < lc or i > s - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t
    
    return q, s
 
 
def format_sqr(s, l):
    for i in range(0, l - len(s)):
        s = "0" + s
    return s + " "
 
 
def display(q):
    s = q[1]
    print(" - {0} x {1}\n".format(s, s))
    k = 1 + math.floor(math.log(s * s) / LOG_10)
    for j in range(0, s):
        for i in range(0, s):
            stdout.write(format_sqr("{0}".format(q[0][i][j]), k))
        print()
    print("Magic sum: {0}\n".format(s * ((s * s) + 1) // 2))
def isMagicSquare( mat) : 
    s = 0
    s1=0
    r=N-1
    for i in range(0, N) : 
        s = s + mat[i][i]
    for i in range(0, N) : 
        s1 = s1 + mat[i][r]
        r=r-1

    if(s!=s1):
            return False;
    for i in range(0, N) : 
        rowSum = 0;      
        for j in range(0, N) : 
            rowSum += mat[i][j] 
        if (rowSum != s) : 
            return False
    for i in range(0, N): 
        colSum = 0
        for j in range(0, N) : 
            colSum += mat[j][i] 
        if (s != colSum) : 
            return False
    print(rowSum,colSum,s,s1)
    return True
def DoublyEven(n): 
        arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 
        l=int(n/4); 
        for i in range(0,l): 
                for j in range(0,l): 
                        arr[i][j] = (n*n + 1) - arr[i][j];  
        for i in range(0,l): 
                for j in range(3 * l,n): 
                        arr[i][j] = (n*n + 1) - arr[i][j];  
        for i in range(3 * l,n): 
                for j in range(0,l): 
                        arr[i][j] = (n*n + 1) - arr[i][j];  
        for i in range(3 * l,n): 
                for j in range(3 * l,n): 
                        arr[i][j] = (n*n + 1) - arr[i][j];
        for i in range(l,3 *l): 
                for j in range(l,3 * l): 
                        arr[i][j] = (n*n + 1) - arr[i][j]; 
        print(isMagicSquare(arr))
        return arr,N
    #c-a+b,c,c+a-b,'\n',a+c,c-a-b,c+b,end=''
N = int(input("enter order of magic square:"))
if N%2==1:
        display(odd(N))
elif N%4==0:
        display(DoublyEven(N))
else:
	display(even(N))
