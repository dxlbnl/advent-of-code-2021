increases = 0
prev = None
window = []

i =0

with open("./inputs/1.txt") as f:
    for line in f:
        value = int(line)
        window = (list(map(lambda i: i+value, window)) + [value])[-3:]

        if len(window) == 3:
            current = window[0]

            if prev and prev < current:
                increases += 1
            prev = current

print(increases)    