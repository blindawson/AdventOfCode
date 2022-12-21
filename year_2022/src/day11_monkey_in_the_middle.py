import pandas as pd

cols = ["items", "test div", "if true monkey", "if false monkey"]
inputs = [
    [[74, 64, 74, 63, 53], 5, 1, 6],
    [[69, 99, 95, 62], 17, 2, 5],
    [[59, 81], 7, 4, 3],
    [[50, 67, 63, 57, 63, 83, 97], 13, 0, 7],
    [[61, 94, 85, 52, 81, 90, 94, 70], 19, 7, 3],
    [[69], 3, 4, 2],
    [[54, 55, 58], 11, 1, 5],
    [[79, 51, 83, 88, 93, 76], 2, 0, 6],
]
# inputs = [
#     [[79, 98], 23, 2, 3],
#     [[54, 65, 75, 74], 19, 2, 0],
#     [[79, 60, 97], 13, 1, 3],
#     [[74], 17, 0, 1],
# ]
df = pd.DataFrame(inputs, columns=cols)
df["inspections"] = 0
items = df["items"].values


def op(monkey, x):
    ops = [x * 7, x * x, x + 8, x + 4, x + 3, x + 5, x + 7, x * 3]
    # ops = [x * 19, x + 6, x * x, x + 3]
    return ops[monkey]


for _ in range(20):
    for index, row in df.iterrows():
        for i in items[index]:
            df.loc[index, "inspections"] += 1
            worry = op(index, i)
            worry = int(worry / 3)
            if worry % row["test div"] == 0:
                receiving_monkey = row["if true monkey"]
            else:
                receiving_monkey = row["if false monkey"]
            items[receiving_monkey] += [worry]
        items[index] = []
    # print(inputs)

df
