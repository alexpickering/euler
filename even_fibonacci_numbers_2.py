def fib():
    x, y = 0, 1
    while 1:
        x, y = y, x + y
        yield y

gen = fib()
result, tmp = 0, 0
while tmp < 4000000:
    if not tmp % 2:
        result += tmp
    tmp = next(gen)

print(result)
