# coding:utf-8
# @Time : 2019/2/23 19:38 
# @Author : Andy.Zhang
# @Desc : 基于 maxheap 最大实现的优先级对列


import sys
sys.path.append('../15_heap')
from heap_and_heapsort import MaxHeap


class PriorityQueue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        entry = (priority, value)  # push a tuple
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry  # return a tuple
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    # TDD
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())

    assert res == ['purple', 'orange', 'black', 'white']