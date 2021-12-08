
with open("./inputs/6.txt") as f:
  # Parse input
  fish = [int(n) for n in f.read().strip().split(',')]

  # Group them by age
  fish = [len([1 for age in fish if age == agegroup]) for agegroup in range(9)]

  for day in range(256):
    spawn, *fish = fish
    fish[6] += spawn
    fish += [spawn]

  print(sum(fish))


  