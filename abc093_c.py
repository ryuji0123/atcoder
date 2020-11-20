def solve():
    target = nums[-1]
    while True:
        diff = sum([target - n for n in nums])
        if diff % 2 == 0:
            print(diff // 2)
            return
        target += 1

nums = sorted(list(map(int, input().split())))
solve()
