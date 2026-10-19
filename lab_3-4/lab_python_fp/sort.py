"""Сортировка чисел по убыванию абсолютного значения."""

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]


if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda number: abs(number), reverse=True)
    print(result_with_lambda)
