def input_data() -> list[int]:
    n = int(input())
    raw_numbers = input().split()

    numbers = []    
    for i in raw_numbers:
        numbers.append(int(i))
    
    return numbers

def merge(first: list[int], second: list[int]) -> list[int]:
    r = []
    while len(first) > 0 and len(second) > 0:
        if first[0] < second[0]:
            r.append(first.pop(0))
        else:
            r.append(second.pop(0))
    
    r.extend(first)
    r.extend(second)

    return r

def merge_sort(a: list[int]) -> list[int]:
    l = len(a)
    if l == 1:
        return a
    hl = l // 2
    first, second = a[0:hl], a[hl:l]
    first, second = merge_sort(first), merge_sort(second)
    return merge(first, second)


if __name__ == "__main__":
    nums = input_data()
    snums = merge_sort(nums)
    print(*snums)