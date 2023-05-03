class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data
    
class Stack:

    def __repr__(self):
        return self.print()

    def __init__(self, headData = None):

        self.baseValue = None
        
        if headData is None:
            self.front = None
        else:
            self.front = Node(headData)
            self.baseValue = headData
        
    def push(self, data):
        new_node = Node(data)
        if self.front is not None:
            new_node.next = self.front
        self.front = new_node
            
        
        
    def pop(self):
        if self.front is None or self.front is self.baseValue:
            self.front = self.baseValue
            return None #list empty
        removed = self.front
        self.front = self.front.next
        if self.front is None:
            self.front = self.baseValue

        
        return removed
    
    def peek(self):
        if not self.front:
            return self.front
        return self.front.data
    
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
        return display_text

    def get_front(self): 
        return self.front

    @staticmethod
    def copyStack(stackToCopy):
        #get stack info
        data_list = []
        cur_node = stackToCopy.get_front()
        while cur_node is not None:
            #dostuff
            data_list.insert(0,cur_node.data)
            cur_node = cur_node.get_next()
        
        #make new stack

        newStack = Stack(headData = '')
        for dat in data_list:
            newStack.push(dat)

        return newStack


def test():
    stack = Stack('')
    if stack.peek():
        print('peeked')
    stack.push('a')
    stack.push('b')
    stack.push('c')
    print('first stack')
    stack.print()

    newstack = Stack.copyStack(stack)
    print('next stack')
    newstack.print()
    print('\n')
    print('adding stuff to old stack')
    stack.push('Iaddedthis')
    stack.print()
    print('and the new stack remains unchanged:')
    newstack.print()

if __name__ == "__main__":
    test()