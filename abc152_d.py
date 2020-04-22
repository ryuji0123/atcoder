def solve(N):
    ret = 0
    counter = [[0 for _ in range(10)] for _ in range(10)]
    for n in range(1, N + 1):
        i, j = map(int, [str(n)[0], str(n)[-1]])
        counter[i][j] += 1

    for i in range(10):
        for j in range(10):
            ret += counter[i][j] * counter[j][i]
    return ret


if __name__ == '__main__':
    N = int(input())
    ret = solve(N)
    print(ret)