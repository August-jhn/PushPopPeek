class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.front = None
        
    def push(self, data):
        new_node = Node(data)
        if self.front is None:
            new_node.next = self.front.next
        self.front = new_node
        
    def pop(self):
        if self.front is None:
            return False #list empty
        else:
            self.front.next = self.front
        return True
    
    def peek(self):
        return self.front
    
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def print(self):
        cur_node = self.front
        display_text = ""
        while cur_node is not None:
            display_text += "{data} ".format(data = cur_node.data)
            cur_node = cur_node.next
