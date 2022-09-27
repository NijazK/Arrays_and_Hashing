class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Initialize hash set
        hs = set()

        # Loop through nums array to see if there are matching integers
        # if there are return true, else keep adding the integers to the hash set
        for i in nums:
            if i in hs:
                return True
            else:
                hs.add(i)
        return False
