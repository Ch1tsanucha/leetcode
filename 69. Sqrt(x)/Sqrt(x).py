class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = 1000000
        sqr = 0
        while l<=r:
            mid = (l + r)//2
            if(mid * mid <= x):
                sqr = mid
                l = mid+1
            else:
                r = mid-1
        return sqr