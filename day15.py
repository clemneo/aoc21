import pprint
pp = pprint.PrettyPrinter()
import heapq as hq

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

class Graph:
  def __init__(self):
    self.v = 0
    self.graph = {}

  def add_vertice(self, vertice):
    self.graph[vertice] = []
    self.v += 1

  def add_edge(self, source, dest, cost):
    self.graph[source].append({'dest': dest, 'cost': cost})

def generate_graph(input_array):
  graph = Graph()
  for row_no in range(len(input_array)):
    for col_no in range(len(input_array[0])):
      graph.add_vertice((row_no, col_no))
  for row_no in range(len(input_array)):
    for col_no in range(len(input_array[0])):
      if row_no != 0: # adding top
        graph.add_edge((row_no, col_no), (row_no-1, col_no), input_array[row_no-1][col_no])
      if row_no != len(input_array)-1: # adding bottom
        try: 
          graph.add_edge((row_no, col_no), (row_no+1, col_no), input_array[row_no+1][col_no])
        except:
          print (col_no, row_no)
      if col_no != 0: # adding left
        graph.add_edge((row_no, col_no), (row_no, col_no-1), input_array[row_no][col_no-1])
      if col_no != len(input_array[0])-1: # adding right
        graph.add_edge((row_no, col_no), (row_no, col_no+1), input_array[row_no][col_no+1])
  return graph

# For learning purposes, the code below was my first attempt implementing Dijkstra without heapq

# def solver(part):
#   input_file = open_file('input/day15_test.txt')
#   input_array = []
#   for line in input_file:
#     input_array.append(list(map(int, list(line.strip()))))

#   if part == 1:
#     max_x = len(input_array[0])-1
#     max_y = len(input_array)-1
#     # graph.graph is adjacency list, where graph.graph[(x,y)] gives you [{'dest': (x2,y2), 'cost': 5}]    
#     graph = generate_graph(input_array)
#     # Initiating the visits dictionary 
#     visits = {}
#     for vertice in graph.graph:
#       visits[vertice] = {}
#       visits[vertice]['total_cost'] = float('inf')
#       # visits[vertice]['prev_v'] = None
#       visits[vertice]['done'] = False
#     visits[(0,0)]['total_cost'] = 0
#     visits[(0,0)]['done'] = True
#     current_node = (0,0)
#     while True:
#       # Dijkstra's algorithm here

#       for neighbor in graph.graph[current_node]:
#         if visits[current_node]['total_cost'] + neighbor['cost'] < visits[neighbor['dest']]['total_cost']:
#           visits[neighbor['dest']]['total_cost'] = visits[current_node]['total_cost'] + neighbor['cost']
#       visits[current_node]['done'] = True

#       # do check on whether to break or not here
#       current_least_cost = float('inf')
#       for vertice in visits:
#         if visits[vertice]['total_cost'] < current_least_cost and visits[vertice]['done'] == False:
#           current_least_cost = visits[vertice]['total_cost']
#       if (visits[(max_x,max_y)]['total_cost'] <= current_least_cost):
#         break

#       # If not, set next node to check

#       for vertice in visits:
#         if visits[vertice]['total_cost'] == current_least_cost and visits[vertice]['done'] == False:
#           current_node = vertice
#           break

#       if current_node[0]%10==0 and current_node[1]%10==0: print('Current Node: ', current_node, end='\r')
#     return visits[(max_x,max_y)]['total_cost']
#   elif part == 2:
#     # pp.pprint(input_array)
#     x_length = len(input_array[0])
#     for i in range(1,5): # expanding horizontally
#       for row in range(len(input_array)):
#         for col in range(x_length):
#           # print('current num', num)
#           new_num = input_array[row][col] + i
#           if new_num >= 10:
#             new_num -= 9
#           input_array[row].append(new_num)
#     # print(input_array)
#     print("@@@@@@")
#     y_length = len(input_array)
#     x_length = len(input_array[0])
#     for i in range(1,5): # expanding vertically
#       for row in range(y_length):
#         new_row = []
#         for col in range(x_length):
#           new_num = input_array[row][col] + i
#           if new_num >= 10:
#             new_num -= 9
#           new_row.append(new_num)
#         input_array.append(new_row)
#     # print(input_array)
#     # print("########")

#     max_x = len(input_array[0])-1
#     max_y = len(input_array)-1

