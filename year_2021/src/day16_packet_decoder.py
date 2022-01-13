from support import support
import numpy as np


def read_packet_header(bin_input, position):
    version = support.bin_to_dec(bin_input[position:position+3])
    type_id = support.bin_to_dec(bin_input[position+3:position+6])
    position += 6
    return version, type_id, position
    
    
def read_5bit(bit5):
    prefix = bit5[0]
    suffix = bit5[1:5]
    return prefix, suffix


def simple_literal(bin_input, position):
    literal_bin = ''
    last_group = False
    while not last_group:
        bit5_prefix, bit5_suffix = read_5bit(bin_input[position:position+5])
        if bit5_prefix == '0':
            last_group = True
        literal_bin += bit5_suffix
        position += 5
    return [support.bin_to_dec(literal_bin)], position
    
    
def operate_on_packets(type_id, literal_values):
    if type_id == 0:
        return sum(literal_values)
    elif type_id == 1:
        return np.prod(literal_values)
    elif type_id == 2:
        return min(literal_values)
    elif type_id == 3:
        return max(literal_values)
    elif type_id == 5:
        if literal_values[0] > literal_values [1]:
            return 1
        else:
            return 0
    elif type_id == 6:
        if literal_values[0] < literal_values [1]:
            return 1
        else:
            return 0
    elif type_id == 7:
        if literal_values[0] == literal_values [1]:
            return 1
        else:
            return 0
            
            
def operator15(bin_input, position, type_id, versions, literal_vals):
    total_bit_length = support.bin_to_dec(bin_input[position:position+15])
    position += 15
    stop_position = position + total_bit_length
    while position < stop_position:
        versions, literal_vals, position = read_subpacket(bin_input, position,
                                                          versions, literal_vals)
    literal_val = operate_on_packets(type_id, literal_vals)
    return versions, [literal_val], position
    
    
def operator11(bin_input, position, type_id, versions, literal_vals):
    num_packets = support.bin_to_dec(bin_input[position:position+11])
    position += 11
    i = 0
    while i < num_packets:
        i += 1
        versions, literal_vals, position = read_subpacket(bin_input, position,
                                                          versions, literal_vals)
    literal_val = operate_on_packets(type_id, literal_vals)
    return versions, [literal_val], position
    
    
def read_subpacket(bin_input, position, versions, literal_vals):
    version, type_id, position = read_packet_header(bin_input, position)
    versions += [version]
    if type_id == 4:
        literal_val, position = simple_literal(bin_input, position)
    else:
        length_type_id = bin_input[position]
        position += 1
        if length_type_id == '0':
            versions, literal_val, position = operator15(bin_input, position, type_id,
                                                          versions, [])
        else:
            versions, literal_val, position = operator11(bin_input, position, type_id,
                                                          versions, [])
    literal_vals += literal_val
    return versions, literal_vals, position


def read_transmission(transmission, position=0):
    versions = []
    literal_vals = []
    while position < len(transmission) and '1' in transmission[position:]:
        versions, literal_vals, position = read_subpacket(transmission, position, 
                                                          versions, literal_vals)
    return versions, literal_vals
    
    
transmission_hex = open(r'year_2021/input/16_packet_decoder.txt').read()
transmission_bin = support.hex_to_bin(transmission_hex)
versions, literal_values = read_transmission(transmission_bin)
print(f'Part 1 Answer: {sum(versions)}')
print(f'Part 2 Answer: {literal_values}')
