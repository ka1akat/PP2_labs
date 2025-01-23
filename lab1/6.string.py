#string is one of data type
x="Kbtu one of the best univercitY,place"

#slicing strings
print(x[-5:-2]) #rci
print(x[3:]) #u one of the best univercity
print(x[2:]) #tu one of the best univercity

#Modify Strings
print(x.upper())
print(x.lower())

n=" Hello "
print(n.strip())

print(x.replace("K", "Y"))
print(x.split(" "))

#String Concatenation
#more clear
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

#not convenient
a = "Hello"
b = "World"
c = a + b
print(c)

#2 method
str1 = "Hello"
str1 += " World"
print(str1)

#Format - Strings
#Create an f-string
name = "Karakat"
age = 17
strr = f"My name is {name}, I am {age}"
print(strr)

#Placeholders and Modifiers
size = 59
txt = f"The size is {size} pounts"
print(txt)

size = 59
txt = f"The size is {size:.2f} pounts"
print(txt)

txt = f"The size is {6*7} pounts"
print(txt)










