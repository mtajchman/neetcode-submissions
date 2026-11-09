class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1
        max = arr[i]
        arr[i] = -1
        i -= 1
        while i >= 0:
            temp = arr[i]
            arr[i] = max
            if temp > max:
                max = temp
            i -= 1
        return arr