class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hs = {}
        
        for i in range(len(nums)):
            sum = target - nums[i]
            
            if sum in hs:
                return[i, hs[sum]]  
            
            hs[nums[i]] = i
