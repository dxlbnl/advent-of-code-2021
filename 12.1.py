import string
from collections import defaultdict

connections = defaultdict(list)

def step(position, path):
  if position == 'end':
    return [path]

  paths = []
  for point in connections[position]:
    if point.islower() and point in path:
      continue

    paths += step(point, path + (point, ))

  return paths

with open("./inputs/12.txt") as f:
  for line in f:
    [a, b] = line.strip().split('-')

    connections[a].append(b)
    if not (a == 'start' or b == 'end'):
      connections[b].append(a)
  
  paths = step('start', ('start', ))
  print('\n'.join([str(l) for l in paths]))
  print(len(paths))


  