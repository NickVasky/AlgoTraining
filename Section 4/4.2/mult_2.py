def MaxPairwiseProduct(a: list[int], n: int):
    comp_counter = 1
    m1 = a[0]
    m2 = a[1]
    if m2 > m1:
        m1, m2 = m2, m1

    for i in range(2, n):
        comp_counter += 1
        if a[i] > m1:
            m2, m1 = m1, a[i]
        else:
            comp_counter += 1
            if a[i] > m2:
                m2 = a[i]
    # return m1 * m2
    # lets return the number of comparisons instead
    return comp_counter


# actual solution function
def getAnswer(n: int):
    s = [n] + list(range(1,n))
    if n > 6:
        print('Yes\n', *s)
        return True, s
    else:
        print('No')
        return False, s

# tests MaxPairwiseProduct for bad sequences
def test(n:int):
    flag, s = getAnswer(n)
    c = MaxPairwiseProduct(s, len(s))
    print(f"\nN: {n}, Comparisons: {c}")
    if c > 1.5*n:
        print("Correct")
    else:
        print("incorrect")

if __name__ == "__main__":
    for i in range(2,30):
        test(i)
