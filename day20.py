import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def get_neighbors_dark(image, coords):
  neighbor_string = ""
  try:
    neighbor_string += image[coords[0]-1][coords[1]-1]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]-1][coords[1]]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]-1][coords[1]+1]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]][coords[1]-1]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]][coords[1]]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]][coords[1]+1]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]+1][coords[1]-1]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]+1][coords[1]]
  except:
    neighbor_string += '.'
  try:
    neighbor_string += image[coords[0]+1][coords[1]+1]
  except:
    neighbor_string += '.'

  return neighbor_string

def get_neighbors_bright(image, coords):
  neighbor_string = ""
  try:
    neighbor_string += image[coords[0]-1][coords[1]-1]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]-1][coords[1]]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]-1][coords[1]+1]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]][coords[1]-1]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]][coords[1]]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]][coords[1]+1]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]+1][coords[1]-1]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]+1][coords[1]]
  except:
    neighbor_string += '#'
  try:
    neighbor_string += image[coords[0]+1][coords[1]+1]
  except:
    neighbor_string += '#'

  return neighbor_string

def enhance_image(image, enhancements, times):
  # padding the image
  # pp.pprint(image)

  for i in range(times):
    new_image = []
    for j in range(len(image)): # for every row
      new_line = ""
      for k in range(len(image[0])): # for every character
        if i%2==0:
          enhancement_string = get_neighbors_dark(image, (j,k))
        else:
          enhancement_string = get_neighbors_bright(image, (j,k))
        enhance_no = ""
        for char in enhancement_string:
          if char == ".":
            enhance_no += "0"
          else:
            enhance_no += "1"
        enhance_no = int(enhance_no, 2)
        new_line += enhancements[enhance_no]
        # print("nl" , new_line)
      new_image.append(new_line)
    image = new_image
  # pp.pprint(image)

  return image


def solver(part):
  input_file = open_file('input/day20.txt')
  enhancements = input_file[0]
  image = input_file[2:]

  if part == 1:
    times = 2
    for i in range(len(image)):
      image[i] = '.'*(times) + image[i] + '.'*(times)
    for j in range(times):
      image.insert(0,('.'*len(image[0])))
      image.append(('.'*len(image[0])))

    image = enhance_image(image, enhancements, times)
    lit_pixels = 0
    for line in image:
      for char in line:
        if char == "#":
          lit_pixels += 1
    return lit_pixels
  if part == 2:
    times = 50
    for i in range(len(image)):
      image[i] = '.'*(times) + image[i] + '.'*(times)
    for j in range(times):
      image.insert(0,('.'*len(image[0])))
      image.append(('.'*len(image[0])))

    image = enhance_image(image, enhancements, times)
    lit_pixels = 0
    for line in image:
      for char in line:
        if char == "#":
          lit_pixels += 1
    return lit_pixels



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))