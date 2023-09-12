# factory pattern

class Shape(object):
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Draw Circle")

class Rectangle(Shape):
    def draw(self):
        print("Draw Rectangle")

class Square(Shape):
    def draw(self):
        print("Draw Square")

class ShapeFactory(object):
    @staticmethod
    def getShape(shapeType):
        if shapeType == 'CIRCLE':
            return Circle()
        elif shapeType == 'RECTANGLE':
            return Rectangle()
        elif shapeType == 'SQUARE':
            return Square()
        else:
            return None

if __name__ == '__main__':
    shape1 = ShapeFactory.getShape('CIRCLE')
    shape1.draw()

    shape2 = ShapeFactory.getShape('RECTANGLE')
    shape2.draw()

    shape3 = ShapeFactory.getShape('SQUARE')
    shape3.draw()

    shape4 = ShapeFactory.getShape('HEXAGON')
    shape4.draw()


# Reference:
# https://www.geeksforgeeks.org/factory-method-python-design-patterns/