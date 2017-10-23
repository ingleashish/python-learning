import module
from module import console_log
class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        console_log('you have instantiate the circle object')
        self.radius = radius

    def area(self):
        module.my_first_module_func()
        return self.radius * self.radius * Circle.pi



my_circle = Circle(14)
print("radius of circle {} which calculated area is {} ".format(my_circle.radius,my_circle.area()))
