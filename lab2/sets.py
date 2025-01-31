#what is set
thislist = {"apple", "banana", "cherry"}
print(thislist)
#Loop through the set, and print the values:
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
print(thisset) #{'mango', 'apple', 'cherry', 'papaya', 'orange', 'banana', 'pineapple'}

#remove sets
#to remove specific item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#to remove randomj or last element
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#delete the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

