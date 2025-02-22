import re
list=["t_ext","bala_batyr","ab_kino","acc","abd"]
patt=r"[a-z]+_[a-z]+"

for i in list:
    match = re.fullmatch(patt, i)
    if match:
        print(i)