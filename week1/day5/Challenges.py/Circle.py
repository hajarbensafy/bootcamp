import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Vous devez spécifier soit le rayon, soit le diamètre.")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle avec un rayon de {self.radius} et un diamètre de {self.diameter}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def draw(self):
        turtle.circle(self.radius)
        turtle.done()

def draw_circles(circles):
    """Dessine les cercles avec le module Turtle."""
    turtle.speed(0)
    for circle in circles:
        turtle.penup()
        turtle.goto(0, -circle.radius)
        turtle.pendown()
        turtle.circle(circle.radius)
    turtle.done()

# Exemple d'utilisation
if __name__ == "__main__":
    c1 = Circle(radius=50)
    c2 = Circle(diameter=100)
    c3 = c1 + c2

    print(c1)
    print(c2)
    print(c3)

    print(f"Aire de c1 : {c1.area()}")
    print(f"Aire de c2 : {c2.area()}")
    print(f"Aire de c3 : {c3.area()}")

    circles = [c3, c1, c2]
    circles.sort()
    print("Cercles triés par rayon :")
    for circle in circles:
        print(circle)

    # Bonus : Dessiner les cercles avec Turtle
    draw_circles(circles)