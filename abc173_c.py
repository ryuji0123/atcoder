def valid(selected_rows, selected_cols):
    return sum([r not in selected_rows and c not in selected_cols and matrix[r][c] == '#' for r in range(H) for c in range(W)]) == K


def solve():
    ret = 0
    for ri in range(pow(2, H)):
        selected_rows = set()
        for rj in range(H):
            if ri >> rj & 1:
                selected_rows.add(rj)

        for ci in range(pow(2, W)):
            selected_cols = set()
            for cj in range(W):
                if ci >> cj & 1:
                    selected_cols.add(cj)
            
            ret += valid(selected_rows, selected_cols)
    print(ret)


H, W, K = map(int, input().split())
matrix = []
for _ in range(H):
    matrix.append(list(input()))
solve()
