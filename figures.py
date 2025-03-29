from abc import ABC, abstractmethod
pi = 3.1415926535
class Figure(ABC):
    @abstractmethod
    def calculate_square(self):
        pass
class Square(Figure):
    def __init__(self, a):
        self.a = a
    def calculate_square(self):
        return self.a ** 2
class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def calculate_square(self):
        return pi * self.r ** 2
class Triangle(Figure):
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def calculate_square(self):
        return self.a * self.h / 2
class FigureFactory:
    @staticmethod
    def create_figure(figure_type):
        if figure_type == "square":
            a = int(input("Введите сторону: "))
            return Square(a)
        elif figure_type == "circle":
            r = int(input("Введите радиус: "))
            return Circle(r)
        elif figure_type == "triangle":
            a = int(input("Введите основание: "))
            h = int(input("Введите высоту: "))
            return Triangle(a, h)
        else:
            raise ValueError("Неиззвестная фигура")
if __name__ == "__main__":
    figure_type = input("Введите тип фигуры (square/circle/triangle): ")
    figure = FigureFactory.create_figure(figure_type)
    print(f"Тип фигуры: {figure_type}, площадь: {figure.calculate_square()}")
