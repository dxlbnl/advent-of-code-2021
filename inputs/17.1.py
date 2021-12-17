import re

input = 'target area: x=20..30, y=-10..-5'
[(xmin, xmax), (ymin, ymax)] = re.findall(r'\w=(-?\d+)\.\.(-?\d+)', input)


print((xmin, xmax), (ymin, ymax))

speed = 6
position = 0
for i in range(14):
  print(f'{i}: speed={speed} position={position}')
  position += speed
  speed -= 1
