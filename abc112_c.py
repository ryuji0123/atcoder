def solve():
    vals.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            x, y, h = vals[0]
            H = h + abs(x - cx) + abs(y - cy)
            if all([h == max(0, H - abs(x - cx) - abs(y - cy)) for x, y, h in vals]):
                print(cx, cy, H)
                return


N = int(input())
vals = []
for _ in range(N):
    vals.append(list(map(int, input().split())))
solve()
