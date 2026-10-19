from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        self.side = side
        super().__init__(side, side, color)

    def __repr__(self):
        return "{} {} цвета: сторона {}, площадь {:.2f}".format(
            self.get_figure_type(),
            self.figure_color.color,
            self.side,
            self.area(),
        )
