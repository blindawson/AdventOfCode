from AdventOfCode.support import support
from itertools import product


class Springs:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.sum = 0
        for row_input, group_input in self.file_input:
            self.sum += self.count_correct_combos(row_input, group_input)
        
    # Split the input string into groups of # and ?
    def grouped_row(self, row: str):
        return [x for x in row.split(".") if x]
        
    # Turn group_input from str into list of ints
    def preprocess_group_input(self, group: str):
        return [int(x) for x in group.split(',')]

    # Make a list of all possible combinations for a given row
    def row_combos(self, row: str):
        q_count = row.count("?")
        dot_hash_combinations = list(product([".", "#"], repeat=q_count))
        row_combinations = []
        
        for dot_hash in dot_hash_combinations:
            row_combination = row
            for i in dot_hash:
                row_combination = row_combination.replace("?", i, 1)
            row_combinations.append(row_combination)
        return row_combinations
        
    # List the size of each group in a row
    def row_count(self, row: str):
        return [len(x) for x in self.grouped_row(row)]
        
    # Count the number of correct combinations in a row
    def count_correct_combos(self, row: str, group_input: str):
        correct_combos = 0
        group_input = self.preprocess_group_input(group_input)
        for row_combo in self.row_combos(row):
            row_count = self.row_count(row_combo)
            if row_count == group_input:
                correct_combos += 1
        return correct_combos
            
        


filename = r"year_2023/tests/test_inputs/12_test_input.txt"
m = Springs(filename)
m.file_input
m.count_correct_combos(m.file_input[-1][0], m.file_input[-1][1])