

# Итератор для удаления дубликатов
class Unique(object):
    _lst = []
    _new_lst = []
    _index = -1

    def __init__(self, items, ignore_case):
        assert len(items) > 0   # выход
        self._lst = list(items)
        if ignore_case & isinstance(self._lst[0], str):
            self._lst.sort(key=lambda st: st.lower())
        else:
            self._lst.sort()
        self._new_lst = []
        cur_in = 0
        self._new_lst.append(self._lst[0])
        for x in self._lst:
            if(ignore_case & isinstance(self._lst[0], str)):
                if(x.lower() != self._new_lst[cur_in].lower()):
                    self._new_lst.append(x)
                    cur_in += 1
            else:
                if(x != self._new_lst[cur_in]):
                    self._new_lst.append(x)
                    cur_in += 1
        self._index = -1

    def __next__(self):
        if self._index >= len(self._new_lst)-1:
            raise StopIteration
        self._index += 1
        return self._new_lst[self._index];

    def __iter__(self):
        return self
