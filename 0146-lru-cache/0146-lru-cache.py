class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None 
    
class LRUCache:

    def __init__(self, capacity: int):
        self.dummy = ListNode([-1, -1])
        self.tail = None
        self.length = 0
        self.capacity = capacity
        #maps key to a node 
        self.nodes = {}

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.update(node)
            return node.val[1]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        #If key already exist, update value 
        if key in self.nodes:
            node = self.nodes[key]
            node.val[1] = value
            self.update(node)
        else:
            node = ListNode([key, value])
            self.nodes[key] = node

            if self.length == 0:
                self.dummy.next = node
                node.prev = self.dummy 
                self.tail = node
            else:
                tmp = self.dummy.next 
                tmp.prev = node
                node.next = tmp
                node.prev = self.dummy
                self.dummy.next = node

            self.length += 1
            
            if self.length > self.capacity:
                tmp = self.tail
                self.tail = self.tail.prev 
                self.tail.next = None
                self.nodes.pop(tmp.val[0])
                self.length -= 1


        #If key doesn't exist, add to front
        #If at capacity, remove tail and set new tail 
        #If 
    
    def update(self, node):
        if self.dummy.next == node:
            return

        if self.tail == node:
            self.tail = node.prev
            node.prev.next = node.next
        else: 
            node.prev.next = node.next
            node.next.prev = node.prev
        
        tmp = self.dummy.next 
        tmp.prev = node

        node.next = tmp
        node.prev = self.dummy

        self.dummy.next = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)