from functools import cache, reduce
from math import sqrt


@cache
def sq(x):
    return x * x

def check_pythagorean(a, b, c):
    return sq(a) + sq(b) == sq(c)

def test_abc_sum():
    assert sum([a, b, c]) == 1000


def find_pythagorean_triplet(abc_sum):
    # list of all squares
    squares_to_nums = {sq(i): i for i in range(abc_sum, 0, -1)}

    for c2, c in squares_to_nums.items():
        #print(f'c2: {c2}, c: {c}')
        for b2, b in squares_to_nums.items():
            #print(f'b2: {b2}, b: {b}')
            if (possible_a2 := c2 - b2) in squares_to_nums:
                if sum(((a := squares_to_nums[possible_a2]), b, c)) == abc_sum:
                    print('*'*80)
                    print(f'a: {a}\nb: {b}\nc: {c}')
                    return reduce(lambda x, y: x * y, [a, b, c])

def main():
    #print(find_pythagorean_triplet(12))
    print(find_pythagorean_triplet(1000))


if __name__ == '__main__':
    main()
