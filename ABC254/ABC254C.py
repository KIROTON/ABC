import sys
 
def Change(Alist,N,Ni,K,Count):
  if Alist[Ni] > Alist[Ni + K]:
    Alist[Ni],Alist[Ni + K] = Alist[Ni + K],Alist[Ni]
 
    if N > Ni + K + K:
      Alist,Count=Change(Alist,N,Ni+K,K,Count)
    Count += 1
  return(Alist,Count)
 
N,K = (map(int, input().split()))
Alist = list(map(int, input().split()))
 
Arisou=sorted(Alist)
 
 
while(Alist != Arisou):
  Count = 0
  for Ni in range(N - K):
    if N > Ni + K:
      Alist,Count = Change(Alist,N,Ni,K,Count)
  if Count == 0:
    print('No')
    sys.exit()
print('Yes')