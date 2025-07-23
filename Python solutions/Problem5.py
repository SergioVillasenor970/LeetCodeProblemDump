class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)): #Even case
            if i != len(s)-1 and s[i] == s[i+1]:
                this_try = self.evenPalindrome(Solution ,s, i)
                if len(this_try) > len(res):
                    res = this_try
            if i != len(s)-1 and s[i-1] == s[i+1]: #Odd case
                this_try = self.oddPalindrome(Solution ,s, i)
                if len(this_try) > len(res):
                    res = this_try
            if len(res) <= 1:
                res = s[i]
        return res

    def evenPalindrome(self, s: str, i: int) -> str:
        res = i
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res = s[left:right + 1]
            left -= 1
            right += 1
        return res

    def oddPalindrome(self, s: str, i: int) -> str:
        res = ""
        center = i
        left = i - 1
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res = s[left:right + 1]
            left -= 1
            right += 1
        return res