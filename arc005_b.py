def solve():
    diff = [0, 0]
    if 'D' in W:
        diff[0] = 1
    elif 'U' in W:
        diff[0] = -1

    if 'R' in W:
        diff[1] = 1
    elif 'L' in W:
        diff[1] = -1

    step = 0
    ret = []
    i, j = x - 1, y - 1

    while step < 4:
        ret.append(c[i][j])
        if  not(0 <= i + diff[0] < 9):
            diff[0] *= -1
        i += diff[0]

        if  not(0 <= j + diff[1] < 9):
            diff[1] *= -1
        j += diff[1]
        step += 1
    print(''.join(ret))


y, x, W = input().split()
x, y = map(int, [x, y])
c = [input() for _ in range(9)]
solve()
