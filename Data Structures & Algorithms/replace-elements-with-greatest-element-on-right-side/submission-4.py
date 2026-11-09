class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1
        max_n = -1
        while i >= 0:
            temp = arr[i]
            arr[i] = max_n
            max_n  = max(temp, max_n)
            i -= 1
        return arr