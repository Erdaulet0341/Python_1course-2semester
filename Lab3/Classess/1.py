import string


class Years_cars:
    def __init__(self, string):
        self.string = string
    
    def getString(self):
        string = input()
        
    def printString(self):
        string = string.upper()
        print(f'{string}')
        
qaz = Years_cars()
qaz.getString()
qaz.printString()