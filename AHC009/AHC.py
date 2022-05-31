
# def MoveStr_onediction(Outstr,Con):
#   OutputStr = ''
#   for _ in range(Con):
#     OutputStr += Outstr
#   return OutputStr

# #移動関数
# #引数
# #Start:移動開始位置
# #Goal :移動終了位置
# def MoveStr(Si,Sj, Ti ,Tj):
#   OutputStr = ''
#   Xspec = Si - Ti
#   Yspec = Sj - Tj
#   #左右
#   if Xspec > 0:
#     OutputStr += MoveStr_onediction('U',Xspec)
#   elif Xspec < 0:
#     OutputStr += MoveStr_onediction('D',Xspec*(-1))
#   #上下
#   if Yspec > 0:
#     OutputStr += MoveStr_onediction('L',Yspec)
#   elif Yspec < 0:
#     OutputStr += MoveStr_onediction('R',Yspec*(-1))
#   return OutputStr

import re

Si,Sj, Ti,Tj, P = map(float,input().split())

Si,Sj, Ti,Tj = int(Si), int(Sj), int(Ti), int(Tj)

H = []

for _ in range(20):
  H.append(list(map(str,input())))

V = []

for _ in range(19):
  V.append(list(map(str,input())))

#動的計画法で地図上の最短距離を移動距離を出力

#各マスの移動可能位置を出力
CanMoveCom = []
MoveCos = []
for Yi in range(20):
  CanMoveComRow = []
  MoveCosRow = []
  for Xi in range(20):
    ComStr = ''
    #D確認
    if Yi < 19:
      if V[Yi][Xi] != '1':
        ComStr += 'D'
    #U確認
    if Yi > 0 :
      if V[Yi-1][Xi] != '1':
        ComStr += 'U'
    #R確認
    if Xi < 19:
      if H[Yi][Xi] != '1':
        ComStr += 'R'
    #L確認
    if Xi > 0 :
      if H[Yi][Xi-1] != '1':
        ComStr += 'L'
      

    CanMoveComRow.append(ComStr)
    MoveCosRow.append(999)
  CanMoveCom.append(CanMoveComRow)
  MoveCos.append(MoveCosRow)

MoveCos[Si][Sj] = 0

Endflag = 1

for Dis_i in range(200):
  for MoveCosfor in MoveCos:
    if Dis_i in MoveCosfor:
      Endflag = 0
  if Endflag == 1:
    break
  for Yi in range(20):
      for Xi in range(20):
        if Dis_i == MoveCos[Yi][Xi]:
          if 'U' in CanMoveCom[Yi][Xi]:
            if MoveCos[Yi - 1][Xi] == 999:
              MoveCos[Yi - 1][Xi] = Dis_i + 1
          if 'D' in CanMoveCom[Yi][Xi]:
            if MoveCos[Yi + 1][Xi] == 999:
              MoveCos[Yi + 1][Xi] = Dis_i + 1
          if 'L' in CanMoveCom[Yi][Xi]:
            if MoveCos[Yi][Xi - 1] == 999:
              MoveCos[Yi][Xi - 1] = Dis_i + 1
          if 'R' in CanMoveCom[Yi][Xi]:
            if MoveCos[Yi][Xi + 1] == 999:
              MoveCos[Yi][Xi + 1] = Dis_i + 1

OutStr=''

#理想移動時のマス
LessComStr = ''
LessDis = MoveCos[Ti][Tj]
Mi = Ti
Mj = Tj
TouchTheWall = []

