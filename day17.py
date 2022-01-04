# target area: x=85..145, y=-163..-108
left_bound = 85
right_bound = 145
top_bound = -108
bottom_bound = -163

def hits_target(x_velo, y_velo):
  x_coor, y_coor = 0, 0
  while y_coor > bottom_bound:
    # Update position
    x_coor += x_velo
    y_coor += y_velo
    
    if left_bound <= x_coor <= right_bound and bottom_bound <= y_coor <= top_bound:
      return True

    # Update velocity
    if x_velo > 0:
      x_velo -= 1
    elif x_velo < 0:
      x_velo += 1
    y_velo -= 1

    if x_coor > right_bound and x_velo == 0:
      return False

  return False

def get_highest_y(x_velo, y_velo):
  x_coor, y_coor = 0, 0
  highest_y = 0

  while y_coor > bottom_bound:
    # Update position
    x_coor += x_velo
    y_coor += y_velo
    if highest_y < y_coor: 
      highest_y = y_coor
    elif highest_y >= y_coor:
      return highest_y

    # Update velocity
    if x_velo > 0:
      x_velo -= 1
    elif x_velo < 0:
      x_velo += 1
    y_velo -= 1

def hits_target_x(x_velo):
  x_coor = 0
  time = 0
  while x_coor < right_bound:
    time += 1
    x_coor += x_velo

    if left_bound <= x_coor <= right_bound:
      return time
    # Update velocity
    if x_velo > 0:
      x_velo -= 1
    elif x_velo < 0:
      x_velo += 1
  return 0

def hits_target_y(y_velo):
  y_coor = 0
  time = 0
  while y_coor > bottom_bound:
    time += 1
    y_coor += y_velo

    if bottom_bound <= y_coor <= top_bound:
      return time
    # Update velocity
    y_velo -= 1

  return 0


def solver(part):
  if part == 1:
    highest_y = float('-inf')
    for x_velo in range(1, right_bound+1):
      # print('x_velo: ', x_velo)
      for y_velo in range(1,1000):
        if hits_target(x_velo, y_velo):
          this_highest_y = get_highest_y(x_velo, y_velo)
          if highest_y < this_highest_y:
            highest_y = this_highest_y
    return highest_y
  elif part == 2:  
    total_hits = 0
    highest_y = float('-inf')
    for x_velo in range(1, right_bound+1):
      # print('x_velo: ', x_velo)
      for y_velo in range(bottom_bound, 500):
        if hits_target(x_velo, y_velo):
          total_hits += 1
    return total_hits

print("Part 1: ", solver(1))
print("Part 2: ", solver(2))