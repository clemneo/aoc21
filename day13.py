def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def get_array(input):
  output_array = []
  max_x = 0
  max_y = 0
  min_x = 9999
  min_y = 9999
  for line in input:
    if line == '\n':
      break
    else:
      line = line.strip()
      line = list(map(int,line.split(',')))
      if line[0] > max_x:
        max_x = line[0]
      if line[0] < min_x:
        min_x = line[0]
      if line[1] > max_y:
        max_y = line[1]
      if line[1] < min_y:
        min_y = line[1]
 
  for i in range(min_y, max_y+1):
    output_array.append([0]*(max_x-min_x+1))
    for line in input:
      if line == '\n':
        break
      else:
        continue
  for line in input:
    if line == '\n':
      break
    else:
      line = line.strip()
      line = list(map(int,line.split(',')))
      output_array[line[1]-min_x][line[0]-min_y] = 1
  return output_array
    
def print_paper(array):
  for line in array:
    for num in line:
      if num != 0: 
        print('#', end="")
      else:
        print('.',end="")
    print()

def get_folds(input):
  folds = []
  folding_now = False
  for i in range(len(input)):
    if input[i] == '\n':
      folding_now = True
    elif folding_now:
      text = input[i][11:].strip()
      direction, num = text.split("=")
      folds.append((direction, int(num)))
  return folds
  
def fold_paper(input_array, fold):
  x_length = len(input_array[0])
  print('x_length is ', x_length)
  y_length = len(input_array)
  print('y_length is ', y_length)
  if fold[0] == 'x': # fold left-right
    for i in range(y_length): # for every row
      for j in range(1,fold[1]+1): # from 1 to <foldplace>
        try:
          input_array[i][fold[1]-j] += input_array[i][fold[1]+j]
        except:
          pass # Quick fix for index error that works somehow lol
    output_array = []
    for i in range(len(input_array)):
      output_array.append(input_array[i].copy()[0:fold[1]])
    return output_array
  elif fold[0] == 'y': # fold top-down
    for i in range(x_length): # for every column, from 0 to
      for j in range(1,fold[1]+1): # from 1 to <foldplace>
        try:
          input_array[fold[1]-j][i] += input_array[fold[1]+j][i]
        except:
          pass # Quick fix for index error that works somehow lol
    return input_array[0:fold[1]]


def solver(part):
  input = open_file('input/day13.txt')
  array = get_array(input)
  folds = get_folds(input)
  if part == 1:
    # print(folds)
    array = fold_paper(array, folds[0])
    total_dots = 0
    for line in array:
      for num in line:
        if num != 0:
          total_dots += 1
    return total_dots
  if part == 2:

    for fold in folds:
      array = fold_paper(array, fold)
    print_paper(array)
    return array


print("Part 1: ", solver(1))
print("Part 2: ", solver(2))