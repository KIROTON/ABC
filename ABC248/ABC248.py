

S1,S2,S3 = map(str,input().split())
T1,T2,T3 = map(str,input().split())

Count = 0

if not S1 == T1:
  Count += 1
if not S2 == T2:
  Count += 1
if not S3 == T3:
  Count += 1

if Count == 0:
  print('Yes')
elif Count == 2:
  print('No')
elif Count == 3:
  print('Yes')