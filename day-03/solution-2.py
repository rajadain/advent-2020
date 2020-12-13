def count_trees_in_slope(slope, right, down):
    """
    Given a map of trees in `slope`, the number of moves `right`
    and `down` to make on every step, returns the number of trees #s
    encountered.
    """

    num_trees = 0
    x = 0
    y = 0

    while y < len(slope):
        if slope[y][x % 31] == '#':
            num_trees += 1

        x += right
        y += down

    return num_trees


slope = []

with open('input-1.txt') as f:
    slope = f.readlines()

one = count_trees_in_slope(slope, 1, 1)  # 61
two = count_trees_in_slope(slope, 3, 1)  # 265
three = count_trees_in_slope(slope, 5, 1)  # 82
four = count_trees_in_slope(slope, 7, 1)  # 70
five = count_trees_in_slope(slope, 1, 2)  # 34

print(one * two * three * four * five)  # 3154761400
