if __name__ == '__main__':
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    if len(X) <= N:
        print(0)
        exit()

    diff = sorted([X[idx + 1] - x for idx, x in enumerate(X[:-1])], reverse=True)
    print(sum(diff[N - 1:]))
