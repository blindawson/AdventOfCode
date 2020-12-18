import re

input_file = open('day2.txt')
# content = input_file.readlines()
content = input_file.read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
test = [r'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm',
        r'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929 hgt:73in']

valid = 0
for line in content:
    line = line + ' '
    try:
        byr_pattern = re.compile(r'byr:(\d\d\d\d)\s')
        byr = int(byr_pattern.search(line).group(1))
        if byr not in range(1920, 2002+1):
            continue

        iyr_pattern = re.compile(r'iyr:(\d\d\d\d)\s')
        iyr = int(iyr_pattern.search(line).group(1))
        if iyr not in range(2010, 2020 + 1):
            continue

        eyr_pattern = re.compile(r'eyr:(\d\d\d\d)\s')
        eyr = int(eyr_pattern.search(line).group(1))
        if eyr not in range(2020, 2030 + 1):
            continue

        pattern = re.compile(r'hgt:(\d+)(in|cm)\s')
        hgt = int(pattern.search(line).group(1))
        unit = pattern.search(line).group(2)
        if unit == 'in':
            if hgt not in range(59, 76+1):
                continue
        if unit == 'cm':
            if hgt not in range(150, 193+1):
                continue

        pattern = re.compile(r'hcl:#([0-9a-f]{6})\s')
        hcl = pattern.search(line).group(1)

        pattern = re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\s')
        ecl = pattern.search(line).group(1)

        pattern = re.compile(r'pid:(\d{9})\s')
        pid = pattern.search(line).group(1)

    except AttributeError:
        continue

    valid += 1

print(valid)
