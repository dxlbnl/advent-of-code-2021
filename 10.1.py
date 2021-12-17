
brackets = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}
errors = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

with open("./inputs/10.txt") as f:
  count = 0
  for line in f:
    stack = []
    for char in line.strip():
      if char in brackets:
        stack.append(brackets[char])
      else:
        expected = stack.pop()

        if char != expected:
          print("Error: found {} expected {}".format(char, expected))
          count += errors[char]
          
  print(count)


  