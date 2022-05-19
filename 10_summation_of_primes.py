from 3_largest_prime_factor import prime_generator



def prime_sum_to(limit)
    gen = prime_generator()
    prime_sum = 0
    prime = 0
    while prime < limit:
        prime_sum += prime
        prime = next(gen)


def main():
    prime_sum_to(10)
    #prime_sum_to(2000000)


if __name__ == '__main__':
    main()
