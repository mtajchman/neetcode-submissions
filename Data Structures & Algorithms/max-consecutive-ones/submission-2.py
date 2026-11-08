class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons = 0
        max_num = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                cons += 1
            else:
                cons = 0
            
            if cons > max_num:
                max_num = cons
            
        return max_num