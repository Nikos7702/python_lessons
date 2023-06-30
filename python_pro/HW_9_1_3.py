class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, name, value):
        if name == "width" or name == "height":
            raise AttributeError("Direct modification of width and height is not allowed.")
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == "width" or name == "height":
            raise AttributeError(f"Property '{name}' does not exist.")
        else:
            raise AttributeError(f"Property '{name}' does not exist.")

    def area(self):
        return self._width * self._height




rectangle = Rectangle(5, 10)

print(rectangle.width)
print(rectangle.height)
print(rectangle.area())

rectangle.width = 8

print(rectangle.unknown_property)

