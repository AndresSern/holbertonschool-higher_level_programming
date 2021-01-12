#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
"""


class Rectangle:
    """ Class To Define a Rectangle with withd and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter the width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return to the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Return to rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ Print the rectangle with the string of the variable
            print_symbol"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        return ("\n".join((str(self.print_symbol) *
                           self.__width for i in range(self.__height))))

    def __repr__(self):
        """ Return a string representation of the rectangle to be able to
            recreate a new instance by using eval()"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print Bye rectangle... when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ that returns the biggest rectangle based on the area
            Returns rect_1 if both have the same area value"""
        if type(rect_1) is not Rectangle:
            print("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            print("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
