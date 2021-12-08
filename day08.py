import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def number_of_unique(entries):
  total_unique = 0
  for entry in entries:
    for output in entry['output']:
      if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
        total_unique += 1
  return total_unique

def find_output_value(entry):
  config = find_config(entry)
  final_num_string = ''
  output_array = entry['output']

  # Defining the Seven-Segment Display
  display = {}
  display['1'] = ['top-right', 'bottom-right']
  display['2'] = ['top', 'top-right', 'middle', 'bottom-left', 'bottom']
  display['3'] = ['top', 'top-right', 'middle', 'bottom-right', 'bottom']
  display['4'] = ['top-right', 'top-left', 'middle', 'bottom-right']
  display['5'] = ['top', 'top-left', 'middle', 'bottom-right', 'bottom']
  display['6'] = ['top', 'top-left', 'middle', 'bottom-left', 'bottom-right', 'bottom']
  display['7'] = ['top', 'top-right', 'bottom-right']
  display['8'] = ['top', 'top-right', 'top-left', 'middle', 'bottom-left', 'bottom-right', 'bottom']
  display['9'] = ['top', 'top-right', 'top-left', 'middle', 'bottom-right', 'bottom']
  display['0'] = ['top', 'top-right', 'top-left', 'bottom-left', 'bottom-right', 'bottom']

  for num in output_array:
    positions = []
    num_list = list(num)
    for letter in num_list:
      for key in config:
        if config[key] == letter:
          positions.append(key)
    for num in display:
      if sorted(display[num]) == sorted(positions):
        final_num_string += num

  return int(final_num_string)

def find_config(entry):
  config = {}

  # Finding top
  for num in entry['signal']:
    if len(num)==3: 
      seven = list(num)
    if len(num)==2:
      one = list(num)
    if len(num)==4:
      four = list(num)
  for letter in seven:
    if letter not in one:
      config['top'] = letter

  # Finding top-right
  all_letters = ['a','b','c','d','e','f','g']
  bltrm = [] # bottom-left or top-right or middle
  six_nine_zero = []
  for num in entry['signal']:
    if len(num) == 6:
      num_list = list(num)
      six_nine_zero.append(num_list)
      for letter in all_letters:
        if letter not in num_list:
          bltrm.append(letter)
  for letter in bltrm:
    if letter in one:
      config['top-right'] = letter
  
  # Finding bottom-right
  for letter in one:
    if letter != config['top-right']:
      config['bottom-right'] = letter

  # Finding number two
  for num in entry['signal']:
    if len(num) == 5:
      if config['bottom-right'] not in list(num):
        two = list(num)

  # Finding middle
  for letter in four:
    if letter in two and letter != config['top-right']:
      config['middle'] = letter
  
  # Finding top-left
  for letter in four:
    if letter != config['top-right'] and letter != config['bottom-right'] and letter != config['middle']:
      config['top-left'] = letter

  # Finding bottom through finding nine
  for num in six_nine_zero:
    if config['middle'] in num and config['top-right'] in num:
      nine = num
  for letter in nine:
    if letter not in config.values():
      config['bottom'] = letter
      break

  # Finally, finding bottom-left because it's the last one
  for letter in all_letters:
    if letter not in config.values():
      config['bottom-left'] = letter

  return config

def solver(part):
  input = open_file('input/day08.txt')
  input_array = []
  for line in input:
    entry = {}
    entry['signal'] = line.strip().split('|')[0].split()
    entry['output'] = line.strip().split('|')[1].split()
    input_array.append(entry)

  if part == 1:
    return number_of_unique(input_array)
  elif part == 2:
    total_output_value = 0
    for entry in input_array:
      total_output_value += find_output_value(entry)
    return total_output_value

print(solver(2))