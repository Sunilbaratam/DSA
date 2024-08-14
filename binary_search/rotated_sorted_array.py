
# Search in rotated sorted array

def search(nums, k):

    low, high = 0, len(nums)-1

    while low<=high:

        mid = (low+high)//2

        if nums[mid]==k:
            return mid
        
        if nums[low]==nums[high]==nums[mid]:
            low+=1
            high-=1
            continue
        
        if nums[low]<=nums[mid]:
            if nums[low]<=k<=nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<=k<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    return -1







# Find minimum in rotated sorted array

def min_array(nums):

    low, high, ans = 0, len(nums)-1, max(nums)

    while low<=high:
        mid = (low+high)//2

        if nums[low]<=nums[mid]:
            ans = min(ans, nums[low])
            low = mid+1
        else:
            ans = min(ans, nums[mid])
            high = mid-1
    return ans



# Find out how many times the array has been rotated
# to find the no of times rotated is to find the index of the min in rotated sorted array

