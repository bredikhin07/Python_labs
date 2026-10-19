import math
import unittest

from lab_python_oop.circle import Circle
from lab_python_oop.color import FigureColor
from lab_python_oop.figure import Figure
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


class FigureTests(unittest.TestCase):
    def test_abstract_figure_cannot_be_created(self):
        with self.assertRaises(TypeError):
            Figure()

    def test_color_property(self):
        color = FigureColor("синего")
        self.assertEqual(color.color, "синего")
        color.color = "красного"
        self.assertEqual(color.color, "красного")

    def test_rectangle(self):
        rectangle = Rectangle(3, 4, "синего")
        self.assertEqual(rectangle.area(), 12)
        self.assertEqual(rectangle.get_figure_type(), "Прямоугольник")
        self.assertEqual(
            repr(rectangle),
            "Прямоугольник синего цвета: ширина 3, высота 4, площадь 12.00",
        )

    def test_circle(self):
        circle = Circle(3, "зеленого")
        self.assertTrue(math.isclose(circle.area(), 9 * math.pi))
        self.assertEqual(circle.get_figure_type(), "Круг")
        self.assertIn("радиус 3", repr(circle))
        self.assertIn("площадь 28.27", repr(circle))

    def test_square_inherits_rectangle(self):
        square = Square(3, "красного")
        self.assertIsInstance(square, Rectangle)
        self.assertEqual((square.width, square.height), (3, 3))
        self.assertEqual(square.area(), 9)
        self.assertEqual(square.get_figure_type(), "Квадрат")
        self.assertEqual(
            repr(square),
            "Квадрат красного цвета: сторона 3, площадь 9.00",
        )


if __name__ == "__main__":
    unittest.main()
