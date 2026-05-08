class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        
        #-1,0,2,4,6,8  target = 4 L=0 R=5
        #.    ^  
        #L.         R
        #
        while L <= R:
            mid = L + ((R - L) // 2)
            
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                return mid
        return -1

        