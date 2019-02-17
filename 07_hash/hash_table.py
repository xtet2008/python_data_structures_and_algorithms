# coding:utf-8
# @Time : 2019/2/17 23:36 
# @Author : Andy.Zhang
# @Desc : 实现一个Hash表（基于之前实现的 Array）


######################################################
# 下边是之前实现的 数组 Array，稍做修改，加了个 init初始化值
######################################################
class Array(object):
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class Slot(object):
    """
    定义一个hash表数组的槽
    一个槽有3种状态。 相比链接法解决冲突，二次探查次删除一个key的操作微信复杂。
    1、从未使用 HashMap.UnUsed，此槽没有被使用和冲突过，查找时只要找到 UnUsed 就不用再继续探查了
    2、使用过但是 remove了，此时 HashMap.Empty，该探查点后边的元素仍可能是有key
    3、槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None  # slot 没被使用过
    EMPTY = Slot(None, None)  # 使用过但被删除了

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0  # 已使用槽的数量

    @property
    def _load_factor(self):  # 装载因子
        return self.length / float(len(self._table))  # 哈希表中已使用的槽数/总槽数

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):  # 寻找key（槽）的位置
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:  # 如果这个槽有使用过的话，找下去才有意义(if UNUSED没使用过说明key不存在)
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1) % _len  # 使用 cpython的一种解决哈希冲突的方式，寻找下一个槽的位置
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5 + 1) % _len
        return None  # 如果什么都没有找着的话，返回 None

    def _slot_can_inserted(self, index):  # 判断该槽能否被插入（只有UNUSED未被使用过的空槽或EMPTY使用过但已删除的槽才可以被插入)
        return self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED

    def _find_slot_for_insert(self, key):  # 找到下一个可插入的 空槽 位置
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_inserted(index):
            index = (index*5 + 1) % _len
        return index

    def __contains__(self, key):  # in operator 实现 in 操作符
        return self._find_key(key) is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1

            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key


def test_hash_table():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)
    assert len(h) == 3
    assert h.get('a') == 0
    assert h.get('b') == 1
    assert h.get('asdf') is None

    h.remove('a')
    assert h.get('a') is None
    assert sorted(list(h)) == ['b', 'c']

    n = 50
    for i in range(n):
        h.add(i, i)

    for i in range(n):
        assert h.get(i) == i


if __name__ == '__main__':
    test_hash_table()