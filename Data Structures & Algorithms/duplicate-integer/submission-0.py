class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}
        # loop thru nums
        for n in nums:
            #check if it exists
            if n not in numsMap:
                # insert n into a hashmap with (n, freq)
                numsMap[n] = 1
            else:
                return True
        return False