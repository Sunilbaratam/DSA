nums = [-2,1,-3,4,-1,2,1,-5,4]

#brute force approach 
#TC = O(n3)  SC=O(1)

def solve(nums):
    max_sum = min(nums)

    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum = 0
            for k in range(i,j):
                sum+=nums[k]
                max_sum = max(max_sum, sum)
    return max_sum


#better approach 
#TC = O(n2), SC=O(1)

def solve_1(nums):

    max_sum = min(nums)
    
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum+=nums[j]
            max_sum = max(max_sum, sum)
    return max_sum


#optimal approach
#TC = O(n), SC=O(1)

def solve_2(nums):
    max_sum, sum = min(nums), 0
    start, end = -1,-1
    for each in range(len(nums)):
        sum+=nums[each]
        #for getting that optimal sub array
        if sum==0:
            start = each
        if sum>max_sum:
            max_sum = sum
            end= each
        if sum<0:
            sum = 0
    return max_sum, start, end

print(solve(nums))