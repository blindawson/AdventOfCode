from AdventOfCode.support import support
import pandas as pd


start_polymer = 'HBCHSNFFVOBNOFHFOBNO'
pair_insertions = support.read_input('year_2021/input/14_extended_polymerization.txt', 
                                     flavor='split', split_char=' -> ')


def add_to_dict(dict, pair, quantity):
    if pair not in dict.keys():
        dict[pair] = quantity
    else:
        dict[pair] += quantity
    return dict


def chain_to_dict(chain):
    dict_polymer_local = {}
    for i in range(len(chain)-1):
        pair = chain[i: i+2]
        dict_polymer_local = add_to_dict(dict_polymer_local, pair, 1)
    return dict_polymer_local
            
            
def expand_chain(dict_polymer_local, instructions, num_steps):
    for _ in range(num_steps):
        new_dict = dict_polymer_local.copy()
        for instruction in instructions:
            target, insertion = instruction
            if target in dict_polymer_local.keys(): 
                if dict_polymer_local[target] > 0:
                    new_dict[target] -= dict_polymer_local[target]
                    new_pair1 = target[0] + insertion
                    new_pair2 = insertion + target[1]
                    for new_pair in [new_pair1, new_pair2]:
                        new_dict = add_to_dict(new_dict, new_pair, dict_polymer_local[target])
        dict_polymer_local = new_dict.copy()
    return dict_polymer_local
            
            
def dict_to_elements(polymer_dict_local):
    element_dict_local = {}
    for item in polymer_dict_local.items():
        for element in item[0]:
            element_dict_local = add_to_dict(element_dict_local, element, item[1])
    return element_dict_local
    
            
def find_extreme_elements(element_dict_local):
    elements_df = pd.DataFrame(element_dict_local.items(), columns=['Elements', 'Quantity']).sort_values(by=['Quantity'])
    return elements_df.iloc[-1, 1]/2, elements_df.iloc[0, 1]/2
            
            
dict_polymer = chain_to_dict(start_polymer)
dict_polymer = expand_chain(dict_polymer, pair_insertions, 10)
dict_elements = dict_to_elements(dict_polymer)
max_element, min_element = find_extreme_elements(dict_elements)
print(f'Part 1 answer: {max_element-min_element}')

dict_polymer = chain_to_dict(start_polymer)
dict_polymer = expand_chain(dict_polymer, pair_insertions, 40)
dict_elements = dict_to_elements(dict_polymer)
max_element, min_element = find_extreme_elements(dict_elements)
print(f'Part 2 answer: {max_element - min_element}')