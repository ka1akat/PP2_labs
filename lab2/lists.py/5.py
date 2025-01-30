#List Comprehension
#example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#example 2
girl_gr=["Kakos", "Tomiris", "Akbota"]

newlist = [x for x in girl_gr if "a" in x]

print(newlist)

#example
newlist2 = [x for x in range(10) if x < 5]
print(newlist2)
