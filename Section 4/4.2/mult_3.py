from operator import truediv
class Task:
    def __init__(self, n: int, a: list[int]):
        self.n = n
        self.a = a
        self.k = 3


def input_data() -> Task:
    n = int(input())

    raw_numbers = input().split()
    a = []
    for i in range(n):
        a.append(int(raw_numbers[i]))

    return Task(n, a)

def lt(a, b) -> bool:
    if a < b:
        return True
    else:
        return False

def gt(a, b) -> bool:
    if a > b:
        return True
    else:
        return False

def find_min_max_k(comparison_op, a: list[int], n: int, k: int) -> list[int]:
    for i in range(k):
        for j in range(n-i-1):
            if comparison_op(a[j], a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

    res = []
    for i in range(k):
        res.append(a[n-i-1])

    return res

# Time complexity is O(3N+2N)
if __name__ == "__main__":
    task = input_data()

    maxs = find_min_max_k(gt, task.a, task.n, task.k) # looking for 3 biggest positives
    mins = find_min_max_k(lt, task.a, task.n, task.k-1) # looking for 2 biggest negatives

    res = max(mins[0]*mins[1]*maxs[0], maxs[0]*maxs[1]*maxs[2]) # choosing biggest combination

    print(res)
