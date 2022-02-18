from math import sqrt

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f'x = {self.x} and y = {self.y}')
        
    def move(self):
        self.x , self.y = self.y , self.x
        print(f'After changing  x = {self.x} and y = {self.y}')
        
    def dist(self):
        d = sqrt((self.y-self.x)**2 + (self.x - self.y)**2)
        print(f'Distance between x,y and y,x = {d}')
        
a,b = map(int, input().split())
cl = point(a,b)
cl.show()
cl.move()
cl.dist()
        