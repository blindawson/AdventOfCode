from AdventOfCode.support import support
from sympy import symbols, Eq, solve


class MonkeyMath:
    def __init__(self, filename: str, part2: bool = False) -> None:
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.read_input()
        if not part2:
            self.part1()
        else:
            self.part2()

    def __repr__(self) -> str:
        return str(self.file_input)

    def read_input(self) -> None:
        self.eqns = {}
        self.ans = {}
        for i in self.file_input:
            monkey = i[0][:-1]
            if len(i) == 2:
                self.ans[monkey] = int(i[1])
            else:
                self.eqns[monkey] = i[1:]

    def part1(self) -> None:
        loop_num = 0
        while "root" not in self.ans.keys():
            loop_num += 1
            self.process_eqns()
            print(loop_num)

    def part2(self) -> None:
        # self.root_eqn = self.eqns.pop("root")
        self.hmn_val = self.ans.pop("humn")
        self.eqns["root"][1] = "="
        for _ in range(50):
            self.process_eqns()

        # Find the eqn with "humn" in it. Get it's key (key0) and value (value0)
        key0, value0 = [
            (key, value) for key, value in self.eqns.items() if "humn" in value
        ][0]
        self.replace_values(key0, value0)

    def replace_values(self, key0, value0) -> None:
        # Find all key0 in eqn values and replace it with value0
        for key, value in self.eqns.items():
            if key0 in value:
                self.eqns[key] = [value0 if x == key0 else x for x in self.eqns[key]]
                # For all those locations where you put in value0, find all instances of that key and repeat
                self.replace_values(key, self.eqns[key])

    def process_eqns(self) -> None:
        moved_monkeys = []
        for monkey in self.eqns:
            eqn_monkey1 = self.eqns[monkey][0]
            eqn_monkey2 = self.eqns[monkey][2]
            eqn_fn = self.eqns[monkey][1]
            if eqn_monkey1 in self.ans.keys():
                eqn_monkey1 = self.ans[eqn_monkey1]
            if eqn_monkey2 in self.ans.keys():
                eqn_monkey2 = self.ans[eqn_monkey2]
            # if both parts of equations are ints
            if isinstance(eqn_monkey1, int) and isinstance(eqn_monkey2, int):
                # solve the equation
                self.ans[monkey] = functions_dict[eqn_fn](eqn_monkey1, eqn_monkey2)
                # transfer item from eqns to answers
                moved_monkeys.append(monkey)
            else:
                # copy values into self.eqns
                self.eqns[monkey] = [eqn_monkey1, eqn_fn, eqn_monkey2]
        [self.eqns.pop(monkey) for monkey in moved_monkeys]

    def solve_algebra(self) -> int:
        eqn = self.eqns["root"]
        if isinstance(eqn[0], int):
            int_part = eqn[0]
            eqn_part = eqn[2]
        else:
            int_part = eqn[2]
            eqn_part = eqn[0]
            opr_part = eqn_part[1]
            
            opr_opp = reverse_operation[opr_part]
            int_part = 
            
        # I need to start by defining the equality (eqn_side and ans_side)
        # then within eqn_side I break that into eqn_part, opr_part, and int_part
        # reverse operation
        # ans_side = int_part reverse operation ans_side
        # eqn_side = eqn_part
        # repeat until eqn_part is length 1
            
            


# Define the functions
def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> int:
    if b != 0:
        return int(a / b)
    else:
        return None


# Create a dictionary with keys and function values
functions_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}
reverse_operation = {"+": "-", "-": "+", "*": "/", "/": "*"}

filename = r"year_2022/tests/test_inputs/21_test_input.txt"
# filename = r"year_2022/input/21_monkey_math.txt"
m = MonkeyMath(filename, part2=True)
