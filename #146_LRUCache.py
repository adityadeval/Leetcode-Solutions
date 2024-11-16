# Leetcode problem : 146. LRU Cache
# Problem description : https://leetcode.com/problems/lru-cache/description/
# Run: O(1), Space: O(1)

class Node:
    def __init__(self, key: int = -1, val: int = 0):
        self.prev, self.next = None, None
        self.key, self.val = key, val

class LRUCache:
    def __init__(self, capacity: int):
        # head and tail are always going to be dummy nodes. All nodes in between would be 
        # 'actual' nodes that are added using 'put' operations.
        # head --> The least recently used node. This would be deleted in case capacity is 
        # going to exceed the defined limit.
        # tail --> The most recently used node. 
        # left --> Points to the last 'actual' node in the LinkedList that was added only 
        # using 'put' operation. Technically tail would be the last node each time.
        self.cache = dict()
        self.head, self.tail = Node(), Node()
        self.left = self.head
        self.rem_capacity = capacity

    # Function for inserting a node just before tail. 
    def insert_node(self, new_node:'Node') -> None:
        new_node.prev = self.left
        self.left.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node
        # The newly added node would be the 'last' actual node. So make left point to it.
        self.left = self.left.next

    # Function for removing any node between head and tail and connecting it's left and right
    # neighbours directly.
    def remove_node(self, target:'Node') -> None:
        # If the node to be removed is the most recently used node, then before removing it,
        # mark the node just before it as the most recently used (by making left point to it).
        if self.left == target:
            self.left = target.prev
        after_target = target.next
        before_target = target.prev
        before_target.next = after_target
        after_target.prev = before_target
        target.next, target.prev = None, None

    def get(self, key: int) -> int:
        if key in self.cache:
            target = self.cache[key]
            # Check if the target node is already just before the tail. If it is, no changes are    
            # required. If it isn't, remove it from the list and add it back just before the tail.
            if target.next.key != -1:
                self.remove_node(target)
                self.insert_node(target)
            return target.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Case 1: Key exists. So new dict entry & new node don't need to be created.
        if key in self.cache:
            # Update the value of given key in the dictionary.
            target = self.cache[key]
            target.val = value
            # Remove the target node and add it back to the end of the list (just before tail), 
            # making it the most recently used node (Do all this only if it's next node isn't tail).
            if target.next.key != -1:
                self.remove_node(target)
                self.insert_node(target)

        # Case 2: Key exists. So new dict entry & new node need to be created.
        else:
            # Case 2a: Capacity is available for adding a new node
            if self.rem_capacity:
                new_node = Node(key, value)
                self.insert_node(new_node)
                self.rem_capacity -= 1
                self.cache[key] = new_node
            # Case 2b: Capacity isn't available for adding a new node. So we need to remove the 
            # least recently used node (the node right after the dummy head).
            else:
                target = self.head.next
                self.remove_node(target)
                del self.cache[target.key]
                self.rem_capacity += 1

                new_node = Node(key, value)
                self.insert_node(new_node)
                self.rem_capacity -= 1
                self.cache[key] = new_node
      
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
