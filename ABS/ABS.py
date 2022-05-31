import sys
import re
S = str(input())

Texts = ['dream','dreamer','erase','eraser']


while len(S)>0:
  checkerr=0
  for oneText in Texts:
    if S.endswith(oneText):
      S=S[:-1 * len(oneText)]
      checkerr = 1
      break

  if checkerr == 0 and len(S)>0:
    print('NO')
    sys.exit()


print('YES')
