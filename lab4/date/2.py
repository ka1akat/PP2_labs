from datetime import datetime, timedelta
cdate = datetime.now()
ydate=cdate-timedelta(days=1)
ndate=cdate+timedelta(days=1)

print(cdate.strftime('%Y-%m-%d'))
print(ydate.strftime('%Y-%m-%d'))
print(ndate.strftime('%Y-%m-%d'))