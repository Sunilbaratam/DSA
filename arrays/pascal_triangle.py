n=3

res = [[1]]

for i in range(n-1):
    temp = [0]+res[-1]+[0]
    result = []
    for j in range(len(res[-1])+1):
        result.append(temp[j]+temp[j+1])
    res.append(result)
print(res)