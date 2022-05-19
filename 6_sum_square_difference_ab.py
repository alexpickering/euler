import sys

limit = int(sys.argv[1])

def sum_of_squares():
    num = 0
    sum_total = 0
    while True:
        num += 1
        sum_total += num ** 2
        yield sum_total

def sum():
    num = 0
    sum_total = 0
    while True:
        num += 1
        sum_total += num
        yield sum_total


gen_first = sum_of_squares()
gen_second = sum()


for i in range(limit):
    first = next(gen_first)
    second = next(gen_second)

second = second ** 2


print(first)
print(second)
print(second - first)
