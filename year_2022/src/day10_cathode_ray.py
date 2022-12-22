from support import support
import pandas as pd
import numpy as np

# List of input commands
instructions = support.read_input(r"year_2022/input/10_cathode_ray.txt", flavor="split")

# Convert to dataframe
df = pd.DataFrame(instructions, columns=["instruction", "value"])
# Set None values to 0 and change values to ints
df.loc[pd.isnull(df["value"]), "value"] = 0
df["value"] = df["value"].astype("int")
# Value starts at 1
df.loc[0, "value"] += 1
# Set cumulative values
df["cycle"] = 1
df.loc[df["instruction"] == "addx", "cycle"] = 2
df.loc[0, "cycle"] += 1
df["start cycle"] = df["cycle"].cumsum() - df["cycle"]
df["end cycle"] = df["cycle"].cumsum()
df["start x"] = df["value"].cumsum() - df["value"]
df["end x"] = df["value"].cumsum()
# Signal Strength
def find_cycle(c):
    return df.loc[df["start cycle"] <= c].iloc[-1]

signal_strength = 0
for c in [20, 60, 100, 140, 180, 220]:
    x = find_cycle(c)["start x"]
    signal_strength += x * c
    # print([x, c])
print(f"Part 1 Answer: {signal_strength}")

df["sprite"] = df["start x"] + 1
crt = [1] * 240
for r in range(6):
    for c in range(1, 41):
        # print(r * 40 + c)
        row = find_cycle(r * 40 + c)
        if abs(row["sprite"] - c) <= 1:
            crt[r * 40 + c - 1] = 8
print(np.reshape(crt, (-1, 40)))
