COST = 0
START = 1
FREQ = 2

def solve():
    for i in range(N):
        time = info[i][START] + info[i][COST]
        i += 1
        while i < N:
            if time <= info[i][START]:
                time = info[i][START] + info[i][COST]
            elif (time - info[i][START]) % info[i][FREQ] == 0:
                time += info[i][COST]
            else:
                time = info[i][FREQ] * (time // info[i][FREQ] + 1) + info[i][COST]
            i += 1
        print(time)
    print(0)


N = int(input()) - 1
info = [list(map(int, input().split())) for _ in range(N)]
solve()
