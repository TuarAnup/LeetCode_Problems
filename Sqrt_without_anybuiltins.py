class Solution:
    def mySqrt(self, x):
        self.x = x
        z= x
        count = 0
        a = []
        odd = 1
        # return a
        while (x > 0 or x == 0):
            x -= odd
            odd += 2
            count +=1
            
           
        if count**2 >= z:
            return count-1
        else:
            return count
        
            

                    
                

object = Solution()
object.mySqrt(99)
        