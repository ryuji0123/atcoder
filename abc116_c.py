def merge(height):
    if len(height) == 0:
        return 0
    if len(height) == 1:
        return height[0]
    m = min(height)
    m_idx = height.index(m)
    height = [h - m for h in height]
    left_height = height[:m_idx]
    right_height = height[m_idx + 1:]
    return  merge(left_height) + merge(right_height) + m

if __name__ == '__main__':
    N = int(input())
    h = list(map(int, input().split()))
    print(merge(h))
