N = int(input())
S = input()
#ret = str([chr(ord(s) + N) for s in S])
ret = ''

for s in S:
    if ord(s) + N <= ord('Z'):
        ret += chr(ord(s) + N) 
    else:
        ret += chr(ord(s) + N - ord('Z') + ord('A') - 1)

print(ret)
