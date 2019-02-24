# coding:utf-8
# @Time : 2019/2/24 14:37 
# @Author : Andy.Zhang
# @Desc : graph 图与图的遍历

from collections import deque
import sys
sys.path.append('../05_stack')
from stack_structure import Stack


GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    """广度优先搜索，使用queue对列，先进邻居，再先出邻居方式"""
    search_queue = Queue()
    search_queue.push(start)
    searched = set()
    while search_queue:  # 队列不为空就继续
        cur_node = search_queue.pop()
        if cur_node not in searched:
            yield cur_node
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.push(node)


DFS_SEARCHED = set()


def dfs(graph, start):
    """深度优先搜索，使用递归方式一直访问其邻居"""
    if start not in DFS_SEARCHED:
        yield start
        DFS_SEARCHED.add(start)

    for node in graph[start]:
        if node not in DFS_SEARCHED:
            yield from dfs(graph, node)


def dfs_use_stack(graph, start):
    """深度优先搜索，使用栈，先进后出(后进先出)"""
    stack = Stack()
    stack.push(start)
    searched = set()
    while stack:
        cur_node = stack.pop()
        if cur_node not in searched:
            yield cur_node
            searched.add(cur_node)
            # 思考一下这里为什么加 reversed, 不加也是可以的
            for node in reversed(graph[cur_node]):  # 因为先进后出，为了先弹出左领导，再出右邻居，所以加个 reversed把左右顺序调换
                stack.push(node)


def test_graph_search():
    assert list(bfs(GRAPH, 'A')) == ['A', 'B', 'F', 'C', 'I', 'G', 'E', 'D', 'H']
    assert list(dfs(GRAPH, 'A')) == ['A', 'B', 'C', 'I', 'D', 'G', 'F', 'E', 'H']
    assert list(dfs_use_stack(GRAPH, 'A')) == ['A', 'B', 'C', 'I', 'D', 'G', 'F', 'E', 'H']


if __name__ == '__main__':
    test_graph_search()