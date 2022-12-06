input_file = open(r'year_2022/input/06_tuning_trouble.txt')
content = input_file.read()
      
for packet_length in [4, 14]:
    for i in range(packet_length, len(content)):
        if len(set(content[i-packet_length:i])) == packet_length:
            print(f'Answer: {i}')
            break
