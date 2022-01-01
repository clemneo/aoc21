def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines


def get_graph(input):
  graph = {}
  for line in input:
    line = str.strip(line)
    points = line.split("-")
    for point in points:
      if point not in graph:
        graph[point] = []
    if points[0] != 'end' and points[1] != 'start': graph[points[0]].append(points[1])
    if points[1] != 'end' and points[0] != 'start': graph[points[1]].append(points[0])
  return graph


def dfs_small_once(graph, current_path, all_paths):
  for next_cave in graph[current_path[-1]]:
    if next_cave.islower() and next_cave in current_path:
      continue
    current_path.append(next_cave)
    if current_path[-1] == 'end':
      completed_path = current_path.copy()
      all_paths.append(completed_path)
    else:
      dfs_small_once(graph, current_path, all_paths)
    current_path.pop()
    

def already_visited_small_twice(path):
  for cave in path:
    if cave == 'start' or cave == 'end':
      continue
    if cave.islower():
      if path.count(cave) == 2:
        return True


def dfs_small_twice(graph, current_path, all_paths):
  for next_cave in graph[current_path[-1]]:
    if next_cave.islower() and next_cave in current_path:
      if already_visited_small_twice(current_path) == True:
        continue
      else:
        pass
    current_path.append(next_cave)
    if current_path[-1] == 'end':
      completed_path = current_path.copy()
      all_paths.append(completed_path)
    else:
      dfs_small_twice(graph, current_path, all_paths)
    current_path.pop()


def solver(part):
  input = open_file('input/day12.txt')
  graph = get_graph(input)
  if part == 1:
    current_path = ['start']
    all_paths = []
    dfs_small_once(graph,current_path, all_paths)
    # print(all_paths)
    return len(all_paths)
  if part == 2:
    current_path = ['start']
    all_paths = []
    dfs_small_twice(graph,current_path, all_paths)
    # print(all_paths)
    return len(all_paths)

print("Part 1: ", solver(1))
print("Part 2: ", solver(2))