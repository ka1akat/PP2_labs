#add elements to list
girl_gr=["Kakos", "Tomiris", "Akbota"]
girl_gr.append("Aziza")
print(girl_gr)

#plenty of elements
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#REMOVE ELEMENT
girl_gr=["Kakos", "Tomiris", "Akbota"]
girl_gr.remove("Kakos")
girl_gr.pop(0)
print(girl_gr)