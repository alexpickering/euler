from math import prod

grid = [
    [ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65],
    [52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92],
    [16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40],
    [ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54],
    [ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]
    ]

# store starting x,y, pattern by number, and product
# access by grid[y][x]

#def prod(nums):
#    return reduce(lambda x,y: x * y, nums)

def is_in_grid(end):
    assert isinstance(end, tuple)
    return all(n in range(20) for n in end)


def val_at(coords):
    assert isinstance(coords, tuple)
    x, y = coords
    return grid[y][x]


def horizontal_transform(x, y):
    return [(x + i, y) for i in range(4)]


def vertical_transform(x, y):
    return [(x, y + i) for i in range(4)]


def backslash_diagonal_transform(x, y):
    return [(x + i, y + i) for i in range(4)]


def forward_slash_diagonal_transform(x, y):
    return [(x - i, y + i) for i in range(4)]


def iter_grid_coords():
    for y in range(20):
        for x in range(20):
            yield (x, y)


def func():
    transforms = [func for name, func in globals().items()
                  if callable(func) and name.endswith('_transform')]
    grid_coords = iter_grid_coords()
    cur_max = 0
    init_coords = (0, 0)
    trans_func = None
    for xy in grid_coords:
        for transform in transforms:
            line = transform(*xy)
            if is_in_grid(line[-1]):
                line_vals = [val_at(xy) for xy in line]
                if (new_max := prod(line_vals)) > cur_max:
                    cur_max = new_max
                    init_coords = xy
                    trans_func = transform.__name__

    print(init_coords, trans_func)
    return cur_max


def test_is_in_grid():
    assert is_in_grid((3, 0)) is True
    assert is_in_grid((8, 5)) is True
    assert is_in_grid((22, 0)) is False
    assert is_in_grid((22, 19)) is False
    assert is_in_grid((3, 3)) is True
    assert is_in_grid((0, 3)) is True
    assert is_in_grid((-3, -3)) is False


def test_val_at():
    assert val_at((0, 0)) == 8
    assert val_at((4, 2)) == 55
    assert val_at((18, 18)) == 5


def main():
    print(func())


if __name__ == '__main__':
    main()
