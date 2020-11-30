def solve():
    free_colors = 0
    colors = set()
    for a in A:
        if 3200 <= a:
            free_colors += 1
        else:
            colors.add(a // 400)
    print(max(1, len(colors)), len(colors) + free_colors)


N = input()
A = list(map(int, input().split()))
solve()
