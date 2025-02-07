def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    a=numbers[i]
    primes =lambda x: is_prime(a)
print("Простые числа:", primes)  
