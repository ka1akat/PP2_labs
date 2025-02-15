from datetime import datetime, timedelta
cdate = datetime.now()
ndate=cdate-timedelta(days=5)

print(cdate.strftime('%Y-%m-%d'))
print(ndate.strftime('%Y-%m-%d'))