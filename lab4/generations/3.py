def interv(x):
    for i in range(x+1):
        if i%3==0 and i%4==0:
            yield i

x=int(input())
for i in interv(x):
    print(i)