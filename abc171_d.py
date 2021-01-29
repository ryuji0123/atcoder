from collections import Counter

def solve():
    s = sum(A)
    counter = Counter(A)
    for b, c in replace_list:
        num = counter[b]
        counter[b] = 0
        counter[c] += num
        s += num * (c - b)
        print(s)


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
replace_list = [list(map(int, input().split())) for _ in range(Q)]
solve()
