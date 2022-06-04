N = int(input())
 
Nout=[]
Napp = []
 
for Ny in range(N):
  Napp = []
  for Nx in range(Ny + 1):
    Napp.append([])
  Nout.append(Napp)
 
for Nx in range(N):
  for Ny in range(Nx//2 + 1):
    Nxma  = -1 * (Ny + 1)
    # Nout[0][Ny] = 0
    if Ny == 0:
      Nout[Nx][Ny] = 1
      Nout[Nx][Nxma] = 1
    elif Nx > 1:
      Nout[Nx][Ny] = Nout[Nx-1][Ny] + Nout[Nx-1][Ny-1]
      Nout[Nx][Nxma] = Nout[Nx-1][Ny] + Nout[Nx-1][Ny-1]
    # print(Nx,Ny)
for Nx in range(N):
  Outstr = ' '.join([str(_) for _ in Nout[Nx]])
  print(Outstr)