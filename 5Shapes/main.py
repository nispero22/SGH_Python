class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def calc_perimeter(self):
        return self._a*2+self.b*2

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

#Question_3. adding a Square that inherits from Rectangle and uses its calc_surface implementation
#inheritance to calculate the surface and the perimeter of the square
class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a,a)


import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def calc_perimeter(self):
        return 2*math.pi*self._a

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


class Sphere(Circle):
    def calc_volume(self):
        return 4/3*math.pi*self._a**3

    def calc_surface(self):
        return 4*super().calc_surface()

# Question_1. adding a Triangle and EquilateralTriangle - they may inherit from each other
class Triangle(Shape):
    def __init__(self, _a, b, c):
        super().__init__(_a, b)
        self.c=c
    pass

    def calc_perimeter(self):
        return self._a+self.b+self.c

class EquilateralTriangle(Triangle):
    def __init__(self, _a):
        super().__init__(_a,0,0)
        pass

    def calc_perimeter(self):
        return self._a*3


#profesor's tests
r = Rectangle(5, 6)
print(r)
#r._a = 600
print(r.calc_surface())
r.swap_sides()
r_desc = str(r)
print(r_desc)

c = Circle(7)
c_desc = str(c)
print(c_desc)
print(c.calc_surface())
s = Sphere(8)
print(s)
print('s volume: ')
print(s.calc_volume())
print('s surface:')
print(s.calc_surface())

shape_list = [r, c, s]
print()
print('--------------------')
for sh in shape_list:
    print(sh.__class__.__name__)
    sh.set_params(10, 15)
    print(sh.calc_surface())


print('--------------------')
print("my tests")


# Question_4. providing some code that tests the new functionality and structures
# Question_2. adding perimeter calculation to every structure (except Sphere)
# calculation of perimeters : rectangle, square, circle, triangle and equilateral triangle
print("Rectangle perimeter")
r = Rectangle(5, 6)
print(r.calc_perimeter()==22)
print("Square perimeter")
s = Square(3)
print(s.calc_perimeter()==12)
print("Square surface")
print(s.calc_surface()==9)
print("Circle perimeter")
c = Circle(3)
print(c.calc_perimeter())
print("Triangle perimeter")
t1 = Triangle(2,3,30)
print(t1.calc_perimeter()==35)
print("Equilateral Triangle perimeter")
t2 = EquilateralTriangle (5) #Side of EquilateralTriangle = 5
print(t2.calc_perimeter()==15)

