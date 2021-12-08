import math

area = lambda n: int((n * n) / 2 + n/2)

with open("./inputs/7.txt") as f:
  positions = sorted([int(n) for n in f.read().split(',')])

  minimal = None
  for target in range(5000):
    distances = sum([area(abs(position - target)) for position in positions])
    if not minimal or distances < minimal:
      minimal = distances
      print('new', target, distances)

  