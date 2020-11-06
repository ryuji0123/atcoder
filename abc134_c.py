def solve():
    m1, m2 = sorted(A, reverse=True)[:2]
    for a in A:
        print(m1 if m1 != a else m2)


N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
solve()
