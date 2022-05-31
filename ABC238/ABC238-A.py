from socket import ntohl


N = int(input())
Nmod=998244353

Ndiff=1
NTotal = 0


while(not N%Ndiff == N):
  if N>Ndiff*10:
    Nadd = Ndiff * 10 - Ndiff
  else:
    Nadd = N          - Ndiff +1
  NTotal += int (Nadd*(Nadd+1)/2)
  NTotal = NTotal % Nmod
  # print(Ndiff)
  Ndiff *= 10


print(NTotal)