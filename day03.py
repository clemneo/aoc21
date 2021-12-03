def get_gamma_epsilon(lines):
  number_of_entries = len(lines)
  length_of_number = len(lines[0])-1 # removes the /n character
  one_array = []
  gamma = ''
  epsilon = ''
  for i in range(0, length_of_number):
    one_array.append(0)
  for i in range(0, number_of_entries):
    for j in range(0, length_of_number):
      if lines[i][j] == '1':
        one_array[j] += 1
  for num in one_array:
    if num>number_of_entries/2: # if more than half are 1s.
      gamma += '1'
      epsilon += '0'
    else:
      gamma += '0'
      epsilon += '1'
  return (gamma, epsilon)

def multiply_gamma_epsilon(gamma, epsilon):
  return int(gamma, 2)*int(epsilon, 2)

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def get_rating(lines, gas_type, index):
  # gas_type: 0 == oxygen, 1 == CO2
  number_of_entries = len(lines)
  # print(lines)
  if number_of_entries == 1:
    return lines[0]
  length_of_number = len(lines[0])-1
  ones_in_index = 0
  for i in range(0, number_of_entries):
    if lines[i][index] == '1':
      ones_in_index += 1

  newlines = []

  if gas_type == 0:
    if ones_in_index*2 >= number_of_entries: # if 1 is more common
      for i in range(0, number_of_entries):
        if lines[i][index] == '1':
          newlines.append(lines[i])
    else:
      for i in range(0, number_of_entries):
        if lines[i][index] == '0':
          newlines.append(lines[i])
    return get_rating(newlines, 0, index+1)

  elif gas_type == 1:
    if ones_in_index*2 < number_of_entries: # if 1 is less common
      for i in range(0, number_of_entries):
        if lines[i][index] == '1':
          newlines.append(lines[i])
    else:
      for i in range(0, number_of_entries):
        if lines[i][index] == '0':
          newlines.append(lines[i])
    return get_rating(newlines, 1, index+1)


lines = open_file('input/day03.txt')
# Part 1
gamma, epsilon = get_gamma_epsilon(lines)
answer1 = multiply_gamma_epsilon(gamma, epsilon)
print("Part 1: ", answer1)
#Part 2
oxygen = get_rating(lines, 0, 0)
carbon_dioxide = get_rating(lines, 1, 0)
answer2 = multiply_gamma_epsilon(oxygen, carbon_dioxide)
print('Part 2: ', answer2)