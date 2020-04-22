def solve(X, Y, p, q, r):
    red_apples = sorted(p, reverse=True)[: X]
    green_apples = sorted(q, reverse=True)[: Y]
    return sum(sorted(red_apples + green_apples + r, reverse=True)[: X + Y])

if __name__ == '__main__':
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    print(solve(X, Y, p, q, r))