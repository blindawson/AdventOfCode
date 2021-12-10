input_file = open(r'../input/08_seven_segment_search.txt')
inputs = [x.split(' | ') for x in input_file.read().splitlines()]

unique_char_counts = [2, 3, 4, 7]

unique_count_codes = 0
for line in inputs:
    output_values = line[1].split()
    for output_value in output_values:
        if len(output_value) in unique_char_counts:
            unique_count_codes += 1

print(f'Part 1 answer: {unique_count_codes}')


def in_all_length_6_codes(length_6_codes, letter):
    return ((letter in length_6_codes[0]) and
            (letter in length_6_codes[1]) and
            (letter in length_6_codes[2]))


sum_outputs = 0
for line in inputs:
    input_values = line[0].split()
    output_values = line[1].split()
    code_dict = {}
    position_dict = {}
    length_5_codes = []
    length_6_codes = []
    letters = 'abcdefg'

    # assign codes with unique lengths to numbers
    for i in input_values:
        if len(i) == 2:
            code_dict[1] = i
        if len(i) == 3:
            code_dict[7] = i
        if len(i) == 4:
            code_dict[4] = i
        if len(i) == 5:
            length_5_codes.append(i)
        if len(i) == 6:
            length_6_codes.append(i)
        if len(i) == 7:
            code_dict[8] = i

    # use logic to assign letters to positions
    for c in code_dict[7]:
        if c not in code_dict[1]:
            position_dict['top'] = c
            letters = letters.replace(c, '')
    for c in code_dict[1]:
        if in_all_length_6_codes(length_6_codes, c):
            position_dict['bottom_right'] = c
            letters = letters.replace(c, '')
        else:
            position_dict['top_right'] = c
            letters = letters.replace(c, '')
    for c in code_dict[4]:
        if c not in code_dict[1]:
            if in_all_length_6_codes(length_6_codes, c):
                position_dict['top_left'] = c
                letters = letters.replace(c, '')
            else:
                position_dict['mid'] = c
                letters = letters.replace(c, '')
    for c in letters:
        if in_all_length_6_codes(length_6_codes, c):
            position_dict['bottom'] = c
        else:
            position_dict['bottom_left'] = c

    # use letters to solve for remaining numbers
    letter_combos = {0: ['top', 'top_left', 'top_right', 'bottom_right', 'bottom_left', 'bottom'],
                     2: ['top', 'top_right', 'mid', 'bottom_left', 'bottom'],
                     3: ['top', 'top_right', 'mid', 'bottom_right', 'bottom'],
                     5: ['top', 'top_left', 'mid', 'bottom_right', 'bottom'],
                     6: ['top', 'top_left', 'mid', 'bottom_right', 'bottom_left', 'bottom'],
                     9: ['top', 'top_left', 'top_right', 'mid', 'bottom_right', 'bottom']}
    for i in input_values:
        if (i in length_6_codes) and all(position_dict[x] in i for x in letter_combos[0]):
            code_dict[0] = i
        elif (i in length_5_codes) and all(position_dict[x] in i for x in letter_combos[2]):
            code_dict[2] = i
        elif (i in length_5_codes) and all(position_dict[x] in i for x in letter_combos[3]):
            code_dict[3] = i
        elif (i in length_5_codes) and all(position_dict[x] in i for x in letter_combos[5]):
            code_dict[5] = i
        elif (i in length_6_codes) and all(position_dict[x] in i for x in letter_combos[6]):
            code_dict[6] = i
        elif (i in length_6_codes) and all(position_dict[x] in i for x in letter_combos[9]):
            code_dict[9] = i

    # flip keys and values in dictionary and sort code alphabetically
    def sort_and_order_characters(string):
        return ''.join(sorted(string))
    code_dict = dict((sort_and_order_characters(v), k) for k, v in code_dict.items())

    output = ''
    for i in output_values:
        output += str(code_dict[sort_and_order_characters(i)])
    sum_outputs += int(output)

print(f'Part 2 answer: {sum_outputs}')
