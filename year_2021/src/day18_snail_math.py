import ast
import re

def search_levels(n, level=0, recreate_string='', first_in_pair=True):
    if isinstance(n, str):
        n = ast.literal_eval(n)
    nested_pair = []
    if isinstance(n, list):
        if level >= 4:
            recreate_string += f'\\[{n[0]},{n[1]}]'
            return n, recreate_string
        else:
            recreate_string += '\\['
            level += 1
            first_in_pair = True
            for i in n:
                if not nested_pair:
                    [nested_pair, recreate_string] = search_levels(i, level, recreate_string, first_in_pair)
                first_in_pair = False
            if not nested_pair:
                recreate_string += ']'
    else:
        recreate_string += str(n)
        if first_in_pair:
            recreate_string += ','
    return nested_pair, recreate_string
    
# Debugging
a = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
print(search_levels(a))

def reduce(x, level=0):
    # Find the first nested 4 pair and the string that includes the numbers to the left and right of the pair
    [nested_pair, regex] = search_levels(a)
    string_with_pair = re.findall(regex + '.*?\d+', a)[0]
	# add to the number to the right of the pair
    num_right = re.findall('\d+$', string_with_pair)[0]
    other_num_right = re.findall('(.*)'+num_right, string_with_pair)[0]
    string_with_pair_r1 = re.sub(re.escape(string_with_pair), 
                                 other_num_right+str(int(num_right) + nested_pair[1]), 
                                 a)
	# add to the number to the left of the pair
    
	# change the pair to 0
	# return snail_math(new_pair)
	
# 	left = pair[0]
# 	right = pair[1]
# 	if isinstance(left, num) and isinstance(right, num) and level == 4:
		
# def explode(pair):
# 	# re search for any double digit number
# 	# replace that number with a half and half pair
# 	# return snail_math(new_pair)
	
# def add(pair, next_pair):
# 	if there's another pair on the list:
# 		return snail_math([pair, next_pair])

# def snail_math(pair):
# 	reduce()
# 	explode()
# 	add()
# 	return answer






# def snail_addition(left, right):
#     return [left, right]
    
# # def read_list(n, level=0):
# #     left = n[0]
# #     right = n[1]
# #     if isinstance(left, list):
# #         read_list(left, level=level+1)
# #     if isinstance(right, list):
# #         read_list(right, level=level+1)

# def read_list(n, level=0):
#     if isinstance(n, list):
#         if level >= 4:
            
    
#         level += 1
#         for i in n:
#             read_list(i, level)
    
    
# def explode(n):
#     # pair's left value added to the first number to the left of the pair
#     # Pair's right value added to the first number to the right of teh pair
#     # Replace the pair with 0
    
# def split(n):
#     # replace num with pair [half round down, half round up]
    
# def snail_reduce(n):
#     if nested4(n):
#         explode(n)
#     elif greater10(n):
#         split(n)
#     else:
#         reduce(n)
        
# open_bracket = "\["
# open_bracket_plus = bracket and then .*
# close_bracket = "\]"                   
# pair = f"{open_bracket}\d+,\d+{close_bracket}"
# nest4pair = f"{open_bracket}{{"
# # the goal is to have an re that can find a 4 nested number
# # then take 4 nested number and explode it

[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
pos		Value				Actual
10000	['11000','12000']	[3,[2,[1,[7,3]]]]
20000	['21000','22000']	[6,[5,[4,[3,2]]]]
11000	3
12000	['12100','12200']	[2,[1,[7,3]]]
12100	2		
12200	['12210','12220']	[1,[7,3]]
12210	1
12220	['12221','12222']	[7,3]
12221	7
12222	3
21000	6
22000	['22100','22200']	[5,[4,[3,2]]]
