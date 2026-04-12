class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

# 10^2
# 10^9 - operations in a second
# 10^6 or 10^7
# hashMap O(n)

# Get every permutation of s1 check if it's a substring of s2 
# getting every substring from s2 see if it mateches everything in s1 

# convert s1 into hashmap of unqiue characters and frequency 
# L, R pointer sliding window from s2, 
# - if current element at R is not in hashmap, L, R reset at curr + 1 
# ab.  cdefgaoab 
# aabaa  aaaaaba
 # ab acab

# defaultdict

        freq_map = {}
        freq_map_copy = {}
        for c in s1:
            if c not in freq_map:
                freq_map[c] = 1
                freq_map_copy[c] = 1
            else:
                freq_map[c] += 1
                freq_map_copy[c] += 1

        l, r = 0, 0
        while r < len(s2) and l < len(s2):
            if s2[r] not in freq_map:
                freq_map = copy.deepcopy(freq_map_copy)
                r += 1
                l = r
                continue 
            
            while freq_map[s2[r]] == 0 and l <= r :
                freq_map[s2[l]] += 1
                l += 1
            
            freq_map[s2[r]] -= 1
            r += 1
            print(l, r)
            if r - l + 1 > len(s1):
                return True
        
        return False 


# print(isPermutation('aabaa', 'aaaaaba'))
# print(isPermutation('aacaa', 'aaaaaba'))
# print(isPermutation('ab', "eidboaoo"))
# print(isPermutation('abccc', 'abc'))