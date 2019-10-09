div = 2019
if __name__ == '__main__':
    L, R = [int(i) for i in input().split()]
    if R - L > div - 1:
        R = L + div - 1
    number_ref = [num for num in range(L, R + 1, 1)]
    
    min_mod = 2018
    for idx, i in enumerate(number_ref):
        for j in number_ref[idx + 1:]:
            if (i * j) % div < min_mod:
                min_mod = (i * j) % div
    print(min_mod)
