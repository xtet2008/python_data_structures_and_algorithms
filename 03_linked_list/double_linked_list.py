# coding:utf-8
# @Time : 2019/2/17 17:57 
# @Author : Andy.Zhang
# @Desc : double linked list 循环双端节点


class Node(object):
    __slots__ = ('value', 'prev', 'next')  # save memory

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    '''
    循环双端表 ADT
    多了个循环其实就是把 root.prev 指向tail节点，串起来
    '''

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):  # O(1)，一般不用 for 循环的就是 O(1)，有限个步骤
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is full')

        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev, node.next = tailnode, self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is full')

        node = Node(value=value)
        if self.root.next is self.root:  # 如果是空链表的话
            node.prev, node.next = self.root, self.root
            self.root.prev, self.root.next = node, node
        else:
            headnode = self.root.next
            node.prev, node.next = self.root, headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node): # O(1), node is not value
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next # 获取头节点
        while curnode.next is not self.root:  # 非尾节点的情况下循环抛出
            yield curnode
            curnode = curnode.next
        yield curnode  # 最后还得把最后的 tailnode 抛出来，因为上面的 while 到 tailnode的时候不满足继续循环条件（不会执行while里面抛出）

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        '''
        相比单链表独有的反序遍历功能
        :return:
        '''
        if self.root.prev is self.root:
            return
        curnode = self.root.prev  # tailnode
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


def test_double_linked_list():
    dll = CircularDoubleLinkedList()
    assert len(dll) == 0

    dll.append('a')
    dll.append('b')
    dll.append('c')
    dll.append('d')

    assert list(dll) == ['a', 'b', 'c', 'd']
    assert [node.value for node in dll.iter_node()] == ['a', 'b', 'c', 'd']
    assert [node.value for node in dll.iter_node_reverse()] == ['d', 'c', 'b', 'a']

    headone = dll.headnode()
    assert headone.value == 'a'
    dll.remove(headone)
    assert len(dll) == 3
    assert [node.value for node in dll.iter_node()] == ['b', 'c', 'd']

    dll.appendleft('a')
    assert [node.value for node in dll.iter_node()] == ['a', 'b', 'c', 'd']
