class bank_accaunt():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, money):
        self.balance+=money
        
    def withdrow(self, money):
        self.balance-=money

l = input().split()
n = int(l[1])
s = l[0]
cl = bank_accaunt("s", n)
cl.deposit(200546)
cl.deposit(212544)
cl.withdrow(321455)
print(f'In the {s} left {cl.balance} tenge')