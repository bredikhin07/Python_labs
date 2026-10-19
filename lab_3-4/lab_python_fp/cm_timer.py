"""Контекстные менеджеры для измерения времени выполнения блока."""

from contextlib import contextmanager
from time import perf_counter, sleep


class cm_timer_1:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'time: {perf_counter() - self.start:.3f}')


@contextmanager
def cm_timer_2():
    start = perf_counter()
    try:
        yield
    finally:
        print(f'time: {perf_counter() - start:.3f}')


if __name__ == '__main__':
    with cm_timer_1():
        sleep(1)
    with cm_timer_2():
        sleep(1)
