from collections import Counter


def solve():
    m = sorted([[e, c] for e, c in Counter(A).most_common() if 2 <= c], key=lambda x: -x[0])
    if len(m) == 0 or (len(m) == 1 and m[0][1] < 4):
        print(0)
    elif 4 <= m[0][1]:
        print(m[0][0]**2)
    elif 2 <= m[0][1] and 2 <= m[1][1]:
        print(m[0][0] * m[1][0])
    else:
        print(0)


N = input()
A = list(map(int, input().split()))
solve()
