class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - ord("a")] += 1
            count[tuple(arr)].append(word)
        print(count)
        return count.values()
        

