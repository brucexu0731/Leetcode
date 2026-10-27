from collections import defaultdict 
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        count = 0

        freq = defaultdict(int)
        l = 0 
        r = 0

        max_freq = 0 

        while r < len(s):
            #expand right bound by 1, check max_freq
            c = s[r]
            freq[c] += 1
            if freq[c] > max_freq:
                max_freq = freq[c]
            r += 1

            #shrink window if invalid
            while r - l > max_freq + k:
                freq[s[l]] -= 1
                l += 1

            print(l, r)
            print(max_freq)
            
            if r - l > max_length:
                max_length = r - l
                count = 1
            elif r - l == max_length:
                count += 1
        
        print(count)
        return max_length



        