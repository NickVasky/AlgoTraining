def factorial(n):
    f = 1
    for i in range(2, n+1, 1):
        f *= i
    return f

r = input()
n, k = r.split()
n, k = int(n), int(k)

# print(n,k)
res = factorial(n + k - 1) / ( factorial(k) * factorial(n-1) )
print(int(res))