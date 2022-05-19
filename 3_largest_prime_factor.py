TEST_NUM = 13195
NUM = 600851475143

def prime_generator():
    yield 2
    n = 1
    while 1:
        n += 2
        end = n // 2
        for i in range(2, end + 1):
            if n % i == 0:
                break

            if i == end:
                yield n
                break



def factor_finder(num):
    gen = prime_generator()
    num_end = num // 2
    largest = 1
    prime = 2
    while prime < num_end:
        prime = next(gen)
        if num % prime == 0:
            print(prime)
            largest = max(largest, prime)

    print('largest:')
    print(largest)
    return


if __name__ == '__main__':
    #factor_finder(TEST_NUM)
    factor_finder(NUM)
