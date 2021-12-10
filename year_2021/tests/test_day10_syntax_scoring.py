from year_2021.src import day10_syntax_scoring as ss

test_file = open(r'../input/10_test_input.txt')
test_data = test_file.read().splitlines()


def test_syntax_error_score():
    assert ss.syntax_error_score(test_data) == 26397


def test_clean_chunk():
    assert ss.clean_chunk('(<{[]}>)(') == '('
    assert ss.clean_chunk('[<>({}){}[([])<>]]') == ''


def test_incomplete_or_corrupt():
    assert ss.incomplete_or_corrupt('{()()()>') == '>'
    assert ss.incomplete_or_corrupt('(((()))}') == '}'
    assert ss.incomplete_or_corrupt('[({(<(())[]>[[{[]{<()<>>') == 'incomplete'


def test_autocomplete():
    assert ss.autocomplete('[({(<(())[]>[[{[]{<()<>>') == '}}]])})]'
    assert ss.autocomplete('{<[[]]>}<{[{[{[]{()[[[]') == ']]}}]}]}>'


def test_autocomplete_score():
    assert ss.autocomplete_score('])}>') == 294
    assert ss.autocomplete_score('}}>}>))))') == 1480781


def test_median_score():
    assert ss.median_score(test_data) == 288957
