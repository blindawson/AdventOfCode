import re

input_file = open(r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input16.txt', 'r')
content = input_file.readlines()

field_pattern = re.compile(r'(\D+):')
rule_pattern = re.compile(r' (\d+-\d+)(?: |\n)')

valid_nums = []
field_rules = []
for line in content[:20]:
    rules = rule_pattern.findall(line)
    field_name = field_pattern.findall(line)[0]
    field_nums = []
    for rule in rules:
        start, end = [int(x) for x in rule.split('-')]
        [valid_nums.append(x) for x in range(start, end+1)]
        [field_nums.append(x) for x in range(start, end+1)]
    field_rules.append([field_name, field_nums])

# print(field_rules[-1])
invalid_sum = 0
for line in content[25:]:
    ticket_nums = [int(x) for x in line.split(',')]
    invalid_nums = [x for x in ticket_nums if x not in valid_nums]
    invalid_sum += sum(invalid_nums)
    if len(invalid_nums):
        content.remove(line)

field_guesses = [[x] for x in range(len(field_rules))]
for field_rule in field_rules:
    for position in range(0, 20):
        field_match = True
        for line in content[25:]:
            field_num = int(line.split(',')[position])
            if field_num not in field_rule[1]:
                field_match = False
        if field_match:
            field_guesses[position].append(field_rule[0])

print(f'Sum of invalid values = {invalid_sum}')
[print(x) for x in field_guesses]
input_file.close()
