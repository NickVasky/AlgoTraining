from random import randint

def input_data() -> list[int]:
    n = int(input())
    raw_numbers = input().split()

    numbers = []    
    for i in raw_numbers:
        numbers.append(int(i))
    
    return numbers

def lomuto(a: list[int]):
    wi = 0
    l = len(a)
    p = randint(0, l-1)
    print(f"Pivot a[{p}] = {a[p]}")
    for ri in range(l):
        if ri == p:
            wi+=1
            continue
        if a[ri] < a[p]:
            a[wi], a[ri] = a[ri], a[wi]
            wi+=1
        #print(a, wi)
    wi-=1
    a[p], a[wi] = a[wi], a[p]


if __name__ == "__main__":
    nums = input_data()
    lomuto(nums)
    print(*nums)