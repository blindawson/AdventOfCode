import numpy as np
from math import gcd

input_file = open('advent_input.txt')
content = input_file.readlines()

buses = content[1].split(',')

# timestamps = [i for i in range(len(buses))]

timestamps = []
for i, b in enumerate(buses):
    if b != 'x':
        timestamps.append(i)
buses = [int(b) for b in buses if b != 'x']

print(timestamps)
print(buses)


def findlcm(a):
    try:
        lcm = a[0]
        for i in a[1:]:
            lcm = lcm * i // gcd(lcm, i)
    except IndexError:
        lcm = a
    return lcm

b1 = 13
b2 = 41
b2adj = 41 - 3

t = 0

t += b1
(t + 3) % b2 == 0


t = 0
for i, b in enumerate(buses):
    lcm = findlcm(buses[:i+1])
    b2 = buses[i+1]
    b2adj = b2 - timestamps[i+1]
    match = False
    while not match:
        t += lcm
        match = (t + timestamps[i+1]) % b2 == 00
    print(t)








# we_got_em = False
# while not we_got_em:
#     t += 1
#     print(t)
#     t_add = 0
#     for b in buses:
#         if b != 'x':
#             b = int(b)
#             if (t + t_add) % b == 0:
#                 t_add += 1
#             else:
#                 break
#             if t_add == len(buses):
#                 we_got_em = True
# print(t)
