class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    # Return number of times shape can fit inside shape without rotation
    def get_amount_inside(self, shape):
        # Take another shape as argument
        return self.get_area() // shape.get_area()


# Subclass of Rectangle(), single side length passed in
class Square(Rectangle):
    # Can access Rectangle() methods
    # Store side length in both width and height attributes of Rectangle()
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    # set_width and set_height sets all sides
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def set_side(self, side):
        self.width = side
        self.height = side
