class Solution:
    def strStr(self, haystack, needle):
        self.haystack = haystack 
        self.needle = needle
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1



haystack = input('Enter the haystack')
needle = input('Enter the needle')
object = Solution()
object.strStr(haystack,needle)