def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def least_fuel_linear(crabs):
  least_fuel = float('inf')
  for i in range(crabs[-1]+1): # inclusive of last spot
    total_fuel = 0
    for crab in crabs:
      total_fuel += abs(crab-i)
    if total_fuel < least_fuel:
      least_fuel = total_fuel
  return least_fuel

def least_fuel_ap(crabs):
  least_fuel = float('inf')
  for i in range(crabs[-1]+1): # inclusive of last spot
    total_fuel = 0
    for crab in crabs:
      total_fuel += abs(crab-i) * (abs(crab-i) + 1) / 2 # arithmetic progression sum
    if total_fuel < least_fuel:
      least_fuel = total_fuel
  return least_fuel

def solver(part):
  input = open_file('input/day07.txt')
  crab_array = sorted(list(map(int, input[0].split(','))))
  if part == 1:
    return least_fuel_linear(crab_array)
  elif part == 2:
    return least_fuel_ap(crab_array)

print('Part 1: ', solver(1))
print('Part 2: ', solver(2))