# product of an array except itself


l = [1,9,7,3,10]

def product(l):
    p=len(l)
    a,b = [1]*p, []*p
    m=1
    for i,j in enumerate(l):
        a[i]=m
        m*=j
    n=1
    for k in range(len(l)-1, -1, -1):
        a[k]=n*a[k]
        n*=l[k]

    return a
print(product(l)) 