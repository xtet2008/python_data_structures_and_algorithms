# coding:utf-8
# @Time : 2019/2/17 22:04 
# @Author : Andy.Zhang
# @Desc : 栈

import sys
sys.path.append('../03_linked_list')
from double_linked_list import CircularDoubleLinkedList


######################################################
# 下边是 栈 实现 (基于之前实现的循环双链表 CircularDoubleLinkedList)
######################################################

class Deque(CircularDoubleLinkedList):
    def pop(self):
        if len(self) == 0:
            raise Exception('empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)


class Stack:
    def __init__(self):
        self.deque = Deque()  # collections.Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack()
    for i in range(3):
        s.push(i)

    assert len(s) == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0
    assert s.is_empty()

    import pytest
    with pytest.raises(Exception) as excinfo:
        s.pop()
    assert 'empty' in str(excinfo.value)