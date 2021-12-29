from year_2021.src import day14_extended_polymerization as ep
from support import support


start_polymer = 'NNCB'
pair_insertions = support.read_input('year_2021/tests/test_inputs/14_test_input.txt', 
                                     flavor='split', split_char=' -> ')
dict_polymer = ep.chain_to_dict(start_polymer)
dict_polymer = ep.expand_chain(dict_polymer, pair_insertions, 10)
dict_elements = ep.dict_to_elements(dict_polymer)
max_element, min_element = ep.find_extreme_elements(dict_elements)
print(max_element, min_element)