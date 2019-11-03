if __name__ == '__main__':
    N, K = map(int, input().split())
    string = input()
    count = 0
    for idx in range(N - 1):
        if string[idx] == string[idx + 1]: count += 1
    print(min(N - 1, count + 2 * K))
