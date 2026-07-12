class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            ptr1 = i+1
            cur_max = float('-inf')
            for j in range(ptr1, len(arr)):
                if arr[j] > cur_max:
                    cur_max = arr[j]
            arr[i] = cur_max
        arr[-1] = -1
        return arr
        