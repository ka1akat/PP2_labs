class bank_acc:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=0

    def deposit(self,k):
        print("ваш баланс равно:")
        self.balance+=k
        print(f"{k} добавлено. Текущий баланс: {self.balance}")

    def withdraw(self,piece):
        if piece>self.balance:
            l=piece-self.balance
            print(f"Недостаточно средств,не хватает {l}" )
        else:
            self.balance-=piece
            print(f"{k} снято. Текущий баланс: {self.balance}")

x=input("Введите имя:")
y=int(input("Введите ваш баланс:"))
c=int(input("Сколькоо хотите добавить:"))
d=int(input("Сколько хотите снять:"))
acc = bank_acc(x,y)
acc.deposit(c)  
acc.withdraw(d) 
 
