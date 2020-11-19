def cmp(sa, sb):
    idx = 0
    na = len(sa)
    nb = len(sb)
    
    while idx < min(na, nb):
        if sa[idx] == sb[idx]:
            idx += 1
            continue
        return 1 if sb < sa else -1
    if sa == sb:
        return 0
    return 1 if nb < na else -1

def solve():
    N = len(s)
    sizes = [1] * N
    count = 0
    used = set()
    min_sub = ''
    while count < K:
        idxs = []
        min_sub = None
        for idx in range(N):
            while idx + sizes[idx] < N + 1 and s[idx: idx + sizes[idx]] in used:
                sizes[idx] += 1

            if idx + sizes[idx] == N + 1:
                continue

            sub = s[idx: idx + sizes[idx]]
            if min_sub is None:
                min_sub = sub
                idxs = [idx]
                continue

            sub = s[idx: idx + sizes[idx]]
            c = cmp(min_sub, sub)
            if c == -1:
                continue
            if c == 0:
                idxs.append(idx)
            else:
                min_sub = sub
                idxs = [idx]
        used.add(min_sub)
        count += 1
    print(min_sub) 

s = input()
K = int(input())
solve()
