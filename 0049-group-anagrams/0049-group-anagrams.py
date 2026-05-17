class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            charmap = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                charmap[i] += 1
            charhash = tuple(charmap)
            if charhash not in groups:
                groups[charhash] = [s]
            else:
                groups[charhash].append(s)
        
        res = []
        for group in groups.values():
            res.append(group)
        
        return res