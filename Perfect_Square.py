class Solution:
    def isPerfectSquare(self, num):
        self.num = num
        a = []
        for val in range(0,num+1):
            a.append(val**2)
        if num in a:
            return True
        else:
            return False
        
        

object = Solution()
object.isPerfectSquare(1)
        