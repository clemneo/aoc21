def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def find_low_points(heightmap):
  max_height = 9
  low_points = []

  for i in range(len(heightmap)): # for column
    for j in range(len(heightmap[0])): # for row
      low_point = True
      if i != 0:
        top = heightmap[i-1][j]
      else:
        top = max_height
      if i != len(heightmap)-1:
        bottom = heightmap[i+1][j]
      else:
        bottom = max_height
      if j != 0:
        left = heightmap[i][j-1]
      else: 
        left = max_height
      if j != len(heightmap[0])-1:
        right = heightmap[i][j+1]
      else:
        right = max_height
      adjacent = (top, bottom, left, right)
      for num in adjacent:
        # print(num)
        if heightmap[i][j] >= num:
          low_point = False
          break
      if low_point:
        low_points.append((i,j))
        
  return low_points

def find_basin(heightmap, starting_point, points):
  points.append(starting_point)

  # Finding neighbours
  top = (starting_point[0]-1, starting_point[1]) if starting_point[0] != 0 else None
  bottom = (starting_point[0]+1, starting_point[1]) if starting_point[0] != len(heightmap)-1 else None
  left = (starting_point[0], starting_point[1]-1) if starting_point[1] != 0 else None
  right = (starting_point[0], starting_point[1]+1) if starting_point[1] != len(heightmap[0])-1 else None
  neighbours = (top, bottom, left, right)

  starting_point_value = heightmap[starting_point[0]][starting_point[1]]
  for point in neighbours:
    if point == None or point in points:
      continue
    point_value = heightmap[point[0]][point[1]]
    if point_value >= starting_point_value and point_value != 9:
      find_basin(heightmap, point, points)
  return points


def solver(part):
  input = open_file('input/day09.txt')
  input_array = []
  for line in input:
    input_array.append(map(int, list(line.strip())))
  if part == 1:
    risk_level = 0
    low_points = find_low_points(input_array)
    for low_point in low_points:
      risk_level += input_array[low_point[0]][low_point[1]]+1
    return risk_level
  elif part == 2:
    low_points = find_low_points(input_array)
    basins = []
    for low_point in low_points:
      basins.append(find_basin(input_array, low_point, []))
    basin_sizes = []
    for basin in basins:
      basin_sizes.append(len(basin))
    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

print('Part 1: ', solver(1))
print('Part 2: ', solver(2))

