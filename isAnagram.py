class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        countFirst = {}
        countSecond = {}
        for letter in range(len(s)):
            countFirst[s[letter]] = countFirst.get(s[letter], 0) + 1
            countSecond[t[letter]] = countSecond.get(t[letter], 0) + 1
        if countFirst == countSecond:
            return True
        return False
