#this problem is kind of fibonacci program.
#three types of solutions will going to study. they are: recursion, memoization and DP.

#RECURSIVE SOLUTION
def recursive(n):
    if n<=1:
        return 1
    return recursive(n-1)+recursive(n-2)


#MEMOIZATION SOLUTION
def memoization(n, memo):
    if n in memo:
        return memo[n]
    if n<=1:
        return 1
    
    memo[n] = memoization(n-1, memo) + memoization(n-2, memo)
    return memo[n]

#DP SOLUTION
def dp_sol(n):
    if n<=1:
        return 1
    
    dp = [0]*(n+1) 
    dp[0], dp[1] = 1,1

    for i in range(2,n+1):
        dp[n] = dp[n-1]+dp[n-2]
    return dp[n]

