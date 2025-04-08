def input_data():
    n = input()
    return int(n)

def hanoi(n, from_peg, to_peg):
    if n == 1:
        print(from_peg, to_peg)
        return
    free_peg = 6 - (from_peg + to_peg)
    hanoi(n - 1, from_peg, free_peg)
    print(from_peg, to_peg)
    hanoi(n - 1, free_peg, to_peg)

if __name__ == "__main__":
    n = input_data()
    print(pow(2, n) - 1)
    hanoi(n, 1, 3)