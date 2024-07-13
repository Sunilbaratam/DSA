# find the first and last occurence of the duplicate element which is present in sorted array
# we can do last-first+1 to find the count of occurences of the element in that array



def first(nums, k):
    low, high, f =  0, len(nums)-1, -1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==k:
            high = mid-1
            f = mid
        elif nums[mid]>k:
            high = mid-1
        else:
            low = mid+1
    return f

def last(nums, k):
    low, high, l =  0, len(nums)-1, -1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==k:
            high = mid+1
            l = mid
        elif nums[mid]>k:
            high = mid-1
        else:
            low = mid+1
    return l