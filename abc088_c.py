def solve():
    rows_and_cols_sum = sum([c[i][i] for i in range(3)])
    total_sum = sum([sum(row) for row in c])
    print('Yes' if total_sum == 3 * rows_and_cols_sum else 'No')


c = []
for _ in range(3):
    c.append(list(map(int, input().split())))
solve()
