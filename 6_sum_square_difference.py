#
## sum(square(x) for x in range(1,11))
#
#a = sum(x ** 2 for x in range(1,11))
#print(a)
#
#b = sum(range(1,11)) ** 2
#print(b)
#
#print(b - a)
#
print(sum(range(1,101)) ** 2 - sum(x ** 2 for x in range(1,101)))

