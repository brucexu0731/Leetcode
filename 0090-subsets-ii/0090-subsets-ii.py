class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        num_freq = {}
        for n in nums:
            if n not in num_freq:
                num_freq[n] = 1
            else:
                num_freq[n] += 1
        keys = list(num_freq.keys())

        def dfs(path, i):          
            if i >= len(keys):
                res.append(path[:])
                return
            for j in range(num_freq[keys[i]] + 1):
                if j == 0:
                    dfs(path[:], i + 1)
                else:
                    path.append(keys[i])
                    dfs(path[:], i + 1)

        dfs([], 0)
        return res        

        