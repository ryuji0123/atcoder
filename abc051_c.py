def solve():
    ret = []
    x, y = sx, sy
    for _ in range(ty - y):
        ret.append('U')
    for _ in range(tx - x):
        ret.append('R')

    x, y = tx, ty
    for _ in range(y - sy):
        ret.append('D')
    for _ in range(x - sx):
        ret.append('L')
    ret.append('L')

    x, y = sx - 1, sy
    for _ in range(ty + 1 - y):
        ret.append('U')
    for _ in range(tx - x):
        ret.append('R')
    ret.append('D')
    ret.append('R')
    
    x, y = tx + 1, ty
    for _ in range(y - (sy - 1)):
        ret.append('D')
    for _ in range(x - sx):
        ret.append('L')
    ret.append('U')

    print(''.join(ret))


sx, sy, tx, ty = map(int, input().split())
solve()
