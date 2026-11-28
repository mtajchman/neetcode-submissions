class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        # loop through nums
        for i, n in enumerate(nums):
            # compute difference
            diff = target - n

            # check if diff is in map
            if diff in hashMap:
                # found solution
                return [ hashMap[diff], i ]
            
            # add n to hashmap
            hashMap[n] = i
        
        