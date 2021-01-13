from collections import Counter


def solve():
    def classify(counter, M, m):
        if 35 <= M:
            counter[1] += 1
        if 30 <= M < 35:
            counter[2] += 1
        if 25 <= M < 30:
            counter[3] += 1
        if 25 <= m:
            counter[4] += 1
        if m < 0 and 0 <= M:
            counter[5] += 1
        if M < 0:
            counter[6] += 1
    
    counter = Counter()
    for M, m in T:
        classify(counter, M, m)
    for i in range(1, 6):
        print(counter[i], end=' ')
    print(counter[6])

N = int(input())
T = [list(map(float, input().split())) for _ in range(N)]
solve()
