class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        i = len(s)-1
        while i >= 0:
            c = s[i]
            if c.isalnum():
                newstr += s[i].lower()
            i = i-1
        return newstr == newstr[::-1]