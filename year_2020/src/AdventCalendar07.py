import re

input_file = open('day2.txt')
content = input_file.readlines()
# print(content)

sub_bags_old = ['shiny gold']
sub_bags_new = []
all_sub_bags = []
total = 0

keep_going = True
while keep_going:
    keep_going = False
    for line in content:
        large_bag_pattern = re.compile(r'(.+?) bags contain')
        small_bag_pattern = re.compile(r'(\d+?|no) (.+?) bag(?:s)?(?:, |.)')

        large_bag = large_bag_pattern.search(line).group(1)
        small_bags = small_bag_pattern.findall(line)

        # print(large_bag)
        # print(small_bags)

        for small_bag in small_bags:
            count, bag_type = small_bag
            if bag_type in sub_bags_old:
                keep_going = True
                total += 1
                sub_bags_new.append(large_bag)
                all_sub_bags.append(large_bag)

    sub_bags_old = sub_bags_new
    sub_bags_new = []

print(len(set(all_sub_bags)))
