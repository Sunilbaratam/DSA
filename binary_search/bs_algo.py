nums = [1,2,3,4,5,6,7,8,9]
target = 6

def iterative_binary_search(nums, target):

    low, high = 0, len(nums)-1

    while low<=high:

        mid = (low+high)//2

        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1

def recursive_binary_search(nums, low, high, target):
    if low>high:
        return -1
    
    mid = (low+high)//2

    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return recursive_binary_search(nums,mid+1, high, target)
    
    return recursive_binary_search(nums,low, mid-1, target)

print(iterative_binary_search(nums, target))
print(recursive_binary_search(nums, 0, len(nums)-1, target))