import heapq

if __name__ == '__main__':
    n, q = map(int, input().split())
    nodes = [[] for _ in range(n + 1)]
    counter = [0] * (n + 1)
    is_valid = [1] * (n + 1)
    
    for _ in range(n - 1):
        p_idx, c_idx = map(int, input().split())
        nodes[p_idx].append(c_idx)
        nodes[c_idx].append(p_idx)

    for _ in range(q):
        idx, cnt = map(int, input().split())
        counter[idx] += cnt

    l = []
    heapq.heapify(l)
    heapq.heappush(l, nodes[1])
    
    print(*counter[1:])
