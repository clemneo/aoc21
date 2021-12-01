def increases(file):
  total = 0
  with open (file, 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)-2):
      if int(lines[i+1])>int(lines[i]): # convert to integer, or else '1013' !> '998'
        total+=1
  return total

def slidingwindow(file):
  total = 0
  with open (file, 'r+') as f:
    lines = f.readlines()
    for i in range(0, len(lines)-3):
      sum1 = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
      sum2 = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
      if sum1 < sum2:
        total+=1
  return total

# print(increases('day01_1.txt'))
print(slidingwindow('day01_1.txt'))
