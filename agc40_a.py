from collections import deque
MAX = float('inf')
S = input()
points = [MAX] * (len(S) + 1)
idxs = []
comp = [[] for _ in range(len(S) + 1)]
if S[0] == '<':
    points[0] = 0
    idxs.append(0)
if S[-1] == '>':
    points[-1] = 0
    idxs.append(len(S))
for idx, s in enumerate(S):
    if s == '<': comp[idx].append(idx + 1)
    else: comp[idx + 1].append(idx)
    if idx == 0 or idx == len(S): continue
    if S[idx - 1] == '>' and s == '<':
        points[idx] = 0
        idxs.append(idx)
stack = deque(idxs)
while stack:
    idx = stack.pop()
    for i in comp[idx]:
        points[i] = max(points[i], points[idx] + 1) if points[i] != MAX else points[idx] + 1
        stack.append(i)
print(sum(points))
