import re

ifn = r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input19a.txt'
start_line = 132
# ifn = r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input19example2.txt'
# start_line = 0

input_file = open(ifn, 'r')
content = input_file.read()


def follow_rule_path(rule_num, letter=''):
    pattern = re.compile(rf'\n{str(rule_num)}:(.+)\n')
    path = pattern.findall(content)[0]
    or_groups = [x for x in path.split('|')]
    new_rule_nums = []
    if len(or_groups) > 1:
        for or_group in or_groups:
            new_rule_nums.append([int(x) for x in list(filter(None, or_group.split(' ')))])
    else:
        try:
            new_rule_nums = [int(x) for x in list(filter(None, path.split(' ')))]
        except ValueError:
            letter += path[2]
    return new_rule_nums, letter


def loop2(rule_num, letter=''):
    dirs, letter = follow_rule_path(rule_num, letter)
    if dirs:
        if isinstance(dirs[0], list):
            letter1 = ''
            letter2 = ''
            for x in dirs[0]:
                letter1 = loop2(x, letter1)
            for x in dirs[1]:
                letter2 = loop2(x, letter2)
            letter = letter + '(?:' + letter1 + '|' + letter2 + ')'
        else:
            for x in dirs:
                letter = loop2(x, letter)
    return letter


loop42 = loop2(42)
loop31 = loop2(31)


def answers(x):
    a = '^(?:' + loop42 + '){' + str(x+1) + ',}(?:' + loop31 + '){' + str(x) + '}\n'
    return re.compile(a)


# answers = '^' + loop2(0) + '\n' # Part 1
# apattern = re.compile(answers) # Part 1
input_file = open(ifn, 'r')
content1 = input_file.readlines()
correct_answers = 0
for x in content1[start_line:]:
    for y in range(1, 20):
        match = answers(y).findall(x)
        # match = apattern.findall(x) # Part 1
        if match:
            correct_answers += 1
            break
print(correct_answers)
