import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def hex_to_bin_str(hex_str):
  return format(int(hex_str, 16), '0' + str(len(hex_str)*4) + 'b')

def parse_packet(packet):
  """Takes in a binary string, and returns packet_info (dictionary) and remaining_string (string)"""
  # print('Packet: ', packet)
  packet_info = {}
  version = int(packet[0:3], 2)
  packet_info['version'] = version
  type_id = int(packet[3:6], 2)
  packet_info['typeID'] = type_id
  packet_info['subpackets'] = []
  if type_id == 4: # if packet is a literal
    literal_num = ''
    i=0
    while True:
      next_five_chars = packet[6+i:11+i]
      # print('nfc: ', next_five_chars)
      literal_num += next_five_chars[1:5]
      if next_five_chars[0] == '0': break
      i += 5
    packet_info['value'] = int(literal_num, 2)
    return packet_info, packet[11+i:]
  else: # if packet is not literal
    length_type_id = int(packet[6])
    if length_type_id == 0:
      subpacket_length = int(packet[7:22], 2)
      # print("Running A")
      # Need to separately define a 'remaining subpacket' so that this still returns the string after the subpacket portion
      remaining_string = packet[22+subpacket_length:]
      subpacket, remaining_subpacket = parse_packet(packet[22:22+subpacket_length])
      packet_info['subpackets'].append(subpacket)
      while len(remaining_subpacket) != 0:
        # print('rs: ', remaining_subpacket)      
        if int(remaining_subpacket) == 0: break
        # print("Running B")
        subpacket, remaining_subpacket = parse_packet(remaining_subpacket)
        packet_info['subpackets'].append(subpacket)
      return packet_info, remaining_string
    elif length_type_id == 1:
      num_of_subpackets = int(packet[7:18], 2)
      # print('no of sp:', num_of_subpackets)
      # print('rs: ', packet)
      remaining_string = packet[18:]
      for i in range(num_of_subpackets):
        # print("Running C")
        subpacket, remaining_string = parse_packet(remaining_string)
        packet_info['subpackets'].append(subpacket)
      return packet_info, remaining_string


def get_version_sum(packet_info):
  current_sum = packet_info['version']
  for subpacket in packet_info['subpackets']:
    current_sum += get_version_sum(subpacket)
  return current_sum
  
def calculate_transmission(packet_info):
  if packet_info['typeID'] == 4: 
    return packet_info['value']
  elif packet_info['typeID'] == 0:
    sum = 0
    for subpacket in packet_info['subpackets']:
      sum += calculate_transmission(subpacket)
    return sum
  elif packet_info['typeID'] == 1:
    total = 1
    for subpacket in packet_info['subpackets']:
      total *= calculate_transmission(subpacket)
    return total
  elif packet_info['typeID'] == 2:
    min = float('inf')
    for subpacket in packet_info['subpackets']:
      if min > calculate_transmission(subpacket):
        min = calculate_transmission(subpacket)
    return min
  elif packet_info['typeID'] == 3:
    max = 0
    for subpacket in packet_info['subpackets']:
      if max < calculate_transmission(subpacket):
        max = calculate_transmission(subpacket)
    return max
  elif packet_info['typeID'] == 5:
    subpackets = []
    for subpacket in packet_info['subpackets']:
      subpackets.append(subpacket)
    if calculate_transmission(subpackets[0]) > calculate_transmission(subpackets[1]):
      return 1
    else:
      return 0
  elif packet_info['typeID'] == 6:
    subpackets = []
    for subpacket in packet_info['subpackets']:
      subpackets.append(subpacket)
    if calculate_transmission(subpackets[0]) < calculate_transmission(subpackets[1]):
      return 1
    else:
      return 0
  elif packet_info['typeID'] == 7:
    subpackets = []
    for subpacket in packet_info['subpackets']:
      subpackets.append(subpacket)
    if calculate_transmission(subpackets[0]) == calculate_transmission(subpackets[1]):
      return 1
    else:
      return 0



def solver(part):
  input_file = open_file('input/day16.txt')
  # print(input_file[])
  packet_info, remaining_string = parse_packet(hex_to_bin_str(input_file[0]))
  if part == 1:
    return get_version_sum(packet_info)
  elif part == 2:
    # pp.pprint(packet_info)
    return calculate_transmission(packet_info)

print("Part 1: ", solver(1))
print("Part 2: ", solver(2))

