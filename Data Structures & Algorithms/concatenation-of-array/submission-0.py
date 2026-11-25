class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [None] * 2 * length
        for i in range(0, length):
            print(i)
            print(nums[i])
            ans[i] = nums[i]
            ans[i+length] = nums[i]
        return ans