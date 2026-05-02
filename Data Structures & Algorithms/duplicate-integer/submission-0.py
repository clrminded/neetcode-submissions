class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
            if hm[num] > 1:
                return True
        return False
        

