import math
def carea(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

n = int(input())
s = float(input())


area = carea(n, s)

print(area)