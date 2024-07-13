nums = [3,5,8,15,19]
n = 5


# lower bound is the smallest idx in array such that nums[idx]>=n
# searchinsert code also as same as lower bound
def lower_bound(nums, n):
    
    for i in range(len(nums)):
        if nums[i]>=n:
            return i
    return n


def lower_bound_bs(nums, n):
    low, high = 0, len(nums)
    ans = n
    while low<=high:
        mid = (low+high)//2

        if nums[mid]>=n:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans


# upper bound is the smallest idx in array such that nums[idx]>n
def upper_bound(nums, n):
    
    for i in range(len(nums)):
        if nums[i]>n:
            return i
    return n


def upper_bound_bs(nums, n):
    low, high = 0, len(nums)
    ans = n
    while low<=high:
        mid = (low+high)//2

        if nums[mid]>n:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans