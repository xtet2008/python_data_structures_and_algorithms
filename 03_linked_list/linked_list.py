# coding:utf-8
# 单链表


class Node(object):
    def __init__(self, value=None, next=None):  # 这里我们 root 节点默认都是 None，所以给了默认值
        self.value = value
        self.next = next

    def __str__(self):
        # 为了方打印出来高度，复杂的代码可能需要断点高度
        return '<Node: value: {}, next={}'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    ''' 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    '''

    def __init__(self, maxsize=None):
        '''
        :param maxsize: int or None, 如果是 None, 无限扩充
        '''
        self.maxsize = maxsize
        self.root = Node()  # 默认 root 节点指向 None
        self.tailnode = None  # 默认尾节点也是 None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):  # O(1) 从右边尾端添加节点
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)  # 构造节点
        tailnode = self.tailnode
        if tailnode is None:  # 还没有append过，length = 0，追加到 root后
            self.root.next = node
        else:  # 否则追加到最后一个节点的后边，并更新最后一个节点是 append 的节点
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:  # 如果原链表为空，插入第一个元素需要设置 tailnode
            self.tailnode = node

        headnode = self.root.next  # self.root.next永远保存着链表目前在插入新节点为止 的第一个节点
        self.root.next = node  # 第一个节点改为当前节点
        node.next = headnode  # 当前节点的下一个节点指向在插入当前节点之前的第一个节点
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        '''遍历从 head节点到 tail节点'''
        curnode = self.root.next
        while curnode is not None:
            yield curnode
            curnode = curnode.next
        if False:
            while curnode is not self.tailnode:  # 从第一个节点开始遍历
                yield curnode
                curnode = curnode.next  # 移动到下一个节点

            if curnode is not None:
                yield curnode

    def remove (self, value):  # O(n)
        '''
        删除包含值的一个节点，将期前一个节点的 next 指向被查询/删除到的节点的下一个节点即可
        :param value:
        '''
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:  # NOTE: 注意更新 tailnode
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:
                prevnode = curnode
        return -1  # 表明删除失败

    def find(self, value):  # O(n)
        '''
        查找一个节点，返回序号，从0开始
        :param value:
        :return:
        '''
        index = 0
        for node in self.iter_node():  # 我们定义了 __iter__，这里就可以用 for遍历它了
            if node.value == value:
                return index
            index += 1
        return -1  # 没找着

    def popleft(self):
        '''删除第一个节点'''
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:  # 增加删除 tailnode 处理，假如只有一个节点的情况下，即是头节点，又同时是尾节点
            self.tailnode = None
        del headnode
        return value  # 返回节点值

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None  # 头节点
        self.length = 0
        self.tailnode = None  # 尾节点

    def reverse(self):
        '''
        返回链表
        :return:
        '''
        curnode = self.root.next  # 头节点
        self.tailnode = curnode  # 刻更新 tailnode，多了这个属性处理起来经常忘记？
        prevnode = None

        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode

            if nextnode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextnode


def test_linked_list():
    ll = LinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')
    ll.append('d')

    assert len(ll) == 4
    assert ll.find("c") == 2
    assert ll.find(-1) == -1

    assert ll.remove('a') == 1
    assert ll.remove(10) == -1
    assert ll.remove('c') == 1
    assert len(ll) == 2
    assert list(ll) == ['b', 'd']
    assert ll.find('a') == -1

    ll.appendleft('a')
    assert list(ll) == ['a', 'b', 'd']
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 'a'
    assert len(ll) == 2
    assert list(ll) == ['b', 'd']

    assert ll.popleft() == 'b'
    assert list(ll) == ['d']
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    print(list(ll))


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    ll.appendleft(3)
    assert list(ll) == [3, 1, 2]


if __name__ == '__main__':
    test_linked_list()
    test_linked_list_append()
    test_linked_list_remove()
    test_linked_list_reverse()
