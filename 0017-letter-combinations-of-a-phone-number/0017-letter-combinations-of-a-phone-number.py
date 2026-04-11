class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not digits:
            return []

        res = []

        def dfs(string, i):
            if i >= len(digits):
                res.append(string)
                return 

            letters = letters_map[digits[i]]
            for c in letters:
                string += c
                dfs(string, i + 1)
                string = string[:-1]
        
        dfs('', 0)
        return res
