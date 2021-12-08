lanternfish_file = open(r'../input/06_lanternfish.txt')
lanternfish_start = [int(x) for x in lanternfish_file.read().split(',')]


def multipy_lanternfish(lanternfish, days):
    for day in range(days):
        # print(day)
        for f, fish in enumerate(lanternfish):
            if fish == 0:
                lanternfish.append(9)
                lanternfish[f] = 6
            else:
                lanternfish[f] = fish - 1
        # print(lanternfish)
    return lanternfish


print(f'Part 1 answer: {len(multipy_lanternfish(lanternfish_start.copy(), 80))}')

fish_by_age = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
               5: 0, 6: 0, 7: 0, 8: 0}

for age in fish_by_age.keys():
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