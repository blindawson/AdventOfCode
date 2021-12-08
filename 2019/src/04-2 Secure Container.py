total_match = 0
for i in range(347312, 805915+1):
    i = str(i)
    match_adj = False
    digits_inc = True

    # pairs of adjacent digits
    c = 0
    if (i[c] == i[c + 1]) & (i[c] != i[c + 2]):
        match_adj = True
    for c in range(1, 4):
        if (i[c] == i[c + 1]) & (i[c] != i[c + 2]) & (i[c] != i[c - 1]):
            match_adj = True
    c = 4
    if (i[c] == i[c + 1]) & (i[c] != i[c - 1]):
        match_adj = True

    # increasing digits
    for c in range(len(i) - 1):
        if i[c] > i[c + 1]:
            digits_inc = False

    if match_adj & digits_inc:
        total_match += 1
print(total_match)

