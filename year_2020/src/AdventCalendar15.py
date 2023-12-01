elf = [9, 12, 1, 4, 17, 0, 18]
# elf = [3,1,2]

elfidx = {}
for i in range(len(elf)-1):
    elfidx[elf[i]] = i

# final_num = 2020
final_num = 30000000


# def findlast(li, st):
#     return next(i for i in reversed(range(len(li))) if li[i] == st)

lastnum = elf[-1]
for i in range(len(elf)-1, final_num-1):
    if i % 10000 == 0:
        print(i, len(elfidx))

    num = i - elfidx[lastnum] if lastnum in elfidx else 0
    elfidx[lastnum] = i
    lastnum = num
    # print(lastnum)

# print(elfidx)
print(lastnum)
