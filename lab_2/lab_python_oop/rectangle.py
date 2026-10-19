from lab_python_oop.color import FigureColor
from lab_python_oop.figure import Figure


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.figure_color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета: ширина {}, высота {}, площадь {:.2f}".format(
            self.get_figure_type(),
            self.figure_color.color,
            self.width,
            self.height,
            self.area(),
        )
