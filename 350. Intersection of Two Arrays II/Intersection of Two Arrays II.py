class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        nums3 = []
        for i in nums1:
            if(i in nums2):
                nums2.remove(i)
                nums3.append(i)    
        return (nums3)
            
        