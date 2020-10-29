from collections import Counter
def solve():
    c = Counter(S)
    count = c.most_common()[0][1]
    for e, co in sorted(c.most_common(), key=lambda x: (-x[1], x[0])):
        if co != count:
            return
        print(e)

N = int(input())
S = []
for _ in range(N):
    S.append(input())
solve()
