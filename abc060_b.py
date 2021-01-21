def solve():
    cur = A % B
    seen = set()
    while True:
        if cur in seen:
            print('NO')
            return
        seen.add(cur)
        if cur == C:
            print('YES')
            return
        cur = (cur + A) % B


A, B, C = map(int, input().split())
solve()
