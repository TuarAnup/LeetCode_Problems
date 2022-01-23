class Solution:
    def twosum(self,nums,target):
        a=[]
        self.nums = nums
        self.target = target
        for i in nums:
            x =  target - i
            if x in nums:
                if (nums.index(x),nums.index(i)) in a :
                    pass
                else:
                    a.append((nums.index(i),nums.index(x)))
        print('The required set of indexes for the required target is', a)
       
#Drivers_code 
calc = Solution() 
nums=[2,11,3,6,7,15,-6]
# # print(nums.index(2))
calc.twosum(nums,target = 9)