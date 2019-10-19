if __name__ == '__main__':
    N, K = map(int, input().split())
    height = sorted([int(input()) for n in range(N)])
    s =  [ height[idx + K - 1] - h for idx, h in enumerate(height)
            if idx + K - 1 < len(height)
    ]
    print(min(s))
