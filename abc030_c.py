def solve():
    a_idx = b_idx = cur = ret = 0
    is_a = True
    while not (is_a and a_idx == N) and not (not is_a and b_idx == M):
        if is_a:
            while a_idx < N and a[a_idx] < cur:
                a_idx += 1
            if a_idx == N:
                break
            is_a = False
            cur = a[a_idx] + X
            a_idx += 1
        else:
            while b_idx < M and b[b_idx] < cur:
                b_idx += 1
            if b_idx == M:
                break
            is_a = True
            cur = b[b_idx] + Y
            b_idx += 1
            ret += 1
    print(ret)


N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
solve()
