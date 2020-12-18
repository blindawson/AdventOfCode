import re

input_file = open('day2.txt')
content = input_file.readlines()

sub_bags_old_ct = [1]
sub_bags_old = ['shiny gold']
sub_bags_new_ct = []
sub_bags_new = []
total = 0

keep_going = True
while keep_going:
    keep_going = False
    print(sub_bags_old)
    for i, b in enumerate(sub_bags_old):
        for line in content:
            large_bag_pattern = re.compile(r'(.+?) bags contain')
            small_bag_pattern = re.compile(r'(\d+?|no) (.+?) bag(?:s)?(?:, |.)')

            large_bag = large_bag_pattern.search(line).group(1)
            small_bags = small_bag_pattern.findall(line)

            # print(large_bag)
            # print(small_bags)

            if large_bag == b:
                keep_going = True
                large_ct = sub_bags_old_ct[i]
                for small_bag in small_bags:
                    if small_bag[0] == 'no':
                        continue
                    count = int(small_bag[0]) * large_ct
                    total += count
                    bag_type = small_bag[1]
                    sub_bags_new.append(bag_type)
                    sub_bags_new_ct.append(count)

    sub_bags_old = sub_bags_new
    sub_bags_old_ct = sub_bags_new_ct
    sub_bags_new = []
    sub_bags_new_ct = []

print(total)
