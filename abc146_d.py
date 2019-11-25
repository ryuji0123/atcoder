from collections import deque
N = int(input())
edges = [[] for _ in range(N + 1)]
for edge_idx in range(1, N):
    a, b = map(int, input().split())
    edges[a].append([edge_idx, b])
    edges[b].append([edge_idx, a])

used_edges = set()
colors = [1 for _ in range(1, N + 1)]
used_colors = [set() for _ in range(N + 1)]
stack = deque([[edges[1], 0]])
max_col = 1

while stack:
    edge_info, parent_node_idx = stack.pop()
    cur_color = 1
    for edge_idx, node_idx in edge_info:
        if edge_idx in used_edges: continue
        while cur_color in used_colors[node_idx] or cur_color in used_colors[parent_node_idx]:
            cur_color += 1
        used_colors[node_idx].add(cur_color)
        colors[edge_idx] = cur_color
        stack.append([edges[node_idx], node_idx])
        used_edges.add(edge_idx)
        max_col = max(max_col, cur_color)
        cur_color += 1

print(max_col)
for c in colors[1:]:
    print(c)
