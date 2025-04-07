def factorial(n):
    f = 1
    for i in range(2, n+1, 1):
        f *= i
    return f

r = input()
n, k = r.split()
n, k = int(n), int(k)

# print(n,k)
res = factorial(n) / ( factorial(k) * factorial(n-k) )
print(int(res))