import math

from lab_python_oop.color import FigureColor
from lab_python_oop.figure import Figure


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius, color):
        self.radius = radius
        self.figure_color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{} {} цвета: радиус {}, площадь {:.2f}".format(
            self.get_figure_type(),
            self.figure_color.color,
            self.radius,
            self.area(),
        )
