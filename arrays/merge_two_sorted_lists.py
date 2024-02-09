#merge the below sorted lists

l1 = [1,1,1,3,5,7,9]
l2 = [2,4,6,8,10]

def merge(l1, l2):
    res = []
    i,j =0,0

    while(True):
        if l1[i]>l2[j]:
            res.append(l2[j])
            j+=1
        elif l1[i]<l2[j] or l1[i]==l2[j]:
            res.append(l1[i])
            i+=1
        ##print(res)
        if i==len(l1):
            res.extend(l2[j:])
            return res
        if j==len(l2):
            res.extend(l1[i:])
            return res
        
        

print(merge(l1, l2))