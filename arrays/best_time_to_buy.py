prices = [5,1,3,6,9]

def get(prices):
    max_profit = 0
    l,r = 0,1
    while(r<len(prices)):
        if prices[l]<prices[r]:
            profit = prices[r]-prices[l]
            max_profit = max(profit, max_profit)
        else:
            l=r
        r+=1
    return max_profit

print(get(prices))
        