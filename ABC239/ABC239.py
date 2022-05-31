import sys

def CheckHashi(N,M,A,B,NNeed,Ni):
  if NNeed[Ni] == 0:
    CheckHashi(N,M,A,B,NNeed)
  return 1

N,M = map(int,input().split())

D = list(map(int,input().split()))

if M > 0:

  AB = [map(int, input().split()) for _ in range(M)]

  A,B = x, y = [list(i) for i in zip(*AB)]
else:
  print(-1)
  sys.exit()

NHashi=[]

for Ni in range(0,N):
  NHashi.append(0)

for Mi in range(0,M):
  NHashi[A[Mi] - 1] += 1
  NHashi[B[Mi] - 1] += 1

NNeed = []

for Ni in range(0,N):
  NNeed.append(D[Ni] - NHashi[Ni])

for Ni in range(N):
  CheckHashi(N,M,A,B,NNeed,Ni)


print(NNeed)