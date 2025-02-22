import re

def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()


input_str = "CamelCaseStringExample"
output_str = insert_spaces(input_str)
print(output_str)  
