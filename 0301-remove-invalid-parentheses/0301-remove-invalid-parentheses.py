class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # minimum removal means you want to only remove ) when it's not matched
        # with an open, or any leftover opens 

        # )((()((

        if ")" not in s:
            return [s.replace("(", "")]


        self.max_length = -1
        self.res = set()

        self.dfs(s, 0, [], 0, 0)
        return list(self.res)

    def dfs(self, s, index, curr_res, opens, closes):
        if index == len(s):
            if opens == closes:
                if len(curr_res) > self.max_length:
                    self.max_length = len(curr_res)
                    self.res = set()
                    self.res.add("".join(curr_res))
                elif len(curr_res) == self.max_length:
                    self.res.add("".join(curr_res))  
            return
        
        if s[index] == "(":
            curr_res.append("(")
            self.dfs(s, index + 1, curr_res, opens + 1, closes)
            curr_res.pop()
            self.dfs(s, index + 1, curr_res, opens, closes)
        elif s[index] == ")":
            self.dfs(s, index + 1, curr_res, opens, closes)
            if opens > closes:
                curr_res.append(")")
                self.dfs(s, index + 1, curr_res, opens, closes + 1)
                curr_res.pop()
        else:
            curr_res.append(s[index])
            self.dfs(s, index + 1, curr_res, opens, closes)
            curr_res.pop()




