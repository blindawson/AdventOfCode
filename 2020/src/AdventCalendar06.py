input_file = open('day2.txt')
content = input_file.read().split('\n\n')

total = 0
for group in content:
    people = group.count('\n') + 1
    group = group.replace('\n', '')

    unique_answers = set(group)
    for u in unique_answers:
        if group.count(u) == people:
            total += 1

print(total)

