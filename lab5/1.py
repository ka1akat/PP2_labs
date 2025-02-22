import re
list=["a","ab","abb","acc","abd"]
patt=r"ab*"

for i in list:
    match = re.fullmatch(patt, i)
    if match:
        print(i)