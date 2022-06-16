"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time


def is_odd(n):
    return n % 2 == 1


col_cache = {1: 1}

def collatz(n, chain=0):
    global col_cache
    if n in col_cache:
        return col_cache[n]

    start = n
    while n >= 1:
        if n in col_cache:
            chain += col_cache[n]
            break
        else:
            chain += 1
            if is_odd(n):
                n = 3 * n + 1
            else:
                n = n // 2
    col_cache[start] = chain

    return chain



def max_collatz_chain_in(r):
    max_chain = 0
    max_start = 0
    for i in range(1, r):
        if (new_chain := collatz(i)) > max_chain:
            max_chain = new_chain
            max_start = i
    return max_start, max_chain


def main():
    t0 = time.perf_counter()
    max_start, max_chain = max_collatz_chain_in(1000000)
    t1 = time.perf_counter()
    print((max_start, max_chain))
    print(t1 - t0)

    #t0 = time.perf_counter()
    #print(collatz(40))
    #t1 = time.perf_counter()
    #print(collatz(13))
    #t2 = time.perf_counter()
    #print(t1 - t0)
    #print(t2 - t1)


if __name__ == '__main__':
    main()
