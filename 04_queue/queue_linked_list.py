# coding:utf-8
# @Time : 2019/2/17 19:56 
# @Author : Andy.Zhang
# @Desc : queue 队列


from collections import deque
import sys
sys.path.append('../03_linked_list')
from linked_list import Node, LinkedList


######################################################
# 下边是 Queue 实现 (基于之前实现的单链表)
######################################################

class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError('queue full')
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) == 0:
            raise EmptyError('queue empty')
        return self._item_linked_list.popleft()


def test_queue():
    q = Queue()
    q.push('a')
    q.push('b')
    q.push('c')

    assert len(q) == 3
    assert q.pop() == 'a'
    assert q.pop() == 'b'
    assert q.pop() == 'c'

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        q.pop()  # raise EmptyError
    assert 'empty' in str(excinfo.value)


class MyQueue:
    """
    使用 collections.deque 可以讯速实现一个队列
    """
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def isempty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]


def test_myqueue():
    myqueue = MyQueue()
    myqueue.append('a')
    myqueue.append('b')
    myqueue.append('c')
    myqueue.append('d')

    assert len(myqueue) == 4
    assert myqueue.pop() == 'a'
    assert myqueue.front() == 'b'
    assert len(myqueue) == 3

    assert myqueue.isempty() is False
    assert myqueue.pop() == 'b'
    assert myqueue.pop() == 'c'
    assert myqueue.pop() == 'd'
    assert myqueue.isempty() is True
