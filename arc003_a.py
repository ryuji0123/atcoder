def solve():
    d = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    print(sum([d[r] for r in rates]) / N)

N = int(input())
rates = input()
solve()
