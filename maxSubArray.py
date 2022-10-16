class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initalize maxSum to first value in array cuz nums > 0
        # current pointer init to 0
        maxSum = nums[0]
        currSum = 0

        # loop through each value nums to see if there are negatives
        # if there are negatives, reset to 0
        # then increment nums with n
        # return maxSum with max values of maxSum and the current computation
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(maxSum, currSum)
        return maxSum
