class Shape():
    def __init__(self):
        self.a = 0
        
        
class Ractangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        
    def area(self):
        a = self.lenght*self.width
        print(a)
        
        
l , w = map(int, input().split())
cl = Ractangle(l,w)
cl.area()