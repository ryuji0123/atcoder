def solve():
    A = [100, 100, 200]
    idx = 3
    while idx < 20:
        A.append(sum(A[-3: ]))
        idx += 1
    print(A[-1])


solve()
