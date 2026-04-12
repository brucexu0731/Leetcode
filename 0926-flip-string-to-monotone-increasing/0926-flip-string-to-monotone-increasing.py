class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # remove 1s <- 0 -> min(0, 1)
        # min(0, 1) <- 1 -> remove 0s
        # so at each index we want the prefix of how many zeros, how many 1s
        # and suffix of how many zeros, how many 1s
        pref0 = [0]
        pre0 = 0
        pref1 = [0]
        pre1 = 0
        suff0 = [0] * len(s)
        post0 = 0
        suff1 = [0] * len(s)
        post1 = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                pre0 += 1
            elif s[i] == '1':
                pre1 += 1
            pref0.append(pre0)
            pref1.append(pre1)

        for i in range(len(s) - 1, 0, -1):
            if s[i] == '0':
                post0 += 1
            elif s[i] == '1':
                post1 += 1
            suff0[i - 1] = post0
            suff1[i - 1] = post1
        

        res = float('inf')
        for i in range(len(s)):
            if s[i] == '0':
                operations = pref1[i] + min(suff0[i], suff1[i])
            elif s[i] == '1':
                operations = min(pref0[i], pref1[i]) + suff0[i]
            res = min(res, operations)
        
        return res





            