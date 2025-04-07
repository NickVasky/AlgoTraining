def factorial(n):
    f = 1
    for i in range(2, n+1, 1):
        f *= i
    return f

n = int(input())
f = factorial(n)
print(f)