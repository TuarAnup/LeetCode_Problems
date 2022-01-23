class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        self.nums1= nums1
        self.nums2=nums2
        nums = nums1 + nums2
        nums = sorted(nums)
        if len(nums)%2 == 1:
            z=int(len(nums)/2)
            return float(nums[z])
        else:
            z=int(len(nums)/2)
            return (nums[z]+nums[z-1])/2
            
            
        
        
nums1 = [1,2]
nums2 = [3,4]

object = Solution()
object.findMedianSortedArrays(nums1,nums2)
