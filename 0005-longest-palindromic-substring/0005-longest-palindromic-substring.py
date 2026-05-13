class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        index = (0, 0)

        #check odd

        for k in range(len(s)):
            l, r = k, k
            curr_len = -1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len += 2
                if curr_len > max_len:
                    max_len = curr_len
                    index = (l, r)
                l -= 1
                r += 1
        
        #check even
        for k in range(len(s)):
            l, r = k, k + 1
            curr_len = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len += 2
                if curr_len > max_len:
                    max_len = curr_len
                    index = (l, r)
                l -= 1
                r += 1

        l, r = index
        return s[l : r + 1]