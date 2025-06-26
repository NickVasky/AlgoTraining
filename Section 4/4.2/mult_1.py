class Task:
    def __init__(self, n: int, a: list[int]):
        self.n = n
        self.a = a


def input_data() -> Task:
    n = int(input())

    raw_numbers = input().split()
    a = []
    for i in range(n):
        a.append(int(raw_numbers[i]))

    return Task(n, a)


def findTwoMax(a: list[int], n: int) -> tuple[int, int]:
    for i in range(2):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return (a[n-2], a[n-1])

if __name__ == "__main__":
    task = input_data()
    max = findTwoMax(task.a, task.n)
    print(max[0] * max[1])
