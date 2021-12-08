import math
with open("./inputs/7.txt") as f:
  positions = sorted([int(n) for n in f.read().split(',')])

  minimal = None
  for target in range(5000):
    distances = sum([abs(position - target) for position in positions])
    if not minimal or distances < minimal:
      minimal = distances
      print('new', target, distances)
  # before = 0
  # after = sum(positions)
  # for position in positions:
  #   before += position
  #   after -= position
  #   print(position, before, after)

  