# time: O(N)
# space: O(1)

def solve():
    ret = v[0]
    idx = 1
    while idx < N:
        ret = (ret + v[idx]) / 2
        idx += 1
    print(ret)

N = int(input())
v = sorted(list(map(int, input().split())))
solve()
