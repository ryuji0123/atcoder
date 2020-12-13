def solve():
    ret = float('-inf')
    for i in range(N):
        scores = []
        for j in range(N):
            if i == j:
                continue
            mi, mj = min(i, j), max(i, j)
            scores.append([
                sum([a[idx] for idx in range(mi, mj + 1) if (idx - mi) % 2 == 0]),
                sum([a[idx] for idx in range(mi, mj + 1) if (idx - mi) % 2 == 1])
            ])
        if 0 < len(scores):
            scores.sort(key=lambda x: -x[1])
            ret = max(ret, scores[0][0])
    print(ret)


N = int(input())
a = list(map(int, input().split()))
solve()
