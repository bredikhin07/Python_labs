"""Итератор, пропускающий уже встречавшиеся значения."""


class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = []

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            comparison_value = item.casefold() if self.ignore_case and isinstance(item, str) else item
            if comparison_value not in self.seen:
                self.seen.append(comparison_value)
                return item
        raise StopIteration


if __name__ == '__main__':
    try:
        from .gen_random import gen_random
    except ImportError:
        from gen_random import gen_random

    print(list(Unique([1, 1, 1, 2, 2])))
    print(list(Unique(gen_random(10, 1, 3))))
    letters = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(letters)))
    print(list(Unique(letters, ignore_case=True)))
