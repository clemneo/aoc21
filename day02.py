def trackposdepth(file):
  aim = 0
  horizontal = 0
  depth = 0
  with open (file, 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
      wordArray = lines[i].split()
      word = wordArray[0]
      num = int(wordArray[1])
      # horizontal, depth = update(word, num, horizontal, depth)
      horizontal, depth, aim = update_with_aim(word, num, horizontal, depth, aim)
  return (horizontal, depth, aim)

def update_with_aim(word, num, horizontal, depth, aim):
  if word == 'forward':
    horizontal += num
    depth += aim*num
  elif word == 'down':
    aim += num
  elif word == 'up':
    aim -= num
  return horizontal, depth, aim

def update(word, num, horizontal, depth):
  if word == 'forward':
    horizontal += num
  elif word == 'down':
    depth += num
  elif word == 'up':
    depth -= num
  return horizontal, depth

info = trackposdepth('day02.txt')
print('Horizontal: ', info[0])
print('Depth:      ', info[1])
print('Product:    ', info[0]*info[1])