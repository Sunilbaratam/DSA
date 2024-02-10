# return the 3 indices whose sum is equal to target given by the user

l = [-1,0,1,2,-1,-4]

def three_sum(nums, target):
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        if i>0 and a == nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while(l<r):
            if a+nums[l]+nums[r] > target :
                r-=1
            elif a+nums[l]+nums[r] < target:
                l+=1
            else:
                res.append([a, nums[l], nums[r]])
                l+=1
                while(nums[l]==nums[l-1] and l<r):
                    l+=1
        return res
    
print(three_sum(l,0))