def solve():
    if m < 100:
        print('00')
    elif 100 <= m <= 5000:
        print(str(m // 100).zfill(2))
    elif 6000 <= m <= 30000:
        print(50 + m // 1000)
    elif 35000 <= m <= 70000:
        print((m // 1000 - 30) // 5 + 80)
    elif 70000 <= m:
        print(89)


m = int(input())
solve()
