def solve():
    keys = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    d = {k: idx for idx, k in enumerate(keys)}
    print(d['Saturday'] - d[day] if day not in ['Sunday', 'Saturday'] else 0)


day = input()
solve()
