#there are popular two ways of joining
#first one
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#second one
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for i in list2:
  list1.append(i)

print(list1)