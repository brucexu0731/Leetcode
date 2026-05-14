class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        print("我".join(strs))
        return "我".join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        curr = ''
        for c in s:
            if c == '我':
                res.append(curr)
                curr = ''
            else:
                curr += c
        res.append(curr)
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))