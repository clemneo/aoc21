def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def mapmaker(map_size):
  map_array = []
  for i in range(map_size):
    map_row = [0]*map_size
    map_array.append(map_row)
  return map_array

def map_printer(map_array):
  for maprow in map_array:
    string = ''
    for num in maprow:
      if num == 0: 
        string += '.'
      else:
        string += str(num)
    print(string)

def solver(part):
  lines = open_file('input/day05.txt')
  map_size = 1000
  ventlines = []
  map_array = mapmaker(map_size)

  for line in lines:
    x1y1, x2y2 = line.split(' -> ')
    x1, y1 = list(map(int, x1y1.split(',')))
    x2, y2 = list(map(int, x2y2.split(',')))

    if part==1:
      if x1 != x2 and y1 != y2:
        continue
    elif part == 2:
      pass
    vent = {}
    vent['x1'] = x1
    vent['x2'] = x2
    vent['y1'] = y1
    vent['y2'] = y2
    ventlines.append(vent)

  # Note: did not take into account 0 indexing here, but there isn't a 1000 input so it doesnt break
  for vent in ventlines:
    # making horizontal lines
    if vent['x1'] == vent['x2']:
      if vent['y1'] < vent['y2']:
        for i in range(vent['y1'], vent['y2']+1):
          map_array[vent['x1']][i] += 1
      else:
        for i in range(vent['y2'], vent['y1']+1):
          map_array[vent['x1']][i] += 1
    # making vertical lines
    elif vent['y1'] == vent['y2']:
      if vent['x1'] < vent['x2']:
        for i in range(vent['x1'], vent['x2']+1):
          map_array[i][vent['y1']] += 1
      else:
        for i in range(vent['x2'], vent['x1']+1):
          map_array[i][vent['y1']] += 1
    # making diagonal lines
    else:
      if vent['x1'] < vent['x2']:
        length = vent['x2'] - vent['x1']
        if vent['y1'] < vent['y2']: # if its a / from bottom left to top right
          for i in range(length+1):
            map_array[vent['x1']+i][vent['y1']+i] += 1
        else: # if its a \ from top left to bottom right
          for i in range(length+1):
            map_array[vent['x1']+i][vent['y1']-i] += 1
      else: 
        length = vent['x1'] - vent['x2']
        if vent['y1'] < vent['y2']: # if it's a \ from bottom right to top left
          for i in range(length+1):
            map_array[vent['x1']-i][vent['y1']+i] += 1
        else: # if its a / from top right to bottom left
          for i in range(length+1):
            map_array[vent['x1']-i][vent['y1']-i] += 1

  total_overlap = 0
  for row in map_array:
    for coord in row:
      if coord > 1:
        total_overlap += 1
  return total_overlap

print(solver(2))
