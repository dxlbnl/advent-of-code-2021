import math

type_map = {
  0: sum,
  1: math.prod,
  2: min,
  3: max,
  5: lambda l: l[0] > l[1],
  6: lambda l: l[0] < l[1],
  7: lambda l: l[0] == l[1],
}


def get(string, amount):
  return string[:amount], string[amount:]

def read_packet(transmission):
  version, transmission = get(transmission, 3)
  type, transmission = get(transmission, 3)
  version = int(version, 2)

  print("Package", version, int(type, 2))
  if int(type, 2) != 4:
    length_type_id, transmission = get(transmission, 1)
    subdata = []

    operator = type_map[int(type, 2)]
    print(f"Operator {operator}")


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
        subdata.append(data)
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
        subdata.append(data)

    return version, operator(subdata), transmission
    
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
    
transmission = 'E0529D18025800ABCA6996534CB22E4C00FB48E233BAEC947A8AA010CE1249DB51A02CC7DB67EF33D4002AE6ACDC40101CF0449AE4D9E4C071802D400F84BD21CAF3C8F2C35295EF3E0A600848F77893360066C200F476841040401C88908A19B001FD35CCF0B40012992AC81E3B980553659366736653A931018027C87332011E2771FFC3CEEC0630A80126007B0152E2005280186004101060C03C0200DA66006B8018200538012C01F3300660401433801A6007380132DD993100A4DC01AB0803B1FE2343500042E24C338B33F5852C3E002749803B0422EC782004221A41A8CE600EC2F8F11FD0037196CF19A67AA926892D2C643675A0C013C00CC0401F82F1BA168803510E3942E969C389C40193CFD27C32E005F271CE4B95906C151003A7BD229300362D1802727056C00556769101921F200AC74015960E97EC3F2D03C2430046C0119A3E9A3F95FD3AFE40132CEC52F4017995D9993A90060729EFCA52D3168021223F2236600ECC874E10CC1F9802F3A71C00964EC46E6580402291FE59E0FCF2B4EC31C9C7A6860094B2C4D2E880592F1AD7782992D204A82C954EA5A52E8030064D02A6C1E4EA852FE83D49CB4AE4020CD80272D3B4AA552D3B4AA5B356F77BF1630056C0119FF16C5192901CEDFB77A200E9E65EAC01693C0BCA76FEBE73487CC64DEC804659274A00CDC401F8B51CE3F8803B05217C2E40041A72E2516A663F119AC72250A00F44A98893C453005E57415A00BCD5F1DD66F3448D2600AC66F005246500C9194039C01986B317CDB10890C94BF68E6DF950C0802B09496E8A3600BCB15CA44425279539B089EB7774DDA33642012DA6B1E15B005C0010C8C917A2B880391160944D30074401D845172180803D1AA3045F00042630C5B866200CC2A9A5091C43BBD964D7F5D8914B46F040' #input("transmission: ")
# transmission = input("transmission: ")
transmission = f'{bin(int(transmission, 16))[2:]:0>{len(transmission)*4}}'

print(f'Read: {read_packet(transmission)}')