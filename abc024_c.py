def solve():
    ret = [D for _ in range(K)]
    loc = [loc_info[i][0] for i in range(K)]
    is_target_ahead = [s <= t for s, t in loc_info]

    for d, (l, r) in enumerate(day_info):
        for i in range(K):
            if loc_info[i][1] == loc[i] or loc[i] < l or r < loc[i]:
                continue
            
            if l <= loc_info[i][1] <= r:
                loc[i] = loc_info[i][1]
                ret[i] = d + 1
                continue
            
            loc[i] = r if is_target_ahead[i] else l

    for r in ret:
        print(r)


N, D, K = map(int, input().split())
day_info = [list(map(int, input().split())) for _ in range(D)]
loc_info = [list(map(int, input().split())) for _ in range(K)]
solve()
