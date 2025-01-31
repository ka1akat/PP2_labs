#Change Tuple Values
x=("Kakos", "Tomiris", "Akbota","Aishabibi")
y = list(x)
y[1] = "Aida"
y.append("Aisaule")
x = tuple(y)

print(x)