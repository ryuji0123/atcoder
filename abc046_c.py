def solve():
    l, r = A[0]
    for a, b in A:
        if l * b == r * a:
            continue
        da = l // a + (l % a != 0)
        db = r // b + (r % b != 0)
        l = max(da, db) * a
        r = max(da, db) * b
    print(l + r)


N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
solve()
