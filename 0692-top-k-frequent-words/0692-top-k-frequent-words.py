from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for i in range(len(words)):
                freq[words[i]] += 1
        
        res = []
        for word, frequency in freq.items():
            res.append((frequency, word))
        
        res.sort(key = lambda x: (-x[0], x[1]))

        res_words = [x[1] for x in res]
        
        if len(res) < k:
            return []
        return res_words[:k]
        # Multiple lines 
# line -> contain words 

# top K frequent words in descending order 

# [(word, freq)]

# abc abc def , K=

# [(abc, 2), (def, 1)]
# line 1: abc abc def
# lin2: efg egf abc 

# n number of words, sort, and then grab the first k -> n log (n)

# Count frequency of words using hashmap, then use min heap of size k to get top k frequent words
# abc abc abc abc ab ab ab ac ac a k = 2
# { ac: 2, a: 1, abc: 4, ab: 3, }
# [2, ] [1, 2] [2, 4] [3, 4]
#from collections import defaultdict
# def getTopK(words: List(List(str)), k) -> List(tuple(str, int)):
#     freq = defaultdict(int)
#     for i in len(words):
#         for j in len(words[0]):
#             freq[words[i][j]] += 1
    
#     res = ()
#     for word, frequency in freq.items():
#         res.append((-frequency, word))
    
#     res.sort()
    
#     if len(res) < k:
#         return []
#     return res[:k]


#print(getTopK([[abc, abc, abc, abc, ab, ab, ab, ac, ac, a]), 2)

# Communication - 
# Code Correctness 
# Code Quality / Readability
# Code Optimality 
# Debugging 
