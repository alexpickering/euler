
#TODO: have 0 and 1 evaluate to false
# 0 (if n)
# 1 (if not n in (0, 1))

# divisible by one and itself
def is_prime(n):
    if n in (0, 1):
        return False
    else:
        return all(n % i for i in range(2, n))


def prime_gen():
    n = 0
    while True:
        if is_prime(n):
            yield n
        n += 1


def nth_prime(n):
    p_gen = prime_gen()
    for i in range(0, n):
        nth_prime = next(p_gen)
    print(nth_prime)


nth_prime(10001)


primes = [2, 3, 5, 7, 11, 13]
