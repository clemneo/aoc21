def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def parse_input(input):
  polymer = input[0]
  rules = {}
  for i in range(2,len(input)):
    a, b = input[i].split(' -> ')
    rules[a] = b
  return (polymer, rules)

def classic_insertion(polymer, rules):
  new_polymer = ""
  for i in range(len(polymer)-1):
    new_polymer += polymer[i]
    new_polymer += rules[polymer[i:i+2]]
  new_polymer += polymer[-1]
  return new_polymer

def count_elements(polymer):
  count = {}
  for char in polymer:
    if char not in count:
      count[char] = 1
    else:
      count[char] += 1
  return count

def polymer_to_dict(polymer, dict):
  for i in range(len(polymer)-1):
    dict[polymer[i:i+2]] += 1
  return dict

def dict_insertion(poly_dict, translation_dict):
  output_dict = poly_dict.copy()
  for key in poly_dict:
    for new_pair in translation_dict[key]:
      output_dict[new_pair] += poly_dict[key]
    output_dict[key] -= poly_dict[key]
  return output_dict

def translate_dict(dict,rules):
  output_dict = {}
  for key in dict:
    output_dict[key] = []
    added_char = rules[key]
    output_dict[key].append(key[0]+added_char)
    output_dict[key].append(added_char+key[1])
  return output_dict

def polymer_dict_counter(input_dict, start_char, end_char):
  count = {}
  for key in input_dict:
    if key[0] not in count:
      count[key[0]] = input_dict[key]
    else:
      count[key[0]] += input_dict[key]
    if key[1] not in count:
      count[key[1]] = input_dict[key]
    else:
      count[key[1]] += input_dict[key]
  count[start_char] += 1
  count[end_char] += 1
  for element in count:
    count[element] = int(count[element]/2)
  return count
    
def get_max_minus_min(element_count):
  max_count = 0
  min_count = float('inf')
  for element in element_count:
    if element_count[element] < min_count:
      min_count = element_count[element]
    if element_count[element] > max_count:
      max_count = element_count[element]
  return max_count - min_count


def solver(part):
  input = open_file('input/day14.txt')
  polymer, rules = parse_input(input)
  if part == 1:
    steps = 10
    for i in range(steps):
      polymer = classic_insertion(polymer, rules)
    element_count = count_elements(polymer)

    return get_max_minus_min(element_count)

  elif part == 2:
    polymer_dict = {}
    for pair in rules:
      polymer_dict[pair] = 0
    translation_dict = translate_dict(polymer_dict, rules)
    polymer_dict = polymer_to_dict(polymer, polymer_dict)

    steps = 40
    for i in range(steps):
      polymer_dict = dict_insertion(polymer_dict,translation_dict)
    element_count = polymer_dict_counter(polymer_dict, polymer[0], polymer[-1])
    return get_max_minus_min(element_count)
    

print("Part 1: ", solver(1))
print("Part 2: ", solver(2))