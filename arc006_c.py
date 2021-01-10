def solve():
    ret = []
    for w in W:
        is_pushable = False
        for idx in range(len(ret)):
            if w <= ret[idx][-1]:
                ret[idx].append(w)
                is_pushable = True
                break
        if not is_pushable:
            ret.append([w])
    print(len(ret))


N = int(input())
W = [int(input()) for _ in range(N)]
solve()
