class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        res = 1
        i = 0
        while True:
            if len(arr) == len(nums):
                break
            if i == len(arr):
                i += 1
            if i == len(nums):
                arr.append(res)
                res = 1
                i = 0
                continue
            res = nums[i] * res
            i += 1
            
        return arr