from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build adjacency list (two pointers), keep track of the source -> then topo sort
        
        # check every work against every other word, 2 pointers, and then for the two words,
        # check the first chars that they differ in, and that gives us a relationship 

        # [ugh ush isk ohd egd]
        # g -> s, u -> i, i -> o, o -> e, and then all the rest of the characters we don't know

        if len(words) == 1:
            return "".join(set(words[0]))
        adj = defaultdict(list)
        all_chars = set()
        
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                w1 = words[i]
                w2 = words[j]
                a, b = 0, 0
                #find the first different character
                while a < len(w1) and w1[a] == w2[b]:
                    all_chars.add(w1[a])
                    all_chars.add(w2[b])
                    a += 1
                    b += 1
                    if a < len(w1) and b >= len(w2):
                        return ""
                        break
                
                if a < len(w1) and b < len(w2):
                    adj[w1[a]].append(w2[b])

                for k in range(a, len(w1)):
                    #print(w1[i])
                    all_chars.add(w1[k])
                for k in range(b, len(w2)):
                    #print(w2[i])
                    all_chars.add(w2[k])
        
        res = []
        visit = set()
        def dfs(n, path):
            nonlocal res 
            if n in path:
                return False 
            if n in visit:
                return True 
            if not adj[n]:
                res.append(n)
                visit.add(n)
                return True
            
            path.add(n)
            acc = True
            for node in adj[n]:
                acc = acc and dfs(node, path)
            path.remove(n)
            res.append(n)
            visit.add(n)
            return acc

        for c in all_chars:
            if not dfs(c, set()):
                return ""

        ans = ''
        for char in res:
            ans = char + ans
        
        return ans



