import sys
import math


def get_coefficient(name, arg_value=None):
    """
    Возвращает корректное действительное значение коэффициента.
    Если передан аргумент командной строки и он корректен - использует его.
    Иначе запрашивает значение с клавиатуры до тех пор, пока оно не станет корректным.
    """
    if arg_value is not None:
        try:
            return float(arg_value.replace(',', '.'))
        except ValueError:
            print(f"Некорректное значение коэффициента {name} "
                  f"в командной строке: '{arg_value}'. Введите его вручную.")

    while True:
        raw = input(f"Введите коэффициент {name}: ").strip()
        try:
            return float(raw.replace(',', '.'))
        except ValueError:
            print(f"Ошибка: '{raw}' не является действительным числом. "
                  f"Повторите ввод.")


def solve_biquadratic(A, B, C):
    """
    Решает A*x^4 + B*x^2 + C = 0.
    Возвращает список действительных корней (без дубликатов, по возрастанию).
    """
    roots = []

    # Вырожденные случаи, когда A = 0
    if A == 0:
        if B == 0:
            # C = 0 -> любое x; C != 0 -> нет решений
            return None if C == 0 else []
        y = -C / B
        if y >= 0:
            r = math.sqrt(y)
            roots.extend([-r, r])
        return sorted(set(roots))

    # Основной случай: квадратное уравнение относительно y = x^2
    D = B * B - 4 * A * C
    print(f"Дискриминант D = {D}")

    if D < 0:
        return []
    elif D == 0:
        y = -B / (2 * A)
        if y >= 0:
            r = math.sqrt(y)
            roots.extend([-r, r])
    else:
        sqrt_D = math.sqrt(D)
        for y in ((-B + sqrt_D) / (2 * A), (-B - sqrt_D) / (2 * A)):
            if y >= 0:
                r = math.sqrt(y)
                roots.extend([-r, r])

    return sorted(set(roots))


def main():
    args = sys.argv[1:]

    # Аргумент из командной строки передаётся, если он есть; иначе None
    A = get_coefficient('A', args[0] if len(args) > 0 else None)
    B = get_coefficient('B', args[1] if len(args) > 1 else None)
    C = get_coefficient('C', args[2] if len(args) > 2 else None)

    print(f"\nУравнение: ({A})·x^4 + ({B})·x^2 + ({C}) = 0")

    roots = solve_biquadratic(A, B, C)

    if roots is None:
        print("Уравнение имеет бесконечно много решений (x — любое).")
    elif not roots:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")
        for r in roots:
            print(f"  x = {r}")


if __name__ == "__main__":
    main()