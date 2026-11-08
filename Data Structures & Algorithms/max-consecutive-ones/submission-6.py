class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = max_num = 0

        for num in nums:
            if num == 0:
                max_num = max(max_num, cnt)
                cnt = 0 
            else: 
                cnt += 1
        
        return max(max_num, cnt)