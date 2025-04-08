def input_data() -> list[str]:
    strings = []
    n = int(input())
    for i in range(2):
        strings.append(input()[:n])
    
    return strings, n

def strange_sum(strings: list[str], n: int):
    sum = []
    for i in range(n):
        sum.append(strings[0][i] + strings[1][i])
    return "".join(sum)


if __name__ == "__main__":
    strings, n = input_data()
    res = strange_sum(strings, n)
    print(res)