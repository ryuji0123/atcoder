# time: O(N2^N)
# space: O(N)

def isValid(honests):
    for k in honests.keys():
        for x, y in A[k]:
            if (x - 1 in honests and y == 0) or (x - 1 not in honests and y == 1):
                return False
    return True


def solve():
    ret = 0
    for i in range(pow(2, N)):
        honests = {}
        for j in range(N):
            if i >> j & 1:
                honests[j] = 1
        if isValid(honests):
            ret = max(ret, len(honests.keys()))
    print(ret)


N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append([])
    for _ in range(a):
        A[-1].append(list(map(int, input().split())))
solve()
