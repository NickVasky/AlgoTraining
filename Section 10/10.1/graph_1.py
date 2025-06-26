class Route:
    def __init__(self, k: int, stops: list[int]):
        self.k = k
        self.stops = stops


class Task:
    def __init__(self, n: int, m: int, routes: list[Route]):
        self.n = n
        self.m = m
        self.routes = routes


def input_data() -> Task:
    raw_params = input().split()
    n = int(raw_params[0])
    m = int(raw_params[1])

    routes = []
    for i in range(m):
        stops = []
        raw_numbers = input().split()
        k = int(raw_numbers[0])
        for i in range(1, k + 1):
            stops.append(int(raw_numbers[i]))

        routes.append(Route(k,stops))

    return Task(n,m, routes)


def getAdjacencyForNeighbours(task: Task) -> list[list[int]]:
    mat = [[0] * task.n for _ in range(task.n)]

    for route in task.routes:
        for i in range(route.k):
            if i + 1 < route.k:
                stop = route.stops[i]
                nextstop = route.stops[i+1]
                mat[stop - 1][nextstop - 1] = 1
                mat[nextstop - 1][stop - 1] = 1

    return mat


def getAdjacencyWithoutTransfers(task: Task) -> list[list[int]]:
    mat = [[0] * task.n for _ in range(task.n)]

    for route in task.routes:
        combs = getCombs2(route.stops, route.k)
        for comb in combs:
            mat[comb[0] - 1][comb[1] - 1] = 1
            mat[comb[1] - 1][comb[0] - 1] = 1

    return mat

def getCombs2(a: list[int], n: int) -> list[tuple[int, int]]:
    combs = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            combs.append( (a[i], a[j]) )
    return combs

def printMatrix(mat: list[list[int]]):
    for r in mat:
        print(*r)


if __name__ == "__main__":
    task = input_data()
    mat1 = getAdjacencyForNeighbours(task)
    mat2 = getAdjacencyWithoutTransfers(task)

    printMatrix(mat1)
    printMatrix(mat2)
