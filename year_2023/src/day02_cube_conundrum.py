from AdventOfCode.support import support


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.sum = 0
        self.power = 0
        for input in self.file_input:
            input[-1] += " "
            self.read_game(input)

    def read_game(self, game):
        game_num = int(game[1][:-1])
        grouped_list = [game[i : i + 2] for i in range(2, len(game), 2)]
        colors = {"blue": 0, "red": 0, "green": 0}
        for g in grouped_list:
            color = g[1][:-1]
            num = int(g[0])
            colors[color] = max(colors[color], num)
        self.power += colors["blue"] * colors["red"] * colors["green"]

        possible = True
        colors_max = {"blue": 14, "red": 12, "green": 13}
        for color, color_max in colors_max.items():
            if colors[color] > color_max:
                possible = False
        if possible:
            self.sum += game_num
