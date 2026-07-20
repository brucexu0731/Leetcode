class ListNode:
    def __init__(self, val, key, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next 
        self.key = key

class LinkedList:
    def __init__(self):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        if not self.head.next.next:
            return True
        else:
            return False 

    def insert_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        node.prev.next = node
    
    def remove_tail(self):
        node = self.tail.prev 
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.key

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.min = 0
        self.groups = {} #1, 2, 3, ... -> linked list of nodes at that frequency 
        self.nodes = {} #key -> node 
        self.frequencies = {} #key -> frequency, keys of frequencies and groups should be identical

        #creating the frequency 1 group for future inserts 
        self.groups[1] = LinkedList()
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.frequencies:
            return -1 

        freq = self.frequencies[key]
        node = self.nodes[key]
        self._remove(node)
        head = self.groups[freq]
        #if the current min_frequency is removed 
        if freq == self.min and head.is_empty():
            self.min += 1
        
        freq += 1
        self.frequencies[key] += 1
        if freq not in self.groups:
            self.groups[freq] = LinkedList()

        new_head = self.groups[freq]
        new_head.insert_head(node)

        return node.val 


    def put(self, key: int, value: int) -> None:
        if key in self.frequencies:
            node = self.nodes[key]
            node.val = value
            self.get(key)
            return

        node = ListNode(value, key)
        self.nodes[key] = node

        if self.capacity == 0:
            removal_head = self.groups[self.min]
            removed_key = removal_head.remove_tail()
            self.frequencies.pop(removed_key)
            self.nodes.pop(removed_key)
            self.capacity += 1

        
        self.frequencies[key] = 1
        curr_head = self.groups[1]
        curr_head.insert_head(node)
        self.capacity -= 1
        self.min = 1


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)