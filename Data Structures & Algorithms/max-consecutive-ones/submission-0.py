class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, cur = 0,0
        for num in nums:
            cur += 1
            if num == 0:
                cur = 0
            if cur > ans:
                ans = cur
        return ans
        