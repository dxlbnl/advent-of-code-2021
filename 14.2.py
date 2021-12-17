from collections import defaultdict

with open("./inputs/14.txt") as f:
  polymer = f.readline().strip()
  insertion_ops = {}

  # Group by all pairs
  pairs = defaultdict(int)
  for index in range(1, len(polymer)):
    pairs[polymer[index-1:index+1]] += 1

  print(pairs)
  for line in f:
    if line.strip():
      [search, insert] = line.strip().split(' -> ')
      insertion_ops[search] = insert

  for step in range(40):
    polymer = dict(pairs)
    print(step, polymer)
    for search in insertion_ops:
      if search in polymer:
        amount = polymer[search]
        n1 = search[0] + insertion_ops[search]
        n2 = insertion_ops[search] + search[1]
        # print("replace", amount, search, '->', n1, n2)
        pairs[search] -= amount
        pairs[n1] += amount
        pairs[n2] += amount

  counts = defaultdict(int)
  for pair in pairs:
    counts[pair[0]] += pairs[pair]
    counts[pair[1]] += pairs[pair]
  
  frequencies = sorted(counts.values())

  print(counts, frequencies[-1]/2 - frequencies[0]/2)


  