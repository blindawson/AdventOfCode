import pandas as pd

input_file = open(r'../input/03_binary_diagnostic.txt')
diagnostic_input = pd.DataFrame([list(x) for x in input_file.read().splitlines()])


def extract_column(table, column_number):
    return table.loc[:, column_number]


def flip_binary(x):
    return abs(x-1)


def most_common_bit(bit_column):
    try:
        if bit_column.value_counts().loc['1'] >= bit_column.value_counts().loc['0']:
            gamma_bit = '1'
            epsilon_bit = '0'
        elif bit_column.value_counts().loc['1'] < bit_column.value_counts().loc['0']:
            gamma_bit = '0'
            epsilon_bit = '1'
    except KeyError:
        gamma_bit = bit_column.value_counts().index[0]
        epsilon_bit = str(flip_binary(int(gamma_bit)))
    return gamma_bit, epsilon_bit


gamma = ''
epsilon = ''
for c in diagnostic_input.columns:
    [gamma_bit, epsilon_bit] = most_common_bit(extract_column(diagnostic_input, c))
    gamma += gamma_bit
    epsilon += epsilon_bit

print(f'Part 1 answer: {int(gamma, 2) * int(epsilon, 2)}')


o2_table = diagnostic_input.copy()
co2_table = diagnostic_input.copy()
for c in diagnostic_input.columns:
    [gamma_bit, epsilon_bit] = most_common_bit(extract_column(o2_table, c))
    o2_table = o2_table.loc[o2_table.loc[:, c] == gamma_bit, :]
    if o2_table.shape[0] == 1:
        break

for c in diagnostic_input.columns:
    [gamma_bit, epsilon_bit] = most_common_bit(extract_column(co2_table, c))
    co2_table = co2_table.loc[co2_table.loc[:, c] == epsilon_bit, :]
    if co2_table.shape[0] == 1:
        break

o2_rating = str(int(o2_table.sum(axis=1)))
co2_rating = str(int(co2_table.sum(axis=1)))

print(f'Part 2 answer: {int(o2_rating, 2) * int(co2_rating, 2)}')
