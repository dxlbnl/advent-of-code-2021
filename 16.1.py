

def get(string, amount):
  return string[:amount], string[amount:]

def read_packet(transmission):
  version, transmission = get(transmission, 3)
  type, transmission = get(transmission, 3)
  version = int(version, 2)
  print("Package", version, int(type, 2))

  if int(type, 2) != 4:
    length_type_id, transmission = get(transmission, 1)
    if length_type_id == '1':
      # Amount of sub_packets
      packet_amount, transmission = get(transmission, 11)
      to_read = int(packet_amount, 2)
      print(f'Reading {to_read} subpackets')

      while to_read:
        print(f"> {to_read}")
        p_version, data, transmission = read_packet(transmission)
        version += p_version
        to_read -= 1
        print(f"< {to_read}: subpacket : {data}")
    else:
      # Amount of bits in packet
      bit_length, transmission = get(transmission, 15)
      sub_packets, transmission = get(transmission, int(bit_length, 2))
      print(f'Reading {int(bit_length, 2)} bits')

      while sub_packets:
        print(f"> {int(bit_length, 2)}")
        p_version, data, sub_packets = read_packet(sub_packets)
        version += p_version
        print(f"< {int(bit_length, 2)} subpacked: {data}")
  else:
    literal = ''
    done = False
    while not done:
      done, transmission = get(transmission, 1)
      done = not bool(int(done))

      bits, transmission = get(transmission, 4)
      literal += bits
    print("Literal", int(literal, 2))
    return version, int(literal, 2), transmission
    
  return version, None, transmission
    
# transmission = '38006F45291200' #input("transmission: ")
transmission = input("transmission: ")
transmission = f'{bin(int(transmission, 16))[2:]:0>{len(transmission)*4}}'

print(f'Read: {read_packet(transmission)}')