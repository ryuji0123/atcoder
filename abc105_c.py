def solve(N):
    if (N == 0): 
        print('0') 
        return
      
    ret = []
    while (N != 0): 
        div = int(N / NEG_BASE)
        remainder = N - NEG_BASE * div
        if remainder < 0:
            div += 1
            remainder -= NEG_BASE
        N = div
        ret.append(str(remainder))
    print(''.join(reversed(ret)))


NEG_BASE = -2
N = int(input())
solve(N)
