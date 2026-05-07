class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, n in enumerate(nums):
            my_dict[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in my_dict and my_dict[diff] != i:
                return [i, my_dict[diff]]
        return []

# {3:0, 4:1, }
        