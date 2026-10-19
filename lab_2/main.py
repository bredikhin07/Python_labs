from pyfiglet import Figlet

from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


def main():
    print(Figlet(font="small").renderText("LAB 2"), end="")

    figures = [
        Rectangle(3, 3, "синего"),
        Circle(3, "зеленого"),
        Square(3, "красного"),
    ]
    for figure in figures:
        print(repr(figure))


if __name__ == "__main__":
    main()
