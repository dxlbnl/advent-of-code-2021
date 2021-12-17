
with open("./inputs/15.txt") as f:
  riskmap = [
    [int(x) for x in line.strip()]
    for line in f
  ]
  print('\n'.join([''.join(str(c) for c in l) for l in riskmap]))

  width = len(riskmap[0])
  height = len(riskmap)

  end = (width-1, height-1)
  queue = [((0,0), 0)]
  visited = set()
  in_queue = set()

  print('looking for', end)
  def visit(position, risk):
    if position not in visited and position not in in_queue:
      newrisk = risk + riskmap[position[0]][position[1]]
      if position == end:
        print("Found end:", newrisk)
        return True
      in_queue.add(position)
      queue.append((position, newrisk))

  for step in range(10000):
    queue.sort(key=lambda i: i[1])
    (position, risk)  = queue.pop(0)
    print(step, position, risk)
    visited.add(position)
    (x, y) = position

    if x > 0:
      if visit((x-1, y), risk): break
    if x < width-1:
      if visit((x+1, y), risk): break
    if y > 0:
      if visit((x, y-1), risk): break
    if y < height-1:
      if visit((x, y+1), risk): break
    
    # print(step, risk, position, queue)
