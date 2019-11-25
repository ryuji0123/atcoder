X,Y = map(int,input().split())

MOD = 10**9 + 7
FAC = [1]
INV = [1]
for i in range(1,X+Y+1):
  FAC.append((FAC[i-1]*i) % MOD)
  INV.append(pow(FAC[-1],MOD-2,MOD))

def nCr(n,r):
  return FAC[n]*INV[n-r]*INV[r]

a = (2*X-Y)/3
b = (2*Y-X)/3
if a>=0 and b>=0 and a.is_integer() and b.is_integer():
  print(nCr(int(a)+int(b),min(int(a),int(b)))%MOD)
else:
  print(0)

