increases = 0
prev = None

with open("./inputs/1.txt") as f:
    for line in f:
        current = int(line)
        if prev and prev < current:
            increases += 1
        prev = current

print(increases)    