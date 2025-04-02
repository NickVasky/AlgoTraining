from time import process_time_ns

NS = pow(10,9)

def input_data() -> list[list[int]]:
    n = int(input())

    lists = []
    for i in range(n):
        m = int(input())

        numbers = []
        raw_numbers = input().split()
        for i in raw_numbers:
            numbers.append(int(i))
        
        lists.append(numbers)
    
    return lists

def merge(first: list[int], second: list[int]) -> list[int]:
    r = []
    l1, l2 = len(first), len(second)
    i1, i2 = 0, 0
    
    # First version of merge() used the list.pop() method iterate through
    # both parts of list. However, pop() has linear complexity O(n).
    # The removal of pop() made execution x20 faster for 10^5 elements 
    while i1 < l1 and i2 < l2:
        if first[i1] < second[i2]:
            r.append(first[i1])
            i1+=1
        else:
            r.append(second[i2])
            i2+=1
    
    r.extend(first[i1:])
    r.extend(second[i2:])

    return r

def merging(lists: list[list[int]]) -> list[list[int]]:
    l = len(lists)

    if l == 1:
        return lists
    
    nlists = []
    for i in range(l//2):
        l1, l2 = lists[i], lists[l - i - 1]
        nlists.append(merge(l1, l2))
    
    if l % 2 == 1:
        nlists.append(lists[l//2+1])
    
    return merging(nlists)

if __name__ == "__main__":
    lists = input_data()

    t = process_time_ns()
    result = merging(lists)[0]
    t1 = process_time_ns() - t

    print(*result)
    print(f"\nN: {len(lists)}\nSum of N*Mi: {len(result)}\nExec time: {t1/NS:.4f} sec")