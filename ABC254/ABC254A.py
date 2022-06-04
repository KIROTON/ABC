N = int(input())
 
Nout = N % 100
 
if Nout >= 10:
  print(Nout)
else:
  print(f"0{Nout}")