class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = defaultdict(list)
        for i in range(len(numbers)):
            newTarget = target - numbers[i]
            print('keys', count.keys())
            print('Target', newTarget)
            if newTarget in count.keys() and count[newTarget] != i +1:
                return [count[newTarget], i+1]
            count[numbers[i]] = i + 1