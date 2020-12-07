def solve():
    ret = float('inf')
    for x in range(-100, 101):
        cost = 0
        for a in A:
            cost += (a - x) ** 2
        ret = min(ret, cost)
    print(ret)


N = input()
A = list(map(int, input().split()))
solve()
