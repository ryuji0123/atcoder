def solve():
    ret = start = end = 0
    for t in times:
        if t <= end:
            end = t + T
        else:
            ret += end - start
            start = t
            end = t + T
    print(ret + (end == times[-1] + T) * (end - start))


N, T = map(int, input().split())
times = list(map(int, input().split()))
solve()
