def solve():
    if B.find('.') == -1:
        b = int(B)
    else:
        count = B.index('.')
        b = int(B[: count] + B[count + 1: ])
    print(int(int(A) * b // pow(10, len(B) - 1 - count)))

A, B = input().split()
solve()
