#starts with a then any characters and at the end b
import re
list=["cayb","alab","abbbb","Samat","atalab"]
patt=r"a.*b"

for i in list:
    match = re.fullmatch(patt, i)
    if match:
        print(i)