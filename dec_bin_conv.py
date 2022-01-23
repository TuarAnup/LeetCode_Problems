class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = [0,1]
        bv = ''
        while n>=1:
            rem = n%2
            rem = str(rem)
            bv+= rem
            n = n//2
        bv = bv[::-1]
        return int(bv)
            

object = Solution()
object.bitwiseComplement(2)      


        