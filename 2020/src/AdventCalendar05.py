input_file = open('day2.txt')

content = input_file.read().split('\n')

seat_ids = []
for line in content:
    row = int(line[0:7].replace('B', '1').replace('F', '0'), 2)
    col = int(line[7:10].replace('R', '1').replace('L', '0'), 2)
    seat_id = row * 8 + col
    seat_ids.append(seat_id)

for s in range(min(seat_ids)+1, max(seat_ids)):
    if s not in seat_ids:
        print(s)