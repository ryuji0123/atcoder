def solve():
    count = [0]
    for idx in range(N - 1):
        if S[idx] + S[idx + 1] == 'AC':
            count.append(count[-1] + 1)
        else:
            count.append(count[-1])
    for l, r in vals:
        print(count[r - 1] - count[l - 1])


N, Q = map(int, input().split())
S = input()
vals = []
for _ in range(Q):
    vals.append(map(int, input().split()))
solve()
