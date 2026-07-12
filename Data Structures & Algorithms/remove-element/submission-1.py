class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                for j in range(i+1, n):
                    nums[j-1] = nums[j]
                n -= 1
            else:
                k += 1
                i += 1
        return k
            
            

        