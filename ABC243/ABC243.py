from functools import lru_cache
import math

@lru_cache
def Outpartlist(Input):
  sqrtInp = math.ceil(sqrt(i))
  

def Anserout(Input):
  Listi = [Input]
  Outpartlist(Listi)
  pass


N = int(input())
T = []

for _ in range(N):
  T.append(int(input()))

for Nx in range(N):
  print(Anserout(T[Nx]))
