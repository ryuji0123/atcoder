def solve():
    N = len(S)
    d = list('atcoder@')
    score = {k: 1 for k in 'atcoder'}
    score['@'] = 10
    for i in range(ord('a') + 1, ord('z') + 1):
        c = chr(i)
        if c not in score:
            score[c] = 0
    for idx in range(N):
        if S[idx] != T[idx] and score[S[idx]] + score[T[idx]] <= 10:
            print('You will lose')
            return
    print('You can win')

S = input()
T = input()
solve()
