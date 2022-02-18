class console():
    def getString(self, s):
        self.s = s
        
    def printString(self):
        print(self.s.upper())
        
cl = console()

cl.getString(input())
cl.printString()
