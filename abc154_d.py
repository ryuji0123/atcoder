def solve():
    mean_list = [(p + 1) / 2 for p in P]
    idx = 0
    ret = cur = sum(mean_list[idx: K])
    for i in range(1, N - K + 1):
        cur += -mean_list[i - 1]  + mean_list[i + K - 1]
        ret = max(cur, ret)
    print(ret)

N, K = map(int, input().split())
P = list(map(int, input().split()))
solve()
