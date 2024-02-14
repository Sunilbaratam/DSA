#brute force solution is to apply merge sort with time complexity O(logn) and space complexity O(n)


#better solution with time complexity O(n+n) and space complexit O(1)
def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a,b,c=0,0,0

        for each in nums:
            if each == 0:
                a+=1
            elif each==1:
                b+=1
            else:
                c+=1
        
        for i in range(0,a):
            nums[i]=0
        for j in range(a, a+b):
            nums[j]=1
        for k in range(a+b, a+b+c):
            nums[k] = 2


#optimal solution with time complexity O(n) and space complexity O(1)
def abc(nums):
        low, mid, high  =  0, 0, len(nums)-1

        while(mid<=high):

            if nums[mid] == 0:
                nums[low], nums[mid] =nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid] ==1:
                mid+=1
            else:
                nums[high], nums[mid] = nums[high], nums[mid]
                high-=1
                

