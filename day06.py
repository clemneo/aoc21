def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  return lines

# I started out manually creating one integer for each fish,
# But the second part made me realise just how horribly
# inefficient this was
def reproduction(fish_array, days):
  computed_answers = {}
  total_fish = 0
  for k in range(len(fish_array)):
    if fish_array[k] in computed_answers:
      total_fish+=computed_answers[fish_array[k]]
    else:
      single_fish_array=[fish_array[k]]
      for i in range(days):
        print('Calculating Day ', i)
        new_fish_array = []
        for j in range(len(single_fish_array)):
          if single_fish_array[j]>0:
            single_fish_array[j] = single_fish_array[j]-1
          elif single_fish_array[j]==0:
            single_fish_array[j]=6
            new_fish_array.append(8)
        for new_fish in new_fish_array:
          single_fish_array.append(new_fish)
      computed_answers[fish_array[k]] = len(single_fish_array)
      total_fish+=computed_answers[fish_array[k]]
    print(computed_answers)
  return total_fish

# How I should have done it from the start
def reproduction_dict(fish_dict, days):
  for i in range(days):
      amount_to_reproduce = fish_dict[0]
      for j in range(0,8):
        fish_dict[j] = fish_dict[j+1]
      fish_dict[6] += amount_to_reproduce
      fish_dict[8] = amount_to_reproduce
  total = 0
  for key in fish_dict:
    total += fish_dict[key]
  return total


def solver(part):
  lines = open_file('input/day06.txt')
  fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
  fish_array = list(map(int, lines[0].split(',')))
  for fish in fish_array:
    fish_dict[fish] += 1
  if part == 1:
    return reproduction_dict(fish_dict, 80)
  elif part == 2:
    return reproduction_dict(fish_dict, 256)

print('Part 1: ', solver(1))
print('Part 2: ', solver(2))