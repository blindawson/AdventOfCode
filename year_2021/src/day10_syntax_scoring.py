from statistics import median

syntax_file = open(r'year_2021/input/10_syntax_scoring.txt')
syntax_original = syntax_file.read().splitlines()

character_scores = {')': 3,
                    ']': 57,
                    '}': 1197,
                    '>': 25137,
                    'incomplete': 0}


def clean_chunk(chunk):
    small_chunks = ['()', '[]', '{}', '<>']
    still_cleaning = True
    while still_cleaning:
        if any([x in chunk for x in small_chunks]):
            for x in small_chunks:
                chunk = chunk.replace(x, '')
            clean_chunk(chunk)
        else:
            still_cleaning = False
    return chunk


def incomplete_or_corrupt(chunk):
    for x in clean_chunk(chunk):
        if x in character_scores.keys():
            return x
    return 'incomplete'


def syntax_error_score(data):
    illegal_characters = []
    for x in data:
        illegal_characters.append(incomplete_or_corrupt(x))
    return sum([character_scores[x] for x in illegal_characters])


print(f'Part 1 answer: {syntax_error_score(syntax_original)}')

autocomplete_scores_dict = {')': 1,
                            ']': 2,
                            '}': 3,
                            '>': 4}


def autocomplete(chunk):
    dict_autocomplete = {'(': ')',
                         '{': '}',
                         '[': ']',
                         '<': '>'}
    chunk = clean_chunk(chunk)
    autocomplete_chunk = ''
    for x in chunk[::-1]:
        autocomplete_chunk += dict_autocomplete[x]
    return autocomplete_chunk


def autocomplete_score(autocomplete_chunk):
    score = 0
    for x in autocomplete_chunk:
        score = score * 5 + autocomplete_scores_dict[x]
    return score


def median_score(data):
    scores = []
    for x in data:
        if incomplete_or_corrupt(x) == 'incomplete':
            scores.append(autocomplete_score(autocomplete(x)))
    return median(scores)


print(f'Part 2 answer: {median_score(syntax_original)}')
