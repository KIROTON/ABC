import math

N = int(input())

Count = 0

for Nx in range(1,N+1):
  for Ny in range(1,Nx+1):
    X = math.sqrt(Nx*Ny)
    if X % 1 == 0:
      if Nx == Ny:
        Count+=1
      else:
        Count+=2
      # print(Nx,Ny,X)

print(Count)