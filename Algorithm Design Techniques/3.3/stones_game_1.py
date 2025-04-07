def input_data():
    n, m = input().split()
    return int(n), int(m)

def check_win(n:int, m:int) -> bool:
    if n % 2 == 0 and m % 2 == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    print(0 % 3)
    answers = {True: 'Win', False: 'Lose'}
    n, m = input_data()
    print(answers[check_win(n, m)])