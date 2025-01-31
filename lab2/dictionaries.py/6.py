#Copy Dictionaries 
my_dict = {"name": "Alice", "age": 25, "city": "Wonderland"}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}

#Nested Dictionaries
my_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(my_dict["person1"]["name"])  # Output: Alice

#Dictionary Methods
my_dict = {"name": "Alice", "age": 25, "city": "Wonderland"}
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)  # Output: dict_keys(['name', 'age', 'city'])
print(values)  # Output: dict_values(['Alice', 25, 'Wonderland'])
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'Wonderland')])