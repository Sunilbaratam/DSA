# find the third maximum number in the array

l = [87,56,220,75,1000,1,1150, 400, 10000]

def find(l):
    m1, m2, m3 =0,0,0

    for i,a in enumerate(l):
        if a>m1:
            m3=m2
            m2=m1
            m1=a
        elif m1>a>m2:
            m3=m2
            m2=a
        elif m2>a>m3:
            m3=a
    return m3

print(find(l))