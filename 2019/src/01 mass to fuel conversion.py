from math import floor
import pandas as pd

input_file = '../input/01a module masses.txt'
df_mass = pd.read_csv(input_file, delim_whitespace=True, header=None)


def fuel(mass):
    return max(floor(mass / 3) - 2, 0)


initial_fuel = df_mass.apply(lambda m: fuel(m), axis=1)
added_fuel = initial_fuel.apply(lambda m: fuel(m))
total_fuel = initial_fuel + added_fuel
while added_fuel.sum() > 0:
    added_fuel = added_fuel.apply(lambda m: fuel(m))
    total_fuel = total_fuel + added_fuel
print(total_fuel.sum())
