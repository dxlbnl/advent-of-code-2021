import math
brackets = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}
errors = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}

with open("./inputs/10.txt") as f:
  counts = []
  for line in f:
    stack = []
    for char in line.strip():
      if char in brackets:
        stack.append(brackets[char])
      else:
        expected = stack.pop()

        if char != expected:
          break
    else:
      if stack:
        count = 0
        print("incomplete", stack[::-1])
        for c in stack[::-1]:
          count *= 5
          count += errors[c]
        counts.append(count)
  print(sorted(counts)[math.floor(len(counts)/2)])


  