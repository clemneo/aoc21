def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def is_bingo(grid, drawn_nos):
  has_bingo = has_horizontal_bingo(grid, drawn_nos) or has_vertical_bingo(grid, drawn_nos) # or has_diagonal_bingo(grid, drawn_nos)
  return has_bingo


def has_diagonal_bingo(grid, drawn_nos):
  grid_size = len(grid)
  i = j = 0
  while i < grid_size:
    if not grid[i][j] in drawn_nos:
      break
    if i == grid_size-1:
      return True
    i += 1
    j += 1
  i = 0
  j = grid_size-1
  while i < grid_size:
    if not grid[i][j] in drawn_nos:
      break
    if i == grid_size-1:
      return True
    i += 1
    j -= 1
  return False

def has_horizontal_bingo(grid, drawn_nos):
  grid_size = len(grid)
  i = 0
  for i in range(grid_size):
    for j in range(grid_size):
      if not grid[i][j] in drawn_nos:
        break
      if j == grid_size-1:
        return True
  return False

def has_vertical_bingo(grid, drawn_nos):
  grid_size = len(grid)
  i = 0
  for i in range(grid_size):
    for j in range(grid_size):
      if not grid[j][i] in drawn_nos:
        break
      if j == grid_size-1:
        return True
  return False

def get_score(grid, current_numbers):
  last_number = current_numbers[-1]
  sum_of_unmarked = 0
  for grid_row in grid:
    for num in grid_row:
      if not num in current_numbers:
        sum_of_unmarked += num
  return last_number * sum_of_unmarked


def solver(part):
  size_of_grid = 5

  lines = open_file('input/day04.txt')
  drawn_nos = list(map(int,lines[0].split(',')))
  grids = []

  i = 0
  while i<len(lines):
    grid = []
    if lines[i] == '\n':
      for j in range(size_of_grid):
        gridline = list(map(int,lines[i+j+1].split()))
        grid.append(gridline)
      grids.append(grid)
    i += 1

  if part == 1:
    for count in range(size_of_grid-1, len(drawn_nos)):
      current_numbers = drawn_nos[:count]
      for grid in grids:
        if is_bingo(grid, current_numbers):
          return(get_score(grid, current_numbers))
  elif part == 2:
    for count in range(size_of_grid-1, len(drawn_nos)):
      current_numbers = drawn_nos[:count]
      if len(grids) == 1:
        return get_score(grids[0], current_numbers)
      j = 0
      while j < len(grids):
        if is_bingo(grids[j], current_numbers):
          grids.pop(j)
        else:
          j += 1
          # return(get_score(grid, current_numbers))
    
print('Part 1: ', solver(1))
print('Part 2: ', solver(2))