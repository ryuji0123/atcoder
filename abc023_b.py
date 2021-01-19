def solve():
    s = 'b'
    n = 0
    while len(s) <= N:
        if s == S:
            print(n)
            return
        n += 1
        if n % 3 == 0:
            s = 'b' + s + 'b'
        elif n % 3 == 1:
            s = 'a' + s + 'c'
        else:
            s = 'c' + s + 'a'
    print(-1)


N = int(input())
S = input()
solve()
