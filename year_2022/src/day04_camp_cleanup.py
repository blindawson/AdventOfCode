import re

input_file = open(r'year_2022/input/04_camp_cleanup.txt')
content = input_file.read().splitlines()

def check_x_in_y(x, y):
    if int(x[0]) >= int(y[0]) and int(x[1]) <= int(y[1]):
        return True
    else:
        return False
        
contain_sum = 0
partial_contain_sum=0
for i in content:
    i = re.split(r'-|,', i)
    if check_x_in_y([i[0], i[1]], [i[2], i[3]]) or check_x_in_y([i[2], i[3]], [i[0], i[1]]):
        contain_sum += 1
    for j in range(int(i[0]), int(i[1])+1):
        if j in range(int(i[2]), int(i[3])+1):
            partial_contain_sum += 1
            break
    
print(f'Part 1 Answer: {contain_sum}')
print(f'Part 2 Answer: {partial_contain_sum}')
