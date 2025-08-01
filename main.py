class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Invalid new width for rectangle.")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Invalid new width for rectangle.")

    @width.deleter
    def width(self):
        del self._width
        print("Private width has been deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Private height has been deleted.")


rectangle = Rectangle(3, 4)

rectangle.width = 6
rectangle.height = 15

del rectangle.width
del rectangle.height

rectangle.width = 6
rectangle.height = 15

print(rectangle.width, rectangle.height)


        



