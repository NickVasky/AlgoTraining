def input_data() -> list[list[int]]:
    n, m = map(int, input().split())

    mats = []
    for i in range(2):
        matrix = []
        for i in range(n):
            row = list(map(int, input().split()))[0:m]
            matrix.append(row)
        mats.append(matrix)
            
    return mats, n, m

def sum_of_elem(mats: list[list[list[int]]], n: int, m: int) -> list[list[int]]:
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(mats[0][i][j]+mats[1][i][j])
        result.append(row)
    return result

if __name__ == "__main__":
    mats, n, m = input_data()
    res = sum_of_elem(mats, n, m)
    for row in res:
        print(*row)