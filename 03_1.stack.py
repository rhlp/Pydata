class Stack(object):
    """栈"""

    def __init__(self):
        '''创建一个新的空栈'''
        self.item = []

    def push(self, item):
        '''添加一个新的元素item到栈顶'''
        self.item.append(item)

    def pop(self):
        '''弹出栈顶元素'''
        return self.item.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self.item[self.size()-1]

    def is_empty(self):
        '''判断栈是都为空'''
        return self.item == []

    def size(self):
        '''返回栈的元素个数'''
        return len(self.item)

if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.is_empty())
    print(stack.size())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())