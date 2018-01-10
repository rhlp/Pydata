class Node(object):
    """单循环链表节点"""
    def __init__(self, item):
        """初始化"""
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单循环链表类"""

    def __init__(self):
        """初始化首节点"""
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        # 判断首节点是否为空
        return self.__head is None

    def length(self):
        """链表长度"""
        # 判断链表是否为空
        if self.is_empty():
            return 0
        # 遍历统计
        cur = self.__head
        # 定义count，记录个数
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        # 判断链表是否为空
        if self.is_empty():
            return
        # 从头节点开始遍历
        # 定义游标变量
        cur = self.__head
        print(cur.item, end=" ")
        # 把第二个节点到尾节点输出
        while cur.next is not self.__head:
            cur = cur.next
            print(cur.item, end=" ")
        print()

    def add(self, item):
        """链表头部添加元素"""
        # 把传递进来的item创建一个节点
        node = Node(item)
        # 判断链表是否为空
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return

        # 遍历找到尾节点
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        # 循环结束，cur指向的是尾节点
        node.next = self.__head
        self.__head = node
        # 让尾节点指向新的头节点
        cur.next = self.__head

    def append(self, item):
        """链表尾部添加元素"""
        # 判断链表是否为空
        if self.is_empty():
            self.add(item)
            return
        # 遍历找到尾节点
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        # 当循环结束时，cur指向的是尾节点
        node = Node(item)
        cur.next = node
        # 让新节点指向头节点
        node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 根据传入的pos，找到前一个节点
            cur = self.__head
            # 定义index，记录下标
            index = 0
            while index < (pos - 1):
                index += 1
                cur = cur.next
            # 当循环结束，cur指向的就是pos前面的节点
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        # 判断链表是否为空
        if self.is_empty():
            return
        # 需要遍历找要删除的节点的前一个节点
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            # 判断当前节点是否是要删除的节点
            if cur.item == item:
                # 如果pre为空，证明删除的是头节点
                if pre is None:
                    # 需要找到尾节点，让尾节点指向新的头节点
                    temp = self.__head
                    while temp.next is not self.__head:
                        temp = temp.next
                    # 循环结束，temp指向尾节点
                    self.__head = cur.next
                    temp.next = self.__head

                else:
                    pre.next = cur.next

            pre = cur
            cur = cur.next
        # 循环里面只能判断第一个节点到到手第二个节点，判断不了最后一个节点
        # 循环结束后，cur指向的是尾节点
        if cur.item == item:
            # 如果pre为空，证明链表只有一个节点，删除的是头节点
            if pre is None:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        """查找节点是否存在"""
        # 判断链表是否为空
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next is not self.__head:
            # 判断当前节点是否是要找的节点
            cur = cur.next
            if cur.item == item:
                return True
        # 循环结束还没有找到
        return False

if __name__ == '__main__':

    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.add(5)
    sll.add(3)
    sll.add(2)
    print(sll.is_empty())
    sll.travel()
    print(sll.length())

    sll.append(1)
    sll.travel()

    sll.insert(2, 4)
    sll.travel()
    sll.insert(-10, 6)
    sll.travel()
    sll.insert(10, 7)
    sll.travel()

    sll.remove(6)
    sll.travel()
    sll.remove(3)
    sll.travel()
    sll.remove(7)
    sll.travel()

    print(sll.search(2))
    print(sll.search(1))
    print(sll.search(3))

