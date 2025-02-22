import re
list=["Zara","ZANA","abumat","Samat","ALTynai"]
patt=r"[A-Z][a-z]+"

for i in list:
    match = re.fullmatch(patt, i)
    if match:
        print(i)