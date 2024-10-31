class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        arr = []
        biggest = None
        number = None
        for num in nums:
            count[num] = count.get(num, 0) +1
        print(count.items())
        for i in range(0,k):
            for key,v in count.items():
                if biggest is None or v > biggest:
                    biggest = v
                    number = key
            arr.append(number)
            count[number] = 0
            biggest = None
            number = None
        return arr