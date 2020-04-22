def solve(K):
    ref = [[['0'], ['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']]]
    if K < 10:
        return ref[0][K][0]

    rest = K - 9
    i = 0
    while True:
        i += 1
        ref.append([[] for _ in range(10)])
        for j in range(10):
            if j == 0:
                for r in ref[i-1][j] + ref[i-1][j+1]:
                    ref[i][j].append(str(j) + r)
            elif j == 9:
                for r in ref[i-1][j-1] + ref[i-1][j]:
                    ref[i][j].append(str(j) + r)
                    rest -= 1
                    if rest == 0:
                        return str(j) + r
            else:
                for r in ref[i-1][j-1] + ref[i-1][j] + ref[i-1][j+1]:
                    ref[i][j].append(str(j) + r)
                    rest -= 1
                    if rest == 0:
                        return str(j) + r

if __name__ == '__main__':
    K = int(input())
    print(solve(K))