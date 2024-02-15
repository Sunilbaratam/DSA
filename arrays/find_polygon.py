#leetcode = 2971


nums = [5,5,5]

def perimeter(nums):
    nums.sort()
    s = sum(nums)

    for i in range(len(nums)-1, -1,-1):
        if s-nums[i]>nums[i]:
            return s
        s-=nums[i]
    return -1 

print(perimeter(nums))