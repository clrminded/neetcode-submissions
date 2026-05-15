class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        # 1,2,3,4,5,6 tar=4
        # l         r
        # 0+(5-0)//2 = 2
        # 
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                r = mid-1
    
        return -1