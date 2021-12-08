input_file = open(r'..\input\02a intcode input.txt')
initial_content = input_file.read().split(',')
initial_content = [int(i) for i in initial_content]


def int_program(int_list, start_int):
    continue_program = True
    operation_code = int_list[start_int]
    input1 = int_list[int_list[start_int + 1]]
    input2 = int_list[int_list[start_int + 2]]
    out_loc = int_list[start_int + 3]
    if operation_code == 1:
        int_list[out_loc] = input1 + input2
    elif operation_code == 2:
        int_list[out_loc] = input1 * input2
    else:
        # raise ValueError('Number is wrong')
        continue_program = False

    return int_list, continue_program


def run_program(content, noun, verb):
    content[1] = noun
    content[2] = verb
    i = 0
    while content[i] != 99:
        # print(content)
        # print(content[i:i+4])
        content, continue_program = int_program(content, i)
        i += 4
        if not continue_program:
            content[i] = 99

    # print(content)
    return content[0]


print(run_program(initial_content.copy(), 12, 2))
for n in range(100):
    for v in range(100):
        result = run_program(initial_content.copy(), n, v)
        # print(result)
        if result == 19690720:
            print(100 * n + v)
            exit()
        # else:
            # print(f'Tried {n}, {v}. Got {result}')
