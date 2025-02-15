def squar(N):
    for i in range(N):
        yield i**2

N = 5
for i in squar(N):
    print(i)