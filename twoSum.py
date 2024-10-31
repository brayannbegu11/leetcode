class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enum = {}
        for i in range(len(nums)):
            enum[nums[i]] = enum.get(nums[i], i) 
            newTarget = target - nums[i]
            if newTarget in enum.keys() and enum[newTarget] != i:
                return [enum[newTarget], i]