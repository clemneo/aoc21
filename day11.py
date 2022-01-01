def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def get_graph(input):
  
  graph = {}
  for row in range(len(input)): # row is 0 to 9
    for col in range(len(input[0])-1): # col is 0 to 9
      graph[(row,col)] = {}
      graph[(row,col)]['energy'] = int(input[row][col])
      graph[(row,col)]['flashed'] = False
      graph[(row,col)]['neighbors'] = []
      if row != 0: graph[(row,col)]['neighbors'].append((row-1,col)) # left
      if row != len(input)-1: graph[(row,col)]['neighbors'].append((row+1,col)) # right
      if col != 0: graph[(row,col)]['neighbors'].append((row, col-1)) # up
      if col != len(input[0])-2: graph[(row,col)]['neighbors'].append((row, col+1)) # down
      if row != 0 and col != 0: graph[(row,col)]['neighbors'].append((row-1, col-1)) # top-left
      if row != 0 and col != len(input[0])-2: graph[(row,col)]['neighbors'].append((row-1, col+1)) # bottom-left
      if row != len(input)-1 and col != 0: graph[(row,col)]['neighbors'].append((row+1, col-1)) # top-right
      if row != len(input)-1 and col != len(input[0])-2: graph[(row,col)]['neighbors'].append((row+1, col+1)) # bottom-right
  return graph
      

def print_graph(graph):
  for row in range(100):
    try:
      test = graph[row,0]
      for col in range(100):
        try:
          print(graph[(row,col)]['energy'], end='')
        except KeyError:
          print()
          break
    except KeyError:
      return

def solver(part):
  input = open_file('input/day11.txt')
  graph = get_graph(input)
  # print(graph)
  if part == 1:
    steps = 100
    total_flashes = 0
    for i in range(steps):
      for octopus in graph:
        graph[octopus]['energy'] += 1
      done = False
      while not done:
        for octopus in graph:
          if graph[octopus]['energy'] > 9:
            graph[octopus]['energy'] = 0
            graph[octopus]['flashed'] = True
            total_flashes += 1
            for neighbor in graph[octopus]['neighbors']:
              if graph[neighbor]['flashed'] == False:
                graph[neighbor]['energy'] += 1
        for octopus in graph:
          done = True
          if graph[octopus]['energy'] > 9:
            done = False
            break

      # Reset 'flashed' status at the end of the step
      for octopus in graph:
        graph[octopus]['flashed'] = False

    print_graph(graph)
    return total_flashes
  elif part == 2:
    total_steps = 0
    while True:
      for octopus in graph:
        graph[octopus]['energy'] += 1
      done = False
      while not done:
        for octopus in graph:
          if graph[octopus]['energy'] > 9:
            graph[octopus]['energy'] = 0
            graph[octopus]['flashed'] = True
            for neighbor in graph[octopus]['neighbors']:
              if graph[neighbor]['flashed'] == False:
                graph[neighbor]['energy'] += 1
        for octopus in graph:
          done = True
          if graph[octopus]['energy'] > 9:
            done = False
            break
      total_steps += 1

      # check if all have flashed
      everything_flashed = True
      for octopus in graph:
        if graph[octopus]['flashed'] == False:
          everything_flashed = False
      if everything_flashed:
        return total_steps
      # Reset 'flashed' status at the end of the step
      for octopus in graph:
        graph[octopus]['flashed'] = False

    print_graph(graph)
              

  



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))