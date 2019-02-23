# coding:utf-8
# @Time : 2019/2/23 20:50 
# @Author : Andy.Zhang
# @Desc : Binary Search Tree 二叉查找树，有空研究一下红黑树以及 mysql 索引使用的 B-Tree 结构(多路平衡查找树) todo


class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}

        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, value=key)  # 这里暂时用和key一样的

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1

        return cls(root)

    def _bst_search(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node:
            return node.value
        else:
            return default

    def __contains__(self, key):
        """实现 in 操作符"""
        return self._bst_search(self.root, key) is not None

    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:  # 已到左子树的尽头
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def bst_max(self):
        pass  # todo

    def _bst_insert(self, subtree, key, value):  # 每次插入都相当个叶子节点
        """
        插入并返回subtree(根)节点，如果subtree为None的话，那么插入的就是根节点，如果 key<subtree.key则往左节点里面递归插入，否则往右节点里递归插入
        :param subtree:
        :param key:
        :param value:
        :return:
        """
        if subtree is None:  # 插入的节点一定是根节点，包括 root 为空的情况
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)

        return subtree

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node:
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    def _bst_remove(self, subtree, key):
        """删除节点并返回subtree(根)节点"""
        if subtree is None:
            return None
        elif key < subtree.key:  # 如果subtree不是要删除的节点，并且要删除的节点比其小，则往左边递归寻找并删除
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:  # 如果subtree不是要删除的节点，并且要删除的节点比其大，则往右边递归寻找并删除
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        else:  # 找到了要删除的节点
            if subtree.left is None and subtree.right is None:  # 叶节点，返回None，并把其父节点指向它的指针重新设置为 None
                return None  # 递归调用出口，其上一个调用的栈会自动接收返回的None值，并赋值到 subtree.left或subtree.right中
                # 所以这里 return None 相当于把其父节点指向它的指针重新行置为了 None
            elif subtree.left is None or subtree.right is None:  # 只有一个孩子的节点
                if subtree.left is not None:  # 只有一个左孩子节点
                    return subtree.left  # 返回它的孩子并让它的父亲指过去
                    # (因为到运行到这里来，毕竟是它的父亲node递归调用它，所以这个值会返回给它的父亲
                else:  # 只有一个右孩子节点
                    return subtree.right
            else:  # 两个孩子，寻找后继节点替换，并删除其右子树的后继节点，同时更新其右子树
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(subtree.right, successor_node.key)
                # 理解上面这行代码非常重要，因为后续节点是在其right子树中找到的，所以需要在其 right 子树中删除掉，
                # 相当于删掉的同时也一层层栈递归调用更新整个右子树，并最后一层返回的结果肯定是右子树的最root的节点
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1  # 能执行到这一步，说明上一步不会报错(in 操作不会是 False，如果 assert False，那么assert后面的语句就不会执行了）
        self._bst_remove(self.root, key)


NODE_LIST = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
]


def test_bst_tree():
    bst = BST.build_from(NODE_LIST)
    for node_dict in NODE_LIST:
        key = node_dict['key']
        assert bst.get(key) == key

    assert bst.size == len(NODE_LIST)
    assert bst.get(-1) is None
    assert bst.bst_min() == 1
    bst.add(0, 0)
    assert bst.bst_min() == 0

    bst.remove(12)
    assert bst.get(12) is None

    bst.remove(1)
    assert bst.get(1) is None

    bst.remove(29)
    assert bst.get(29) is None

    assert bst.size == len(NODE_LIST) + 1 - 3


if __name__ == '__main__':
    test_bst_tree()