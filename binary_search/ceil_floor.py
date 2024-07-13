arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5


# What is the floor of x?
# The floor of x is the largest element in the array which is smaller than or equal to x( i.e. largest element in the array <= x).

# What is the ceiling of x?
# The ceiling of x is the smallest element in the array greater than or equal to x( i.e. smallest element in the array >= x).


def ciel(arr, n, x):

    low, high, ans = 0, n-1, -1

    while low<=high:
        mid = (low+high)//2

        if arr[mid]>=x:
            ans = arr[mid]
            high = mid-1
        else:
            low = mid+1

    return ans 

def floor(arr, n, x):
    low, high, ans = 0, n-1, -1

    while low<=high:
        mid = (low+high)//2

        if arr[mid]<=x:
            ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return ans 