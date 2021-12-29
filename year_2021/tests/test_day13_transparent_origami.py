from year_2021.src import day13_transparent_origami as tt
from support import support

point_file = support.read_input(r'year_2021/tests/test_inputs/13_test_input.txt', 
                                flavor='split_int', split_char=',')

def test_count_points():
    folded = tt.fold_page('y', 7, point_file)
    assert tt.count_points(folded) == 17
    folded = tt.fold_page('x', 5, folded)
    assert tt.count_points(folded) == 16
