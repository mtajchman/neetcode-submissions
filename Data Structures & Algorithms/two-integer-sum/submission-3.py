class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize a hashmap
        hashMap = {}

        # loop through nums
        for i, n in enumerate(nums):
            # check if that number is in there already
            if n not in hashMap:
                # add it to map
                hashMap[n] = i # smaller index 

        # loop again?
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                if hashMap[diff] != i:
                    if hashMap[diff] < i:
                        return [hashMap[diff], i]
                    else:
                        return [i, hashMap[diff]]

        return [None, None]