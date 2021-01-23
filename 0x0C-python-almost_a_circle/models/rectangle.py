#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        self.__width

    @property
    def height(self):
        self.__height

    @property
    def x(self):
        self.__x

    @property
    def y(self, value):
        self.__y

    @width.setter
    def width(self, value):
        self.integer_validator('width', value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.integer_validator('height', value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.integer_validator('x', value)
        self.__x = value

    @y.setter
    def y(self, value):
        """ Validation"""
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    @staticmethod
    def integer_validator(name, value):
        """Check if Value is a positive Number"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and (name == 'height' or name == 'width'):
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and (name == 'y' or name == 'x'):
            raise ValueError('{} >= 0'.format(name))

    def display(self):
        """ Print the rectangle with # """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        string = ("[Rectangle] ({}) {}/{} - {}/{}"
                  .format(self.id, self.__x, self.__y, self.__width,
                          self.__height))
        return string

    def update(self, *args):
        attr = ["id", "_Rectangle__width", "_Rectangle__height",
                "_Rectangle__x", "_Rectangle__y"]
        my_len = len(attr)
        for i, argv in enumerate(args):
            if i < my_len:
                self.__dict__[attr[i]] = argv
