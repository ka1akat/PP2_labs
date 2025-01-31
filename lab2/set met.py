#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#copy
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

#difference of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x) #{'banana', 'google', 'microsoft', 'cherry', 'apple'}