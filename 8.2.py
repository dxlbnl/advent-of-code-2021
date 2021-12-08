
"""
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg

0 = abcefg  : 6 
1 = cf      : 2 
2 = acdeg   : 5  
3 = acdfg   : 5  
4 = bcdf    : 4
5 = abdfg   : 5  
6 = abdefg  : 6 
7 = acf     : 3 
8 = abcdefg : 7 
9 = abcdfg  : 6 
"""

def index(L, obj):
  try:
    return L.index(obj)
  except ValueError:
    return None

def map_signals(signals, output):
  options = [None for i in range(10)]

  all_signals = [set(signal) for signal in signals + output]
  sig5 = [signal for signal in all_signals if len(signal) == 5]
  sig6 = [signal for signal in all_signals if len(signal) == 6]

  # Cross of using simple signals
  for signal in all_signals:
    if len(signal) == 2:
      options[1] = signal
    elif len(signal) == 3:
      options[7] = signal
    elif len(signal) == 4:
      options[4] = signal
    elif len(signal) == 7:
      options[8] = signal

    # Other deductions
    if options[4] and not options[2]:
      # We can figure out number 2 from this
      for signal in sig5:
        if signal in options: continue
        if len({ s for s in signal if s in options[4]}) == 2:
          # We found nr 2
          options[2] = signal
          break
    if options[2] and not options[5]:
      # We can find 3 and 5 from this:
      for signal in sig5:
        if signal in options: continue
        if len({ s for s in signal if s in options[2]}) == 3:
          options[5] = signal
    if options[2] and options[5] and not options[3]:
      for signal in sig5:
        if signal not in options:
          # It must be 3
          options[3] = signal
    
    if options[5] and options[1] and not options[9]:
      for signal in sig6:
        if signal in options: continue
        if signal == options[1].union(options[5]):
          options[9] = signal
    if options[5] and options[9] and (not options[6] or not options[0]):
      for signal in sig6:
        if signal in options: continue
        elif len(signal - options[5]) == 1:
          options[6] = signal
        elif len(signal - options[5]) == 2:
          options[0] = signal

  result = [index(options, set(value)) for value in output]
  print('result', result)
  return int(''.join([str(n) for n in result]))


with open("./inputs/8.txt") as f:
  s = 0
  for line in f:
    [signal, output] = [
      part.strip().split(' ') for part in line.split('|')
    ]
    s += map_signals(signal, output)
  print(s)



  