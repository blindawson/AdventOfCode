for part in [1, 2]:
    input_file = open(r'year_2022/input/05_supply_stacks.txt')
    content = input_file.read().splitlines()

    stacks = ['DLJRVGF', 
            'TPMBVHJS', 
            'VHMFDGPC', 
            'MDPNGQ', 
            'JLHNF', 
            'NFVQDGTZ', 
            'FDBL',
            'MJBSVDN',
            'GLD']

    for i in content[10:]:
        # Pull quantities from instructions
        [q, s1, s2] = [int(j) for j in i.split() if j.isdigit()]
        # Convert to 0-index
        s1 -= 1
        s2 -= 1
        # Add letters to new stack
        if part == 1:
            stacks[s2] += stacks[s1][q*-1:][::-1]
        else:
            stacks[s2] += stacks[s1][q*-1:]
        # Remove letters from old stack
        stacks[s1] = stacks[s1][:q*-1]

    # Top of each stack
    tops = ''
    for i in stacks:
        tops += i[-1]
    print(f'Part {part} Answer: {tops}')