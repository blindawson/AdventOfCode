import re

input_file = open(r'C:\Users\brlw\Desktop\Repositories\AdventOfCode\2020\input\input16.txt')
content = input_file.readlines()

rule_pattern = re.compile(r' (\d+-\d+)(?: |\n)')

valid_nums = []
for line in content:
    rules = rule_pattern.findall(line)
    for rule in rules:
        start, end = [int(x) for x in rule.split('-')]
        [valid_nums.append(x) for x in range(start, end+1)]

print(valid_nums)