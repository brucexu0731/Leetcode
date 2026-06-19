class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #do a trie, and then for each new letter inputted, update the current node and return
        # the first three words 

        # new approach -> sort the dictionary

        # 1 - 2 3 - 4 5 - 6
        # 5 - 6 3 - 4 1 - 2
        # each group we have:
        # currFirst, currLast, nextFirst, nextLast
        # prevLast -> currFirst
        # currLast -> prevFirst 

        # 1 - 2 3 - 4 5
        # prevNode, kth, nextNode
        # kth.next = None 
        # prev, curr = nextNode, prevNode.next
        # prevNode.next = kth

        products.sort()
        l, r = 0, len(products) - 1
        res = []

        for i in range(len(searchWord)):
            prefix = searchWord[ : i + 1]
            while l <= r:
                word_l = products[l]
                word_r = products[r]
                prefix_l = word_l[: i + 1]
                prefix_r = word_r[: i + 1]
                if prefix_l != prefix:
                    l += 1
                    continue 
                if prefix_r != prefix:
                    r -= 1
                    continue 
                break
            print(l, r)
            res.append(products[l : min(r + 1, l + 3)])
        
        return res


