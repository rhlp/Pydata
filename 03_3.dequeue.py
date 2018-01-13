class Deque(object):
    '''双端队列'''

    def __init__(self):
        '''创建一个空的双端队列'''
        self.items = []

    def add_front(self, item):
        '''从对头加入一个item元素'''
        self.items.append(item)

    def add_rear(self, item):
        '''从队尾加入一个元素'''
        self.items.append(item)

    def remove_front(self):
        '''从对头删除一个元素'''
        return self.items.pop(0)

    def remove_rear(self):
        '''从队尾删除一个元素'''
        return self.items.pop()

    def is_empty(self):
        '''判断双端队列是否为空'''
        return self.items == []

    def size(self):
        '''返回队列的大小'''
        return len(self.items)

if __name__ == '__main__':
    deque = Deque()

    # 当成栈使用
    # deque.add_rear(1)
    # deque.add_rear(2)
    # deque.add_rear(3)
    #
    # print(deque.remove_rear())
    # print(deque.remove_rear())
    # print(deque.remove_rear())

    # 当成队列使用
    # deque.add_rear(1)
    # deque.add_rear(2)
    # deque.add_rear(3)
    #
    # print(deque.remove_front())
    # print(deque.remove_front())
    # print(deque.remove_front())

    deque.add_front(1)
    deque.add_front(2)
    deque.add_front(3)

    print(deque.remove_rear())
    print(deque.remove_rear())
    print(deque.remove_rear())