match = 0
for i in range(347312, 805915+1):
    i = str(i)
    match_adj = False
    digits_inc = True
    for c in range(len(i) - 1):
        # matching adjacent digits
        if i[c] == i[c + 1]:
            match_adj = True
        # increasing digits
        if i[c] > i[c + 1]:
            digits_inc = False
    if match_adj & digits_inc:
        match += 1
print(match)

