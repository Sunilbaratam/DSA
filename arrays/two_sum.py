
# if the array is sorted

s = [1,2,3,4,5,6]
target = 20

def two_sum(s, target):
    l,r = 0, len(s)-1
    while(l<r):
        sum = s[l]+s[r]
        if sum > target :
            r-=1
        elif sum < target :
            l+=1
        else:
            return (l,r)   
    return "Not Found"

print(two_sum(s,target))


# if the array is not sorted

s1 = [8,5,7,2,4, 3, 15]
target = 20

def sum(s1, target):
    d = {}
    for i in range(len(s1)):
        diff = target-s1[i]
        if s1[i] in d:
            return (d[s1[i]], i)
        d[diff] = i
    return "Not Found"

print(sum(s1, target))