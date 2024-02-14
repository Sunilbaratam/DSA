import math
nums = [3,6,7,11]
h = 8

l,r = 1,max(nums)
res = max(nums)

while(l<=r):
    hours = 0
    k=(l+r)//2
    for each in nums:
        hours+=math.ceil(each/k)
    if hours<=h:
        res=min(res,k)
        r=k-1
    else:
        l=k+1
print(res)

piles=nums
l,r = 1, max(piles)
res =r

while l<=r:
    k=(l+r)//2
    hours =0
    for p in piles:
        hours+=math.ceil(p/k)
    
    if hours<=h:
        res=min(res,k)
        r=k-1
    else:
        l=k+1
print(res)