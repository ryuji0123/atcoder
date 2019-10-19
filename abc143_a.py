if __name__ == '__main__':
    A, B = map(int, input().split())
    if A <= 2 * B:
        print(0)
    else:
        print(A - 2 * B)
