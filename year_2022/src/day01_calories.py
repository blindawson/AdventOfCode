input_file = open(r'year_2022/input/01_calories.txt')
content = input_file.read().splitlines()
# content = [int(c) for c in content]
sum_cal = 0
cal_list = []
for c in content:
    if c == '':
        cal_list.append(sum_cal)
        sum_cal = 0
    else:
        sum_cal += int(c)
cal_list.sort(reverse=True)
print(cal_list[0])
print(sum(cal_list[:3]))