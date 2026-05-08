class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ptr1 = 0
        while ptr1 < len(arr)-1:
            ptr2 = ptr1+1
            max_right = arr[ptr2]
            for i in range(ptr2, len(arr)):
                max_right = max(max_right, arr[i])
            arr[ptr1] = max_right
            ptr1+=1
        arr[ptr1] = -1
        return arr
    




        