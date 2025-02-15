from datetime import datetime
cdate = datetime.now()
wds = cdate.replace(microsecond=0)

print(cdate)
print(wds)