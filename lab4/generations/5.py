def func(n):
    for i in range(n+1):
        yield i

n=int(input())
num=[]
for i in func(n):
    num.append(i)
num.reverse()
for i in range(n):
    print(num[i],end=" ")


    
