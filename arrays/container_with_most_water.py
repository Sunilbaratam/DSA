# find the container with most water

l = [1,8,6,2,5,4,8,3,7]

# there are two methods to solve this

# first method in bruteforce approach

def find_the_container(l):
    area = 0
    for i in range(len(l)):
        for j in range(i+1, (len(l))):
            prod = min(l[i],l[j])*(j-i)
            area = max(prod, area)
    return area

print(find_the_container(l))


#second method in two pointer approach

def find_the_container_1(k):
    res = 0
    l,r = 0, len(k)-1
    while(l<r):
        area = (l-r)*min(k[l], k[r])
        res = max(area, res)
        if k[l]>k[r]:
            r-=1
        elif k[l]<k[r]:
            l+=1
    return res

print(find_the_container_1(l))
