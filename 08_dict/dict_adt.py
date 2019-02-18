# coding:utf-8
# @Time : 2019/2/18 16:16 
# @Author : Andy.Zhang
# @Desc : 创建字典 dict (继承前面的hash_table)


import sys
sys.path.append('../07_hash')
from hash_table import HashTable


######################################################
# 下边是实现 dict 抽象数据类型，继承了之前的 hash_table
######################################################
class DictADT(HashTable):
    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):  # 需要判断是否有意义的槽（非删除的槽并且还不能是未使用的槽)
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)

    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)