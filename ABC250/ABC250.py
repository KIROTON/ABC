


N,A,B = map(int,input().split())
# R,C = map(int,input().split())

Hanten = 0

OutStr = ''
SWtaill = ''
SBtaill = ''

for Bi in range(B):
  SWtaill += '.'
  SBtaill += '#'

for Nyi in range(N * A):
  for Nxi in range(N):
    if Nxi % 2 == Hanten:
      OutStr += SWtaill
    else:
      OutStr += SBtaill

  if Nyi % A == 0 and Nyi > 0:
    if Hanten == 0:
      Hanten = 1
    else:
      Hanten = 0
  print(OutStr)
  OutStr = ''



  
# print(OutStr)
pass