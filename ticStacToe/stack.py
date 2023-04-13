class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.front = None
        
    def push(self, data):
        new_node = Node(data)
        if self.front is not None:
            new_node.next = self.front
        self.front = new_node
            
        
        
    def pop(self):
        if self.front is None:
            return False #list empty
        
        self.front = self.front.next
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
            

        print(display_text)


def test():
    stack = Stack()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.print()
    stack.pop()
    stack.print()
    stack.push('hi')
    stack.print()
    stack.pop()
    stack.pop()
    stack.print()
    stack.pop()
    stack.print()
    stack.pop()

if __name__ == "__main__":
    test()