from AdventOfCode.support import support


class MonkeyMath:
    def __init__(self, filename: str) -> None:
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.read_input()
        self.part1()

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
            
    # def part2(self) -> None:
    #     for _ in range(100):
            
            
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
            if isinstance(eqn_monkey1, int) and isinstance(
                eqn_monkey2, int
            ):
                # solve the equation
                self.ans[monkey] = functions_dict[eqn_fn](
                    eqn_monkey1, eqn_monkey2
                )
                # transfer item from eqns to answers
                moved_monkeys.append(monkey)
            else:
                # copy values into self.eqns
                self.eqns[monkey] = [eqn_monkey1, eqn_fn, eqn_monkey2]
        [self.eqns.pop(monkey) for monkey in moved_monkeys]


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

# filename = r"year_2022/tests/test_inputs/21_test_input.txt"
filename = r'year_2022/input/21_monkey_math.txt'
m = MonkeyMath(filename)
