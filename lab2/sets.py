#what is list
thislist = ["apple", "banana", "cherry"]
print(thislist)
#data types of lists
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#example 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#example 2 checking
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
print("banana" not in thisset)

#Add Set Items
thisset.add("orange")
print(thisset)

#update sets
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)