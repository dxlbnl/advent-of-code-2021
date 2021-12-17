width = 100
height = 100

def get(l, pos):
  (x, y) = pos
  if 0 <= x < width and 0 <= y < height:
    return l[x+y*width]
  return 9999

with open("./inputs/9.txt") as f:
  heightmap = [
    int(p)
      for line in f
      for p in line.strip()
  ]
  s = 0

  for y in range(height):
    for x in range(width):
      print(x,y)
      point = get(heightmap, (x, y))
      left = get(heightmap, (x-1, y))
      right = get(heightmap, (x+1, y))
      top = get(heightmap, (x, y-1))
      bottom = get(heightmap, (x, y+1))

      if left > point < right and top > point < bottom:
        print((x,y),point,(left, right), (top, bottom))
        s += 1 + point
  # print("\n".join(["{}".format(heightmap[y*width:y*width+width]) for y in range(height)]))
  print("V", s)


  