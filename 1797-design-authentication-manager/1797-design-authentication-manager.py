from collections import deque 

class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.ttl = timeToLive
        self.tokens = {}
        self.list = deque()        

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.list.append((tokenId, currentTime + self.ttl))
        self.tokens[tokenId] = currentTime + self.ttl
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId not in self.tokens:
            return
        if self.tokens[tokenId] <= currentTime:
            return

        self.list.append((tokenId, currentTime + self.ttl))
        self.tokens[tokenId] = currentTime + self.ttl
        

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """

        while self.list and self.list[0][1] <= currentTime:
            token = self.list[0][0]
            if token in self.tokens and self.tokens[token] <= currentTime:
                self.tokens.pop(token)
            self.list.popleft()
        
        return len(self.tokens)

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)