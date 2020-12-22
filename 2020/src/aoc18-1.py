import re

input_file = open(r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input18.txt', 'r')
content = input_file.readlines()


def find_paren(expression, is_paren=False):
    paren_pattern = re.compile(r'\(.+\)')
    try:
        sub = paren_pattern.findall(expression)[0]
        oparen = 0
        cparen = 0
        for i, ch in enumerate(sub):
            if ch == '(':
                oparen += 1
            if ch == ')':
                cparen += 1
            if oparen == cparen:
                return find_paren(sub[1:i], is_paren=True)
    except IndexError:
        return expression, is_paren


def eval_small_exp(expression):
    small_pattern = re.compile(r'\d+ [+*] \d+')
    try:
        small_exp = small_pattern.findall(expression)[0]
    except IndexError:
        return expression
    evaluation = str(eval(small_exp))
    return eval_small_exp(expression.replace(small_exp, evaluation, 1))


def calc_sum(line, subtotal=0):
    while ('+' in line) or ('*' in line):
        subexp, is_paren = find_paren(line)
        if is_paren:
            line = line.replace('(' + subexp + ')', eval_small_exp(subexp), 1)
        else:
            line = line.replace(subexp, eval_small_exp(subexp), 1)
    line.replace('\n', '')
    subtotal += int(line)
    print(int(line))
    return subtotal


total = 0
for exp in content:
    print(exp)
    total = calc_sum(exp, total)

print(total)

