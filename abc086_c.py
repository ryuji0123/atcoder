def solve():
    cur_t = cur_x = cur_y = 0
    for t, x, y in plan:
        diff_t = t - cur_t
        diff_x = abs(x - cur_x)
        diff_y = abs(y - cur_y)
        
        if diff_t < diff_x + diff_y or (diff_t - (diff_x + diff_y)) % 2 != 0:
            print('No')
            return

        cur_t = t
        cur_x = x
        cur_y = y

    print('Yes')


N = int(input())
plan = [list(map(int, input().split())) for _ in range(N)]
solve()
