input_file = open(r'C:\Users\brian\Documents\GitHub\AdventOfCode\2019\input\02a intcode input.txt')
content = input_file.read().split(',')
content = [int(i) for i in content]


def int_program(int_list, start_int):
    operation_code = int_list[start_int]
    input1 = int_list[int_list[start_int + 1]]
    input2 = int_list[int_list[start_int + 2]]
    out_loc = int_list[start_int + 3]
    if operation_code == 1:
        int_list[out_loc] = input1 + input2
    elif operation_code == 2:
        int_list[out_loc] = input1 * input2
    else:
        raise ValueError('Number is wrong')
    return int_list


i = 0
while content[i] != 99:
    print(content)
    content = int_program(content, i)
    i += 4

print(content)
