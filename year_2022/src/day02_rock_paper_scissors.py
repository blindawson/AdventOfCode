input_file = open(r'year_2022/input/02_rock_paper_scissors.txt')
content = input_file.read().splitlines()

rps_score = {'A X': 1 + 3,
             'A Y': 2 + 6,
             'A Z': 3 + 0,
             'B X': 1 + 0,
             'B Y': 2 + 3,
             'B Z': 3 + 6,
             'C X': 1 + 6,
             'C Y': 2 + 0,
             'C Z': 3 + 3
             }
    
score = 0
for c in content:
    score += rps_score[c]
print(f'Total Score Part 1: {score}')

rps_score = {'A X': 3 + 0, # lose to rock, throw scissors
             'A Y': 1 + 3, # draw to rock, throw rock
             'A Z': 2 + 6, # win to rock, throw paper
             'B X': 1 + 0, # lose to paper, throw rock
             'B Y': 2 + 3, # draw to paper, throw paper
             'B Z': 3 + 6, # win to paper, throw scissors
             'C X': 2 + 0, # lose to scissors, throw paper
             'C Y': 3 + 3, # draw to scissors, throw scissors
             'C Z': 1 + 6 # win to scissors, throw rock
             }

score = 0
for c in content:
    score += rps_score[c]
print(f'Total Score Part 2: {score}')