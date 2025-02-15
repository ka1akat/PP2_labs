from datetime import datetime
d1=datetime(2023, 10, 1, 12, 0, 0)
d2=datetime(2023, 10, 2, 12, 0, 0)

diff=d2-d1

difs= diff.total_seconds()

print(difs)