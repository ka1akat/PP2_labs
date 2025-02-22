import re
list=["a","ab","abb","abbcc","abbb"]
patt=r"ab{2,3}"

for i in list:
    match = re.fullmatch(patt, i)
    if match:
        print(i)