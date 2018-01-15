class Node(object):
    '''二叉树节点'''
    def __init__(self, item):
        self.item = item
        self.lChild = None
        self.rChild = None

class Tree(object):
    '''完全二叉树'''

    def __init__(self):
        self.__root = None


    def add(self, item):
        '''添加节点'''
        node = Node(item)
        # 是否为空
        if self.__root is None:
            self.__root = node
        else:
            # 从上到下，从左到右，添加节点
            #使用队列
            queue = []
            queue.append(self.__root)

            while queue:
                child = queue.pop(0)
                if child.lChild is None:
                    child.lChild = node
                    return

                if child.rChild is None:
                    child.rChild = node
                    return
                queue.append(child.lChild)
                queue.append(child.rChild)

    def depth_travel(self):
        '''深度优先遍历'''
        self.post_order(self.__root)

    def post_order(self, node):
        '''后续'''
        if node is None:
            return
        self.post_order(node.lChild)
        self.post_order(node.rChild)
        print(node.item, end=" ")

    def in_order(self, node):
        '''中序'''
        if node is None:
            return
        self.in_order(node.lChild)
        print(node.item, end=" ")
        self.in_order(node.rChild)

    def pre_order(self, node):
        '''先序'''
        if node is None:
            return
        print(node.item, end=" ")
        self.pre_order(node.lChild)
        self.pre_order(node.rChild)

    def breath_travel(self):
        '''广度优先遍历，从上到下，从左到右，用 队列'''
        if self.__root is None:
            return
        else:
            queue = []
            queue.append(self.__root)

            while queue:
                node = queue.pop(0)
                print(node.item, end=" ")

                if node.lChild is not None:
                    queue.append(node.lChild)
                if node.rChild is not None:
                    queue.append(node.rChild)

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    # tree.breath_travel()
    tree.depth_travel()





