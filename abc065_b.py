def solve():
    seen = set()
    cur = 1
    count = 0
    while True:
        if cur == 2:
            print(count)
            return
        if cur in seen:
            print(-1)
            return
        seen.add(cur)
        cur = d[cur]
        count += 1


N = int(input())
d = {}
for i in range(1, N + 1):
    d[i] = int(input())
solve()
