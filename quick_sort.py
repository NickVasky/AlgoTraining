from random import randint

def input_data() -> list[int]:
    n = int(input())
    
    raw_numbers = input().split()
    numbers = []
    for i in raw_numbers:
        numbers.append(int(i))
    
    return numbers


def lomuto(a: list[int], lo: int, hi: int, p: int):
    wi = lo

    # swap p and hi and consider hi elem to be a pivot
    a[p], a[hi] = a[hi], a[p]
    pivot = a[hi]

    for ri in range(lo, hi):
        if a[ri] <= pivot:
            a[wi], a[ri] = a[ri], a[wi]
            wi+=1
    
    a[wi], a[hi] = a[hi], a[wi]
    return wi


def quick_sort(a: list[int], lo, hi):
    if lo >= hi or lo < 0:
        return
    
    p = randint(lo, hi)
    p = lomuto(a, lo, hi, p)

    quick_sort(a, lo, p-1)
    quick_sort(a, p+1, hi)


if __name__ == "__main__":
    nums = input_data()
    quick_sort(nums, 0, len(nums)-1)
    print(*nums)