# -*- coding:utf-8 -*-

class Node(object):
    '''单链表节点'''
    def __init__(self, item):
        '''初始化'''
        self.item = item
        self.next = None

class SingleLinkList(object):
    '''单链表类'''

    def __init__(self):
        '''初始化首节点'''
        self.__head = None

    def is_empty(self):
        '''链表是否为空'''
        # 判断首节点是否为空
        return self.__head is None

    def length(self):
        '''链表长度'''
        # 遍历统计
        cur = self.__head
        # 定义count记录个数
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        # 从头节点开始遍历
        # 定义游标变量
        cur = self.__head
        while cur is not None:
            print(cur.item, end="")
            cur = cur.next
        print()

    def add(self, item):
        '''链表头部添加元素'''
        # 把传递进来的item创建一个节点
        node = Node(item)
        # 让新节点的next指向老的头节点
        node.next = self.__head

        # 让head指向新的头节点
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素'''
        # 判断链表是否为空
        if self.is_empty():
            self.add(item)
            return

        # 遍历找到尾节点
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        # 当循环结束时，cur指向的是尾节点
        node = Node(item)
        cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <=0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 根据传入的pos，找到前一个节点
            cur = self.__head
            # 定义index， 记录下标
            index = 0
            while index < (pos - 1):
                index += 1
                cur = cur.next
            # 当循环结束，cur指向的就是pos前面的节点
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        '''删除节点'''
        # 需要遍历找到要删除的节点的前一个节点
        cur = self.__head
        pre = None
        while cur is not None:
            # 判断当前节点是否是要删除的节点
            if cur.item == item:
                if pre is None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next

            pre = cur
            cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''

        cur = self.__head
        while cur is not None:
            # 判断当前节点是否是要找遍历整个链表的节点
            if cur.item == item:
                return True
            cur = cur.next
        # 循环结束还没找到
        return False


    # append(item)
    # 链表尾部添加元素
    # insert(pos, item)
    # 指定位置添加元素
    # remove(item)
    # 删除节点
    # search(item)
    # 查找节点是否存在


if __name__ == '__main__':

    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.add(7)
    sll.add(4)
    sll.add(3)
    print(sll.is_empty())
    sll.travel()
    print(sll.length())

    sll.append(8)
    sll.travel()

    sll.insert(2,5)
    sll.travel()
    sll.insert(-10, 2)
    sll.travel()
    sll.insert(10, 9)
    sll.travel()

    sll.remove(5)
    sll.travel()
    sll.remove(9)
    sll.travel()

    print(sll.search(3))
    print(sll.search(7))
    print(sll.search(9))




