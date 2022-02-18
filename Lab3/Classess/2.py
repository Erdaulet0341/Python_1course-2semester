class Shape():
    def __init__(self):
        self.a = 0
        
class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
        self.a = 0
        
    def area(self):
        k = self.lenght * self.lenght
        print(k)

k = int(input())
cl = Square(k)
cl.area()