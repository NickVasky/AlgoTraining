def input_data() -> list[list[int]]:
    lists = []
    for i in range(2):
        m = int(input())

        numbers = []
        raw_numbers = input().split()
        for i in raw_numbers:
            numbers.append(int(i))
        
        lists.append(numbers)
    
    return lists

def reverse(a: list[int]):
    l = len(a)
    hl = l // 2
    for i in range(hl):
        a[i], a[l-i-1] = a[l-i-1], a[i]

def sum_sequences(lists: list[list[int]]):
    lens = list(map(len, lists))

    res = []
    while lens[0] > 0 and lens[1] > 0:
        s = lists[0][lens[0]-1] + lists[1][lens[1]-1]
        res.append(s)
        lens[0] -= 1
        lens[1] -= 1

    for i in range(2):
        while lens[i] > 0:
            res.append(lists[i][lens[i]-1])
            lens[i] -= 1

    return res

if __name__ == "__main__":
    lists = input_data()
    res = sum_sequences(lists)
    reverse(res)
    print(*res)