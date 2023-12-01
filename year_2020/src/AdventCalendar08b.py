input_file = open('day2.txt')
content = input_file.readlines()
total_lines = len(content)

completed_lines = []
instruction_line = 0
acc = 0
jmpnop_lines = []
jmpnop_acc = []
jmpnop_lock = False

while True:
    if instruction_line == total_lines:
        break
    line = content[instruction_line]
    operation = line[:3]
    argument = int(line.split()[1])
    print(instruction_line, operation, argument)
    if instruction_line in completed_lines:
        jmpnop_lock = True
        print('backup!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        instruction_line = jmpnop_lines[-1]
        acc = jmpnop_acc[-1]
        jmpnop_lines = jmpnop_lines[:-1]
        jmpnop_acc = jmpnop_acc[:-1]
        print(jmpnop_lines[-5:])
        line = content[instruction_line]
        if line[:3] == 'jmp':
            operation = 'nop'
        elif line[:3] == 'nop':
            operation = 'jmp'
        argument = int(line.split()[1])
        completed_lines = completed_lines[:completed_lines.index(instruction_line)]

    if operation == 'acc':
        acc += argument
        next_line = instruction_line + 1
    elif operation == 'jmp':
        next_line = instruction_line + argument
    elif operation == 'nop':
        next_line = instruction_line + 1
    if (operation == 'jmp' or operation == 'nop') and not jmpnop_lock:
        jmpnop_lines.append(instruction_line)
        jmpnop_acc.append(acc)
    completed_lines.append(instruction_line)
    instruction_line = next_line

print(acc)
