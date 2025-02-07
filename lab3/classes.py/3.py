class Rectangle:
    def __init__(self,d,sh):
        self.d=d
        self.sh=sh

    def area(self):
        return self.d*self.sh
    
d=int(input())
sh=int(input())
S=Rectangle(d,sh)
print(S.area())
