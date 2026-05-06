class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        i = 1
        while i <= length:
            if nums[i-1] == val:
                for j in range(i, length):
                    nums[j-1] = nums[j]
                length -= 1
                k += 1
            else:
                i += 1
        return length

            

