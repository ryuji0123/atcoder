def solve():
    x2, y2 = W / 2, H / 2
    if x1 == x2 and y1 == y2:
        print(W * H / 2 ,1)
    else:
        print(W * H / 2, 0)


W, H, x1, y1 = map(int, input().split())
solve()
