N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

def getScore(t, R, S, P):
    if t == 'r':
        return P
    if t == 's':
        return R
    return S

latest = [{'string': '', 'count': 0} for _ in range(K)]

ret = 0
for idx, t in enumerate(T):
    latest_idx = idx % K
    if idx + 1 <= K or t != latest[latest_idx]['string']:
        ret += getScore(t, R, S, P)
        latest[latest_idx]['string'] = t
        latest[latest_idx]['count'] = 1
        continue

    if latest[latest_idx]['count'] % 2 == 0:
        ret += getScore(t, R, S, P)
    latest[latest_idx]['count'] += 1

print(ret)