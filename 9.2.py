import math
width = 100
height = 100

left = lambda pos: (pos[0]-1, pos[1],)
right = lambda pos: (pos[0]+1, pos[1],)
top = lambda pos: (pos[0], pos[1]-1,)
bottom = lambda pos: (pos[0], pos[1]+1,)

with open("./inputs/9.txt") as f:
  heightmap = [
    int(p)
      for line in f
      for p in line.strip()
  ]

  def get(position):
    (x,y) = position
    if 0 <= x < width and 0 <= y < height:
      return heightmap[x+y*width]
    return 9

  def mapbasin(position, done = set()):
    if position in done: return 0

    basin = 1
    point = get(position)
    done.add(position)

    if point < get(left(position)) != 9:
      basin += mapbasin(left(position), done)
    if point < get(right(position)) != 9:
      basin += mapbasin(right(position), done)
    if point < get(top(position)) != 9:
      basin += mapbasin(top(position), done)
    if point < get(bottom(position)) != 9:
      basin += mapbasin(bottom(position), done)
    
    return basin

  basins = []

  for y in range(height):
    for x in range(width):
      pos = (x,y)
      point = get(pos)

      if get(left(pos)) > point < get(right(pos)) and get(top(pos)) > point < get(bottom(pos)):
        basins.append(mapbasin(pos))

  print(math.prod(sorted(basins)[-3:]))
  # print("\n".join(["{}".format(heightmap[y*width:y*width+width]) for y in range(height)]))


  