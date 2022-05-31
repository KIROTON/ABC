

def PartRoop(Outputlist,N,Output):
  for index,Ni in enumerate(N):
    if not N[index] in [R[0] for R in Outputlist]:
      Nipart = N[index] // 2
      N[index] -= Nipart
      N.append(Nipart)
      if N[index] in [R[0] for R in Outputlist] and \
          Nipart in [R[0] for R in Outputlist]:
        Kakeru = 1
        for index2,Output in enumerate(Outputlist):
          if N[index2] == Outputlist[index2][0]:
            print(Outputlist[index2])
            Kakeru *=  Outputlist[index2][1]
          if Nipart == Outputlist[index2][0]:
            print(Outputlist[index2])
            Kakeru *=  Outputlist[index2][1]
        Outputlist.append([N[index]+Nipart,Kakeru])
    # if N[index] > 4:
    #   Nipart = N[index] // 2
    #   N[index] -= Nipart
    #   if Nipart > 4:
    #     N.append(Nipart)
    #   else:
    #     Output *= Nipart
    #     Output %= 998244353
  return Outputlist,Output


N = []
Outputlist = [[2,2],[3,3],[4,4]]

N.append(int(input()))

Output = 1

while(not max(N) in [R[0] for R in Outputlist]):
  # Outputlist,Output = PartRoop(Outputlist,N,Output)
  for index,Ni in enumerate(N):
    if not N[index] in [R[0] for R in Outputlist]:
      Nipart = N[index] // 2
      N[index] -= Nipart
      N.append(Nipart)
      if N[index] in [R[0] for R in Outputlist] and Nipart in [R[0] for R in Outputlist]:
        Kakeru = 1
        for index2,Output in enumerate(Outputlist):
          if N[index] == Outputlist[index2][0]:
            Kakeru *=  Outputlist[index2][1]
          if Nipart == Outputlist[index2][0]:
            Kakeru *=  Outputlist[index2][1]
        Outputlist.append([N[index]+Nipart,Kakeru])
  print(N)
  # print(Output)
  print(Outputlist)



for Ni in N:
  Output *= Ni
  Output %= 998244353
print(Output)