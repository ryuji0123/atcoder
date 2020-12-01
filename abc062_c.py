def calc(H, W):
    ret = float('inf')
    for h1 in range(1, H):
        h2 = (H - h1) // 2
        h3 = H - h1 - h2
        S = [W * h1, W * h2, W * h3]
        if all([1 <= s for s in S]):
            ret = min(ret, max(S) - min(S))
        h2 = H - h1
        w2 = W // 2
        S[1] = h2 * w2
        S[2] = h2 * (W - w2)
        if all([1 <= s for s in S]):
            ret = min(ret, max(S) - min(S))
    return ret


def solve():
    print(min(calc(H, W), calc(W, H)))


H, W = map(int, input().split())
solve()