#     # graph.graph is adjacency list, where graph.graph[(x,y)] gives you [{'dest': (x2,y2), 'cost': 5}]    
#     graph = generate_graph(input_array)
#     # Initiating the visits dictionary 
#     visits = {}
#     for vertice in graph.graph:
#       visits[vertice] = {}
#       visits[vertice]['total_cost'] = float('inf')
#       # visits[vertice]['prev_v'] = None
#       # visits[vertice]['done'] = False
#     visits[(0,0)]['total_cost'] = 0
#     visited = set()
#     visited.add((0,0))
#     # visits[(0,0)]['done'] = True
#     current_node = (0,0)

#     while True:
#       # Dijkstra's algorithm here

#       for neighbor in graph.graph[current_node]:
#         if visits[current_node]['total_cost'] + neighbor['cost'] < visits[neighbor['dest']]['total_cost']:
#           visits[neighbor['dest']]['total_cost'] = visits[current_node]['total_cost'] + neighbor['cost']
#       # visits[current_node]['done'] = True
#       visited.add((current_node))

#       # do check on whether to break or not here
#       # current_least_cost = float('inf')
#       heap = []
#       for vertice in visits:
#         if vertice not in visited:
#           hq.heappush(heap, (visits[vertice]['total_cost'], vertice))
#       current_least_cost = heap[0][0]
#       if (visits[(max_x,max_y)]['total_cost'] <= current_least_cost):
#         break

#       # If not, set next node to check
#       current_node = heap[0][1]
#       # for vertice in visits:
#       #   if visits[vertice]['total_cost'] == current_least_cost and visits[vertice]['done'] == False:
#       #     current_node = vertice
#       #     break
      
#       if current_node[0]%10==0 and current_node[1]%10==0: print('Current Node: ', current_node, end='\r')

#     return visits[(max_x,max_y)]['total_cost']


# Implementing Dijkstra WITH heapq
def solver(part):
  input_file = open_file('input/day15.txt')
  input_array = []
  for line in input_file:
    input_array.append(list(map(int, list(line.strip()))))

  if part == 1:
    max_x = len(input_array[0])-1
    max_y = len(input_array)-1
    # graph.graph is adjacency list, where graph.graph[(x,y)] gives you [{'dest': (x2,y2), 'cost': 5}]    
    graph = generate_graph(input_array)
    # Initiating the distances dictionary 
    distances = {}
    for vertex in graph.graph:
      distances[vertex] = float('inf')
    distances[(0,0)] = 0

    heap = [(0, (0,0))]
    while distances[(max_x,max_y)] > heap[0][0]:
      current_dist, current_vertex = hq.heappop(heap)

      if current_dist > distances[current_vertex]:
        continue


      # print(graph.graph)
      for dest_dict in graph.graph[current_vertex]:
        dest = dest_dict['dest']
        cost = dest_dict['cost']
        new_dist = current_dist + cost
        if new_dist < distances[dest]:
          distances[dest] = new_dist
          hq.heappush(heap, (new_dist, dest))
    return(distances[(max_x,max_y)])


  elif part == 2:
    # pp.pprint(input_array)
    x_length = len(input_array[0])
    for i in range(1,5): # expanding horizontally
      for row in range(len(input_array)):
        for col in range(x_length):
          # print('current num', num)
          new_num = input_array[row][col] + i
          if new_num >= 10:
            new_num -= 9
          input_array[row].append(new_num)
    # print(input_array)
    y_length = len(input_array)
    x_length = len(input_array[0])
    for i in range(1,5): # expanding vertically
      for row in range(y_length):
        new_row = []
        for col in range(x_length):
          new_num = input_array[row][col] + i
          if new_num >= 10:
            new_num -= 9
          new_row.append(new_num)
        input_array.append(new_row)
    # print(input_array)
    # print("########")

    max_x = len(input_array[0])-1
    max_y = len(input_array)-1
    graph = generate_graph(input_array)

    distances = {}
    for vertex in graph.graph:
      distances[vertex] = float('inf')
    distances[(0,0)] = 0

    heap = [(0, (0,0))]
    while distances[(max_x,max_y)] > heap[0][0]:
      current_dist, current_vertex = hq.heappop(heap)

      if current_dist > distances[current_vertex]:
        continue


      # print(graph.graph)
      for dest_dict in graph.graph[current_vertex]:
        dest = dest_dict['dest']
        cost = dest_dict['cost']
        new_dist = current_dist + cost
        if new_dist < distances[dest]:
          distances[dest] = new_dist
          hq.heappush(heap, (new_dist, dest))
    # print(distances)
    return distances[(max_x,max_y)]
  

print("Part 1: ", solver(1))
print("Part 2: ", solver(2))