input_file = open('day2.txt')
content = input_file.readlines()

completed_lines = []
instruction_line = 0
acc = 0
while True:
    print(instruction_line, acc)
    if instruction_line in completed_lines:
        break
    line = content[instruction_line]
    operation = line[:3]
    argument = int(line.split()[1])
    if operation == 'acc':
        acc += argument
        next_line = instruction_line + 1
    elif operation == 'jmp':
        next_line = instruction_line + argument
    elif operation == 'nop':
        next_line = instruction_line + 1
    completed_lines.append(instruction_line)
    instruction_line = next_line

print(acc)
