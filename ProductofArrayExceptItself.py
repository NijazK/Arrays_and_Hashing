class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Initialize n to length of array nums
        # Initialize output to index multiplied to n
        n = len(nums)
        output = [0]*n
    
        # First pass is in-order
        prev = 1
        for i in range(n):
            output[i] = prev
            prev *= nums[i]
        
        # second pass is in-reverse to compute products
        post = 1
        for i in range(1, n+1):
            output[-i] *= post
            post *= nums[-i]
        
        # return output
        return output
