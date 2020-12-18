input_file = open('day2.txt')
content = input_file.readlines()

# memsize = 0
# for line in content:
#     if line[:3] == 'mem':
#         x = int(line.replace('[', ']').split(']')[1])
#         memsize = max(memsize, x)

# mem = [['0' * 36]] * (memsize+1)
mem = []
loc = []
for n, line in enumerate(content):
    print(n, line)
    if line[:4] == 'mask':
        line.split()
        mask = line.split()[2]
    elif line[:3] == 'mem':
        memcmd = line.replace('[', ' ').replace(']', ' ').split(' ')
        idx = int(memcmd[1])
        idb = bin(idx)[2:].zfill(36)
        print(idb)
        val = int(memcmd[4])

        for i, x in enumerate(mask):
            if x == '1':
                idb = idb[:i] + x + idb[i+1:]
        idb = [idb]
        for i, x in enumerate(mask):
            if x == 'X':
                idb = idb * 2
                for v in range(int(len(idb)/2)):
                    idb[v] = idb[v][:i] + '0' + idb[v][i+1:]
                for v in range(int(len(idb)/2), len(idb)):
                    idb[v] = idb[v][:i] + '1' + idb[v][i+1:]
        print(idb)
        for i in idb:
            idx = int(i, 2)
            if idx in loc:
                mem[loc.index(idx)] = val
            else:
                mem.append(val)
                loc.append(idx)
    else:
        raise ValueError
# print(sum(mem))

print(mem)
print(loc)
total = 0
for i in mem:
    total += i
print(total)