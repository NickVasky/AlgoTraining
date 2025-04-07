def input_data():
    n, m = input().split()
    return int(n), int(m)

def check_win(n:int, m:int) -> bool:
    if n == m or abs(m - n) % 3 == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    answers = {True: 'Win', False: 'Lose'}
    n, m = input_data()
    print(answers[check_win(n, m)])