class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_num = 0

        for num in nums:
            count = count + 1 if num else 0
            max_num = max(count, max_num)
        return max_num