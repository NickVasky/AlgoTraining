def input_data() -> list[int]:
    n = int(input())
    raw_numbers = input().split()

    numbers = []    
    for i in raw_numbers:
        numbers.append(int(i))
    
    return numbers


def selection_sort(a: list[int]) -> list[int]:
    l = len(a)
    for i in range(l):
        for j in range(i, l, 1):
            if a[j] < a[i]:
                a[j], a[i] = a[i], a[j]
    return a


if __name__ == "__main__":
    nums = input_data()
    snums = selection_sort(nums)
    print(*snums)