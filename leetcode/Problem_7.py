class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1    
        x = abs(x)                   
        
        r = 0
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        
        r *= sign  
        
        if r < -2**31 or r > 2**31 - 1:
            return 0
        
        return r
