import datetime


def solve():
    cur = datetime.datetime(year=Y, month=M, day=D)
    while True:
        y, m, d = map(int, str(cur.date()).split('-'))
        if y % (m * d) == 0:
            print(f'{y}/{str(m).zfill(2)}/{str(d).zfill(2)}')
            return
        cur += datetime.timedelta(days=1)

Y, M, D = map(int, input().split('/'))
solve()
