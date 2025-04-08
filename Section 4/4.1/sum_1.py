def sum_of_two(a:int, b:int) -> int:
    return a + b

if __name__ == "__main__":
    a, b = map(int, input().split())
    s = sum_of_two(a, b)
    print(s)