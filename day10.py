def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

def check_corrupted(brackets):
  stack = []
  bracket_def = {')':'(', ']':'[', '>':'<', '}':'{'}
  for bracket in brackets:
    if bracket in bracket_def.values():
      stack.append(bracket)
    else:
      if stack[-1] != bracket_def[bracket]:
        return bracket
      else:
        stack.pop()
  return ''

def get_score(string_array):
  score = 0
  scorecard = {')':1, ']':2,'}':3,'>':4}
  for item in string_array:
    score *= 5
    score += scorecard[item]
  return score

def autocomplete(brackets):
  stack = []
  bracket_def = {')':'(', ']':'[', '>':'<', '}':'{'}
  closing_bracket = {'(':')','[':']','<':'>','{':'}'}
  for bracket in brackets:
    if bracket in bracket_def.values():
      stack.append(bracket)
    else:
      if stack[-1] == bracket_def[bracket]:
        stack.pop()
  completion_string = []
  for char in stack:
    completion_string.insert(0, closing_bracket[char])
  return completion_string

def solver(part):
  input = open_file('input/day10.txt')
  input_array = []
  score = {'':0, ')':3, ']':57, '}':1197, '>':25137}
  for line in input:
    input_array.append(list(line.strip()))

  if part==1:
    total_score = 0
    corrupted_brackets = []
    for item in input_array:
      corrupted_brackets.append(check_corrupted(item))
    for bracket in corrupted_brackets:
      total_score += score[bracket]
    return total_score

  elif part==2:
    incomplete_lines = []
    completion_strings = []
    total_score = []
    for item in input_array:
      if check_corrupted(item)=='':
        incomplete_lines.append(item)
    for line in incomplete_lines:
      completion_strings.append(autocomplete(line))
    for string in completion_strings:
      total_score.append(get_score(string))
    total_score.sort()
    return total_score[len(total_score)/2]

print "Part 1: ", solver(1)
print "Part 2: ", solver(2)