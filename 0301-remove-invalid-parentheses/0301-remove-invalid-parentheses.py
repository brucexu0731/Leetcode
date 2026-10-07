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
        elif "(" not in s:
            return [s.replace(")", "")]
        
        left_remove = 0
        right_remove = 0

        for c in s:
            if c == "(":
                left_remove += 1
            elif c == ")":
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1


        self.max_length = -1
        self.res = set()

        self.dfs(s, 0, [], 0, left_remove, right_remove)
        return list(self.res)

    def dfs(self, s, i, curr, balance, left_remove, right_remove):
        if i == len(s):
            if balance == 0 and left_remove == 0 and right_remove == 0:
                self.res.add("".join(curr))
            return

        c = s[i]

        if c == "(":
            # remove it
            if left_remove > 0:
                self.dfs(s, i + 1, curr, balance,
                        left_remove - 1, right_remove)

            # keep it
            curr.append(c)
            self.dfs(s, i + 1, curr, balance + 1,
                    left_remove, right_remove)
            curr.pop()

        elif c == ")":
            # remove it
            if right_remove > 0:
                self.dfs(s, i + 1, curr, balance,
                        left_remove, right_remove - 1)

            # keep it
            if balance > 0:
                curr.append(c)
                self.dfs(s, i + 1, curr, balance - 1,
                        left_remove, right_remove)
                curr.pop()

        else:
            curr.append(c)
            self.dfs(s, i + 1, curr, balance,
                    left_remove, right_remove)
            curr.pop()