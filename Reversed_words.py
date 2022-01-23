

class Solution:
    def reverseWords(self, s):
        self.s = s 
        s = s.split()
        a = ""
        j = ' '
        for val in range(len(s)-1,-1,-1):
            a += (s[val])
            if val>0:
                a += j
            
        return a
       
            
        
object = Solution()
object.reverseWords('The sky is blue')