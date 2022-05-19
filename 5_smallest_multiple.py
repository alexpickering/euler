def smallest_mult(n):
    original_mult_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    smallest = 1000000000
    test = smallest
    while test > n:
        for i in range(11, 21):
            if not test % i == 0:
                break
            elif i == n:
                smallest = min(smallest, test)

        test -= 1
    print(smallest)




#smallest_mult(10)
smallest_mult(20)