for Ni in range(LessDis):
  if 'U' in CanMoveCom[Mi][Mj]:
    if MoveCos[Mi - 1][Mj] == LessDis - Ni -1 :
      LessComStr = 'D' + LessComStr
      #壁の場合
      if not 'D' in CanMoveCom[Mi][Mj]:
        TouchTheWall.append(LessDis - Ni -1)
        # LessComStr = 'D' + LessComStr
        pass
      Mi -= 1
      continue
    
  if 'D' in CanMoveCom[Mi][Mj]:
    if MoveCos[Mi + 1][Mj] == LessDis - Ni -1 :
      LessComStr = 'U' + LessComStr
      #壁の場合
      if not 'U' in CanMoveCom[Mi][Mj]:
        TouchTheWall.append(LessDis - Ni -1)
        # LessComStr = 'U' + LessComStr
        pass
      Mi += 1 
      continue

  if 'L' in CanMoveCom[Mi][Mj]:
    if MoveCos[Mi][Mj - 1] == LessDis - Ni -1 :
      LessComStr = 'R' + LessComStr
      #壁の場合
      if not 'R' in CanMoveCom[Mi][Mj]:
        TouchTheWall.append(LessDis - Ni -1)
        # LessComStr = 'R' + LessComStr
        pass
      Mj -= 1 
      continue

  if 'R' in CanMoveCom[Mi][Mj]:
    if MoveCos[Mi][Mj + 1] == LessDis - Ni -1 :
      LessComStr = 'L' + LessComStr
      #壁の場合
      if not 'L' in CanMoveCom[Mi][Mj]:
        TouchTheWall.append(LessDis - Ni -1)
        # LessComStr = 'L' + LessComStr
        pass
      Mj += 1
      continue
for Ni in TouchTheWall:
  # print(Ni)
  TargetChr = LessComStr[Ni]
  NeedMoveMass = len(re.findall(TargetChr+'+$',LessComStr[:Ni+1]))
  for Mai in range(NeedMoveMass,200):
    #期待値が設定値以上になるのに必要な追加数を確認
    Endfor = 0
    #確率計算
    
    if 1 - (P ** Mai) > 0.9:
      for AddStr in range(Mai - NeedMoveMass):
        LessComStr = LessComStr[:Ni+1] + TargetChr + LessComStr[Ni+1:]
        Endfor = 1
    if Endfor == 1:
      break
print(LessComStr)
# Ri, Rj = Si, Sj
# BreakGo = 0
# IKITU = 0
# while Ri != Ti or Rj != Tj:
#   #縦方向
#   Di = Ri
#   # if IKITU == 0 and (BreakGo == 1 or BreakGo == 3):
#   NiStr = ''
  
#   # Min_i = min(Ri,Ti)


#   for Ni in range(min(Ri,Ti),max(Ri,Ti)):
#     NiStr += V[Ni][Rj]
  
#   if Ri > Ti:
#     for Ni in range(len(NiStr)):
#       Di += 1
#       if NiStr[-1 * Ni] == '1':
#         Di -= 1
#         break
#   elif Ri < Ti:
#     for Ni in range(len(NiStr)):
#       Di += 1
#       if NiStr[Ni] == '1':
#         Di -= 1
#         break

#   #横方向
#   Dj = Rj
#   # if IKITU == 0 and(BreakGo == 0 or BreakGo == 2):
#   NjStr = ''
  
#   for Nj in range(min(Rj,Tj),max(Rj,Tj)):
#     NjStr += H[Di][Nj-1]
#   if Rj > Tj:
#     for Nj in range(len(NjStr)):
#       Dj += 1
#       if NjStr[-1 * Nj] == '1':
#         Dj -= 1
#         break
#   elif Rj < Tj:
#     for Nj in range(len(NjStr)):
#       Dj += 1
#       if NjStr[Nj] == '1':
#         Dj -= 1
#         break

#   #行き詰った場合
#   if Ri == Di and Rj == Dj:
#     IKITU = 1
#     if BreakGo == 0:
#       OutStr += 'U'
#       Di -= 1
#     elif BreakGo == 1:
#       OutStr += 'R'
#       Dj += 1
#     elif BreakGo == 2:
#       OutStr += 'D'
#       Di += 1
#     elif BreakGo == 3:
#       OutStr += 'L'
#       Dj -= 1
#     BreakGo += 1
#     BreakGo %= 4
#   else:
#     IKITU = 0
  
#   OutStr += MoveStr(Ri,Rj, Di,Dj)
#   Ri,Rj = Di,Dj



# print(OutStr)

