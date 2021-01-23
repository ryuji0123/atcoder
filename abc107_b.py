def solve():
    skipped_rows = [all(a[row][i] == '.' for i in range(W)) for row in range(H)]
    skipped_cols  = [all(a[i][col] == '.' for i in range(H)) for col in range(W)]
    for i in range(H):
        need_print = False
        for j in range(W):
            if skipped_rows[i] or skipped_cols[j]:
                continue
            print(a[i][j], end='')
            need_print = True
        if need_print:
            print()


H, W = map(int, input().split())
a = [input() for _ in range(H)]
solve()
