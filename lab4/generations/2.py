def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())
even_numbers = even(n)
first = True
for num in even_numbers:
    if not first:
        print(",", end="")
    print(num, end="")
    first = False
print()
