from collections import deque
H, W, K = map(int, input().split())
s = []
stack = deque()
for i in range(H):
    data = input().split()
    s.append(data)
    for j, d in enumerate(data):
        if d == "#": stack.append([i, j])


print(s)
