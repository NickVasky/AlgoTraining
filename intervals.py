class Interval:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    
    def __str__(self):
        return f"Interval: [{self.l}, {self.r}]"
    
    def is_intersects(self, other) -> bool:
        if other.l > self.r or other.r < self.l:
            return False
        else:
            return True


def get_champ(intervals: list[Interval]) -> int:
    champ_index = 0
    for idx, inter in enumerate(intervals):
        if inter.r < intervals[champ_index].r:
            champ_index = idx
    
    return champ_index


def remove_intersections(intervals: list[Interval], champ_index: int) -> list[Interval]:
    intervals_new = []
    for i in intervals:
        if not intervals[champ_index].is_intersects(i):
            intervals_new.append(i)
    
    return intervals_new


def input_data() -> list[Interval]:
    n = int(input())
    intervals = []

    for i in range(n):
        l, r = input().split()
        intervals.append(Interval(int(l), int(r)))
    
    return intervals

if __name__ == "__main__":
    num_of_intervals = 0
    intervals = input_data()
    
    while (len(intervals) > 0):
        champ_index = get_champ(intervals)
        print("Champ is: ", intervals[champ_index])
        intervals = remove_intersections(intervals, champ_index)
        num_of_intervals += 1
    
    print(num_of_intervals)