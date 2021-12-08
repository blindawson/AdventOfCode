lanternfish_file = open(r'../input/06_lanternfish.txt')
lanternfish_start = [int(x) for x in lanternfish_file.read().split(',')]

fish_by_age = {}
for age in range(9):
    fish_by_age[age] = sum(1 for x in lanternfish_start if x == age)


def multiply_lanternfish_by_age(dict_fish, days):
    # print(days)
    if days > 0:
        dict_fish_new = {}
        for age in range(1, 9):
            dict_fish_new[age - 1] = dict_fish[age]
        dict_fish_new[8] = dict_fish[0]
        dict_fish_new[6] += dict_fish[0]
        return multiply_lanternfish_by_age(dict_fish_new, days-1)
    else:
        return dict_fish


print(f'Part 1 answer: {sum(multiply_lanternfish_by_age(fish_by_age.copy(), 80).values())}')
print(f'Part 2 answer: {sum(multiply_lanternfish_by_age(fish_by_age.copy(), 256).values())}')