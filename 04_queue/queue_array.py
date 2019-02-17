# coding:utf-8
# @Time : 2019/2/17 20:42
# @Author : Andy.Zhang
# @Desc : queue 队列（用数组array方式实现）


from collections import deque
import sys
sys.path.append('../02_array_and_list_line_structure')
from array_and_list import Array


######################################################
# 下边是 Queue 实现 (基于之前实现的数组Array)
######################################################


class FullError(Exception):
    pass


class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head, self.tail = 0, 0  # 头和尾的位置

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


def test_array_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)
    assert list(q.array) == [0, 1, 2, 3, 4]

    with pytest.raises(FullError) as excinfo:
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == size
    assert q.pop() == 0
    assert q.pop() == 1

    q.push(5)
    assert len(q) == 4

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0