from math import sqrt

def input_data():
    n = input()
    return int(n)

def calc_k(n):
    return n - round(sqrt(2*n + 1)) + 1 

def hanoi4_moves(n):
    if n == 1:
        return 1
    else:
        k = calc_k(n)
        return 2 * hanoi4_moves(k) + hanoi3_moves(n-k)

def hanoi3_moves(n):
    return pow(2, n) - 1

#it looks simple now but it was quite a journey on paper to build recurrent rules

if __name__ == "__main__":
    n = input_data()
    print(hanoi4_moves(n))
