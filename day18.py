import ast

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def reduce_sn_no(sn):

  processed_sn = ""
  num_left_brackets = 0
  for i in range(len(sn)):
    if sn[i] == '[':
      num_left_brackets += 1
    elif sn[i] == ']':
      num_left_brackets -= 1

    # Check if embedded 4 pairs (for explode)
    if num_left_brackets == 5:
      # print('Exploding: ' + sn)
      # input()
      # Get left string, numbers, and right_string

      left_string = sn[0:i]

      lxx = 1 if sn[i+2].isdigit() else 0
      left_num = int(sn[i+1:i+2+lxx])

      rxx = 1 if sn[i+4+lxx].isdigit() else 0
      right_num = int(sn[i+3+lxx:i+4+lxx+rxx])
      right_string = sn[i+5+lxx+rxx:]
      for j in range(1,i+1):
        if left_string[i-j].isdigit():
          if left_string[i-j-1].isdigit():
            processed_sn = left_string[0:i-j-1] + str(int(sn[i-j-1:i-j+1])+left_num) + left_string[i-j+1:] + '0'
          else:
            processed_sn = left_string[0:i-j] + str(int(sn[i-j])+left_num) + left_string[i-j+1:] + '0'
          break
      else:
        processed_sn = left_string + '0'
      for j in range(len(right_string)):
        if not right_string[j].isdigit():
          processed_sn += right_string[j]
        else:
          if right_string[j+1].isdigit():
            processed_sn += str(int(right_string[j:j+2])+right_num) + right_string[j+2:]
          else:
            processed_sn += str(int(right_string[j])+right_num) + right_string[j+1:]
          break

      # then run it through the function again!
      processed_sn = reduce_sn_no(processed_sn)

      return processed_sn

    # Add the current char, so that if it runs through the entire string without invoking a condition it just gives processed_sn untouched
    processed_sn += sn[i]

  processed_sn = ""
  for i in range(len(sn)):
    # Check if current num is a 2-digit number
    if sn[i].isdigit():
      if sn[i+1].isdigit():
        # print("Splitting:", sn)
        left_string = sn[0:i]
        right_string = sn[i+2:]

        original_num = int(sn[i:i+2])
        left_num = original_num//2
        right_num = original_num - left_num

        processed_sn = left_string + '[' + str(left_num) + ',' + str(right_num) + ']' + right_string
        processed_sn = reduce_sn_no(processed_sn)

        return(processed_sn)
    processed_sn += sn[i]

  return processed_sn

def add_sn_no(sn1, sn2):
  old_sn_string = '[' + sn1 + ',' + sn2 + ']'
  new_sn_string = reduce_sn_no(old_sn_string)
  return new_sn_string

def get_magnitude(ans_array):
  left_magnitude = ans_array[0]*3 if isinstance(ans_array[0], int) else get_magnitude(ans_array[0])*3
  right_magnitude = ans_array[1]*2 if isinstance(ans_array[1], int) else get_magnitude(ans_array[1])*2
  return left_magnitude+right_magnitude
    
  

def solver(part):
  input_file = open_file('input/day18.txt')
  if part == 1:
    while len(input_file) != 1:
      new_sn = add_sn_no(input_file[0], input_file[1])
      input_file.pop(0)
      input_file.pop(0)
      input_file.insert(0, new_sn)
      # print("Addition Done!")
    answer_array = ast.literal_eval(input_file[0])
    return get_magnitude(answer_array)
  elif part == 2:
    largest_magnitude = 0
    for i in range(len(input_file)):
      for j in range(i+1, len(input_file)):
        answer_array = ast.literal_eval(add_sn_no(input_file[i],input_file[j]))
        current_magnitude = get_magnitude(answer_array)
        if current_magnitude > largest_magnitude:
          largest_magnitude = current_magnitude
    return largest_magnitude


print("Part 1: ", solver(1))
print("Part 2: ", solver(2))
