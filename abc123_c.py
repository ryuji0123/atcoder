def solve():
    mf = float('inf')
    for idx in range(length):
        if flow[idx] < mf:
            mf = flow[idx]
            mi = idx
    print(length - 1 -(-N // mf))


length = 5
N = int(input())
flow = []
for _ in range(length):
    flow.append(int(input()))
solve()
